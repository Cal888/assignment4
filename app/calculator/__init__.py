"""
app/calculator.py

REPL calculator that takes user input.

Provides user with help and history of calculations performed during their session.

Provides user with exit stategies as well.
"""

import sys
from typing import List
from app.calculation import Calculation, CalculationFactory

#--------------------------------------
# Helper Functions
#--------------------------------------

def display_help() -> None:
    """Displays help instructions for the user."""

    help_message = """
    REPL Calculator Help
    --------------------

    Operations:
        <number1> <operator> <number2>
        - Perform a calculation with a supported operator and two numbers.
        
        Supported Operations:
        +   : Adds two operands.
        -   : Subtracts the second operand from the first.
        *   : Multiplies two operands.
        /   : Divide first operand by the second.
        **  : First operand to the power of the second.
        %   : Remainder of first operand divided by second.

    Special Commands:
        help    : Displays this help message.
        history : Shows the history of calculations.
        exit    : Exits the calculator.

    Examples:
        3 + 3
        5 - 2
        3 * 4
        4 / 2
        2 ** 2
        8 % 2
    """

    print(help_message)

def display_history(history: List[Calculation]) -> None:
    """Displays the history of calculations performed during the users session."""

    if not history:
        print("No calculations performed yet.")
    else:
        print("Calculation History:")
        for idx, calculation in enumerate(history, start=1):
            print(f"{idx}. {calculation}")

#--------------------------------------
# REPL Calculator Main Function
#--------------------------------------

def calculator() -> None:
    """
    REPL calculator that performs:
     - Addition
     - Subtraction
     - Multiplication
     - Division
     - Power
     - Modulus
    """

    history: List[Calculation] = []

    print("Welcome to the REPL calculator!")
    print("Type 'help' for instructions or 'exit' to quit")

    while True:
        try:
            user_input: str = input(">> ").strip().lower()

            # If empty, prompt user to enter the calculation again.
            if not user_input:
                continue       # pragma: no cover

            # If the user needs help, they can type 'help'.
            elif user_input == "help":
                display_help()
                continue       # prompt user to try again

            # If the user wants to see their calculation history, they can type 'history'.
            elif user_input == "history":
                display_history(history) 
                continue

            # If the user wants to exit, they can type 'exit'.
            if user_input == "exit":
                print("Exiting REPL calculator. Goodbye!")
                sys.exit(0)    # pragma: no cover

            # Parsing input
            try:
                num1_str, operator, num2_str = user_input.split()
                num1: float = float(num1_str)
                num2: float = float(num2_str)
            except ValueError:
                print("Invalid input. Please use the format: <number1> <operator> <number2>")
                print("Type 'help' for more information.")
                continue       # prompt user to try again

            # Attempt to create calculation instance
            try:
                calculation = CalculationFactory.create_calculation(num1, operator, num2)
            except ValueError as ve:
                print(ve)
                print("Type 'help' for a list of supported operations.")
                continue       # prompt user to try again

            # Attempt to execute calculation
            try:
                result = calculation.execute()
            # Division by zero error
            except ZeroDivisionError as ze:
                print(ze)
                print("Please enter a non-zero divisor.")
                continue       # prompt user to try again
            # Handle any unforseen errors
            except Exception as e:
                print(f"An error occurred during calculation: {e}")
                print("Please try again.")
                continue       # prompt user to try again

            # Print the calculation result string
            result_str: str = f"{calculation}"
            print(f"Result: {result_str}")

            # Append the calculation to the history list
            history.append(calculation)

        except KeyboardInterrupt:
            print("Keyboard interupt detected. Exiting calculator. Goodbye!")
            sys.exit(0)        # pragma: no cover

        except EOFError:
            print("EOF detected. Exiting calculator. Goodbye!")
            sys.exit(0)        # pragma: no cover

# If this script is ran directly, start the calculator REPL.
if __name__ == "__main__":
    calculator()               # pragma: no cover











