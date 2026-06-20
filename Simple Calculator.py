# -*- coding: utf-8 -*-
"""
Simple Calculator
"""
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def calculator():
    print("=" * 30)
    print("      Simple Calculator")
    print("=" * 30)

    while True:
        print("\nOperations:")
        print("  1. Add")
        print("  2. Subtract")
        print("  3. Multiply")
        print("  4. Divide")
        print("  5. Quit")

        choice = input("\nChoose an operation (1-5): ").strip()

        if choice == "5":
            print("Goodbye!")
            break

        if choice not in ("1", "2", "3", "4"):
            print("Invalid choice. Please enter 1-5.")
            continue

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        if choice == "1":
            result = add(num1, num2)
            op = "+"
        elif choice == "2":
            result = subtract(num1, num2)
            op = "-"
        elif choice == "3":
            result = multiply(num1, num2)
            op = "*"
        elif choice == "4":
            result = divide(num1, num2)
            op = "/"

        print(f"\nResult: {num1} {op} {num2} = {result}")


if __name__ == "__main__":
    calculator()
