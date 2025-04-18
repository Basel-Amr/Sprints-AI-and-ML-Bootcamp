"""
Author: Basel Amr Barakat
Email: baselamr52@gmail.com
Date: 2024-12-18
Task Name : Utilize Specialized Collections
Task Number : 15
Part :  Implement Try/Except Blocks and User-Defined Exceptions
Module : Python Programming Language for AI / ML
Submit_Number : 1

Description:
This task focuses on handling errors using try/except blocks and creating custom exceptions for better error management.
Students will implement robust error handling in Python programs.

Requirement 1:
Title: Handle Built-in Exception.
Description: Implement a program that asks the user for a number. Handle invalid input using try/except for ValueError.

Requirement 2:
Title: Create and Use a User-Defined Exception.
Description: Create a custom exception class AgeError that is raised when a user enters an invalid age
(less than 0 or greater than 120).


Requirement 3:

Title Use Finally and Else Clauses
Description: Implement a program where resources are cleaned up in a finally block,
and code is executed if no exceptions occur using the else clause.
"""
class AgeError(Exception):
    """
    Custom exception class for handling invalid age input.

    Raised when the age entered by the user is less than 0 or greater than 120.
    """
    def __init__(self, message="Age must be between 0 and 120"):
        self.message = message
        super().__init__(self.message)


def handle_built_in_exception():
    """
    Handles ValueError exceptions when asking the user for a number.

    Prompts the user for a number and catches invalid input using a try/except block.
    """
    while True:
        try:
            user_input = input("Please enter a number: ")
            number = float(user_input)
            print(f"You entered the number: {number}")
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def check_age():
    """
    Checks the user's age and raises a custom AgeError for invalid age values.

    Prompts the user to enter their age and validates it.
    """
    while True:
        try:
            age = int(input("Please enter your age: "))
            if age < 0 or age > 120:
                raise AgeError
            print(f"Your age is valid: {age}")
            break
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
        except AgeError as e:
            print(f"Error: {e}")


def process_numbers_file(file_name: str) -> None:
    """
    Reads a file, sums up numbers, and demonstrates the use of `finally` and `else`.

    Args:
        file_name (str): The name of the file containing numbers.

    Steps:
        1. Open the file safely.
        2. Attempt to read numbers and compute their sum.
        3. Use `else` to display the result if no errors occur.
        4. Use `finally` to ensure the file is closed.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file contains invalid data.
    """
    try:
        file = open(file_name, 'r')  # Try to open the file
        print(f"File '{file_name}' opened successfully!")
        numbers = file.readlines()  # Read all lines from the file
        numbers = [int(num.strip()) for num in numbers]  # Convert lines to integers
        total = sum(numbers)  # Calculate the sum
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")
    except ValueError:
        print("Error: The file contains invalid data. Only integers are allowed.")
    else:
        print(f"The sum of the numbers in the file is: {total}")
    finally:
        # Ensure file is closed if it was opened
        try:
            file.close()
            print("File closed successfully.")
        except NameError:
            # This handles the case where the file variable was never defined
            print("No file to close.")


def main():
    """
    Main interactive function to execute the tasks based on user choice.

    Provides an interface for the user to choose from the three requirements.
    """
    while True:
        print("\n*** Exception Handling Demo ***")
        print("1. Handle Built-in Exception")
        print("2. Create and Use a User-Defined Exception")
        print("3. Use Finally and Else Clauses")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            print("\n--- Handling Built-in Exception ---")
            handle_built_in_exception()
        elif choice == "2":
            print("\n--- Checking Age with User-Defined Exception ---")
            check_age()
        elif choice == "3":
            print("\n--- Demonstrating Finally and Else Clauses ---")
            file_name = input("Please Input the file you want to read and process on :")
            process_numbers_file(file_name)
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")


if __name__ == "__main__":
    main()
