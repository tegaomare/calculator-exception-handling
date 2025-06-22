# Author: Tega Omarejedje
# Project: Error-Free Calculator with Exception Handling and Logging
# Date: 06/21/2025

import logging

# Configure logging to write to error_log.txt
logging.basicConfig(filename='error_log.txt', level=logging.ERROR, format='%(levelname)s:%(message)s')

def get_number(prompt):
    """Prompt user for a number and handle non-numeric input."""
    while True:
        try:
            return float(input(prompt))
        except ValueError as ve:
            print("Invalid input! Please enter a valid number.")
            logging.error(f"ValueError occurred: {ve}")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError as zde:
        print("Oops! Division by zero is not allowed.")
        logging.error(f"ZeroDivisionError occurred: {zde}")
        return None

def calculator_menu():
    print("Welcome to the Error-Free Calculator!")
    while True:
        print("\nChoose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("> ")

        if choice == "5":
            print("Goodbye!")
            break

        if choice not in {"1", "2", "3", "4"}:
            print("Invalid choice. Please enter a number from 1 to 5.")
            continue

        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")

        try:
            if choice == "1":
                result = add(num1, num2)
                print(f"The result of addition is: {result}")
            elif choice == "2":
                result = subtract(num1, num2)
                print(f"The result of subtraction is: {result}")
            elif choice == "3":
                result = multiply(num1, num2)
                print(f"The result of multiplication is: {result}")
            elif choice == "4":
                result = divide(num1, num2)
                if result is not None:
                    print(f"The result of division is: {result}")
        except Exception as e:
            print("An unexpected error occurred.")
            logging.error(f"Unexpected error: {e}")
        finally:
            print("Operation complete.")

# Run the calculator
calculator_menu()
