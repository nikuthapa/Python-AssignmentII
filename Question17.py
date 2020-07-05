"""
Write a program that serves as a basic calculator. It asks for two
numbers, then it asks for an operator. Gracefully deal with input that
doesn't cleanly convert to numbers. Deal with division by zero errors.
"""


num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

a = input("Enter any operator (+, -, *, /):")


def basic_calculator(x, y, o):  # o stands for operator.
    if o == '+':
        return x + y
    elif o == '-':
        return x - y
    elif o == '*':
        return x * y
    elif o == '/':
        if y == 0:
            return "Error on division by zero."
        return x / y
    else:
        return "Operator does not exist. Please try given operators."


print(basic_calculator(num1, num2, a))