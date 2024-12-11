#Write a function that takes two numbers and an operator (+, -, *, /) as input, performs the operation, and returns the result.
def calculator(num1, num2, operator):
    """
    Perform basic arithmetic operations.
    
    Args:
        num1 (float): The first number.
        num2 (float): The second number.
        operator (str): The operator ('+', '-', '*', '/').
    
    Returns:
        float: The result of the operation.
    """
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero."
    else:
        return "Invalid operator."

# Test the function
print(calculator(10, 5, '+'))  # Output: 15
print(calculator(10, 5, '-'))  # Output: 5
print(calculator(10, 5, '*'))  # Output: 50
print(calculator(10, 0, '/'))  # Output: Error: Division by zero.
