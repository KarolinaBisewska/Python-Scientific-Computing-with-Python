class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item["amount"]
        return balance

    def transfer(self, amount, destination_category):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": f"Transfer to {destination_category.name}"})
            destination_category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:
            description = item["description"][:23]
            amount = f"{item['amount']:.2f}"
            items += f"{description:<23}{amount:>7}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total

def create_spend_chart(categories):
    # Calculate total spent and spent per category
    spent_per_category = []
    total_spent = 0
    for category in categories:
        spent = 0
        for item in category.ledger:
            if item["amount"] < 0:
                spent += -item["amount"]
        spent_per_category.append(spent)
        total_spent += spent

    # Calculate percentages and round down to nearest 10
    percentages = []
    for spent in spent_per_category:
        if total_spent > 0:
            percentage = (spent / total_spent) * 100
            percentage = int(percentage // 10 * 10)  # Round down to nearest 10
        else:
            percentage = 0
        percentages.append(percentage)

    # Create chart
    chart = "Percentage spent by category\n"
    for i in range(100, -10, -10):
        chart += f"{i:>3}| "
        for percentage in percentages:
            chart += "o  " if percentage >= i else "   "
        chart += "\n"
    chart += "    -" + "---" * len(categories) + "\n"

    # Get category names and find max length
    names = [category.name for category in categories]
    max_length = max(len(name) for name in names) if names else 0

    # Add category names vertically
    for i in range(max_length):
        chart += "     "
        for name in names:
            chart += name[i] + "  " if i < len(name) else "   "
        chart += "\n"

    return chart.rstrip("\n")
