from art import logo
from replit import clear

def add(n1, n2):
    """Adds two numbers together."""
    return n1 + n2

def subtract(n1, n2):
    """Subtracts two numbers."""
    return n1 - n2

def multiply(n1, n2):
    """"Multiplies two numbers."""
    return n1 * n2

def divide(n1, n2):
    """Divides two numbers."""
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculate(num1, num2, operation):
    return operations[operation](num1, num2)


print(logo)
num1 = float(input("What's the first number?: "))
calculating = True
while calculating:
    for symbol in operations:
        print(symbol)
    operation_symbol = input("Pick an operation from the list above: ")
    num2 = float(input("What's the second number?: "))
    result = calculate(num1, num2, operation_symbol)
    print(f"{num1} {operation_symbol} {num2} = {result}")
    continue_calulate = input(f"Would you like to continue calculating with {result}? (y/n): ").lower()
    if continue_calulate == "n":
        calculating = False
    else:
        num1 = result
        clear()
        print(logo)
