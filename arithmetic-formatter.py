def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    
    top_row = []
    bottom_row = []
    dash_row = []
    answer_row = []
    
    for problem in problems:
        # Split problem into operands and operator
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Invalid problem format."
        
        num1, operator, num2 = parts
        
        # Validate operator
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        
        # Validate digits
        if not (num1.isdigit() and num2.isdigit()):
            return "Error: Numbers must only contain digits."
        
        # Validate number length
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        # Calculate width needed (length of longest operand plus operator and space)
        width = max(len(num1), len(num2)) + 2
        
        # Format numbers right-aligned
        top_row.append(num1.rjust(width))
        bottom_row.append(operator + num2.rjust(width - 1))
        dash_row.append('-' * width)
        
        # Calculate answer if needed
        if show_answers:
            if operator == '+':
                answer = str(int(num1) + int(num2))
            else:
                answer = str(int(num1) - int(num2))
            answer_row.append(answer.rjust(width))
    
    # Join rows with four spaces between problems
    result = '    '.join(top_row) + '\n' + \
             '    '.join(bottom_row) + '\n' + \
             '    '.join(dash_row)
    
    # Add answer row if requested
    if show_answers:
        result += '\n' + '    '.join(answer_row)
    
    return result