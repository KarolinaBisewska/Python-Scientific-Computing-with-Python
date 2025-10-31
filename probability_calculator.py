import copy
import random

class Hat:
    def __init__(self, **balls):
        # Build the contents list: one string per ball
        self.contents = []
        for color, count in balls.items():
            self.contents.extend([color] * count)
    
    def draw(self, num_balls):
        # If asked to draw more than available, return all
        if num_balls >= len(self.contents):
            drawn = self.contents[:]
            self.contents.clear()
            return drawn
        
        # Otherwise, draw without replacement
        drawn = random.sample(self.contents, num_balls)
        # Remove drawn balls from contents
        for ball in drawn:
            self.contents.remove(ball)
        return drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0
    
    for _ in range(num_experiments):
        # Deep copy the hat to avoid modifying the original
        hat_copy = copy.deepcopy(hat)
        
        # Draw the specified number of balls
        drawn_balls = hat_copy.draw(num_balls_drawn)
        
        # Count how many of each color we drew
        drawn_count = {}
        for ball in drawn_balls:
            drawn_count[ball] = drawn_count.get(ball, 0) + 1
        
        # Check if we have at least the expected number of each color
        meets_expectation = True
        for color, required in expected_balls.items():
            if drawn_count.get(color, 0) < required:
                meets_expectation = False
                break
        
        if meets_expectation:
            success_count += 1
    
    # Return probability as float
    return success_count / num_experiments
