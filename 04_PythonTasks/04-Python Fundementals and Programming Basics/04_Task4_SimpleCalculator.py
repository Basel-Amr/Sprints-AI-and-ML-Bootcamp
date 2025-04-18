"""
Author: Basel Amr Barakat
Email: baselamr52@gmail.com
Date: 2024-12-14
Task Name : Simple Calculator Task
Task Number : 4
Part : Introduction to Python
Module : Python Programming Language for AI / ML
Submit_Number : 1

Description:
This task helps you practice creating a basic calculator that performs arithmetic operations using Python and this task consist of three requirments
Requirement 1:
Title: Variables and Data Types
Description: Create a calculator using variables to store input values. Use appropriate data types (integers or floats) for the calculations.

Requirement 2:
Title: Arithmetic Operators.
Description: Implement basic arithmetic operations such as addition, subtraction, multiplication, and division using Python operators.

Requirement 3:
Title: User Input Validation.
Description: Use Python's input() function to receive user input. Ensure the input is valid (e.g., check if the user inputs a number). If the input is invalid, prompt the user again.
"""

#Requirement One
def get_valid_number(Message : str):
    """
    This functions display a message for the user and ask him to enter a number that he want to make the operation on and 
    also check the validity of the number, and if he entered something rather than a number, it will raise an error and display
    an error message to the user and ask him to try again
    Args:
        Message (str): The message to display to the user.

    Returns:
        float: A valid number input by the user.
    Examples:
        "Enter the first number: "  :   15
        "Enter the first number: "  :   'a'  ---> display error message "Invalid input. Please enter a valid number."
    """
    # Here We will display the messaeg and ask the user to enter a number
    user_input = input(Message)
    invalid_number = False
    # Here we will check the valadity of the number
    # The while loop here will work until the user enters a valid number
    while(True):
        if(invalid_number):
            user_input = input()
        try:
            # If the user entered a number, we will convert it into float because the input() function return a str and then we will return it
            return float(user_input)
        except ValueError:
            # If the user entered an invalid number, we will reject it and ask the user to enter a number again
            print("Invalid input. Please enter a valid number. : ")
            invalid_number = True
def do_arithmeticOperations(number1: int, number2: int):
    """
    This functions takes two numbers as an arguments and make all the possible 
    arithmetic operations on them such as +,-,*,^,/,%
    Args:
        number1 (int): the first number
        number2 (int): the second number
    Returns:
        result (dict): A dictionary which contains all the results of the arithmetic operations
    """
    # Requirement 2:  Arithmetic Operators.
    # Implement basic arithmetic operations such as addition, subtraction, multiplication, and division using Python operators.
    # Addition
    addition = number1 + number2
    # Subtraction
    subtraction = number1 - number2
    # Multiplication
    multiplication = number1 * number2
    # Power
    power = number1 ** number2
    # Division ---> Check for invalid because we can not divide by zero
    try:
        division = number1 / number2
        reminder = number1 % number2
    except ZeroDivisionError:
        division = "Undefined (division by zero)"
        reminder = "Undefined (reminder by zero)"
    result = {
         f"addition {number1} + {number2} = " :addition,
         f"subtraction {number1} - {number2} = " : subtraction,
         f"multiplication {number1} * {number2} = " : multiplication,
         f"power {number1} ** {number2} = " : power,
         f"division {number1} / {number2} = " : division,
         f"reminder {number1} % {number2} = " : reminder,

     }
    return result
def main():
    print("Simple Calculator Task!")
    print("This Task help us to practice creating a basic calculator that performs arithmetic operations")
    Enter_again = str('y')
    while(Enter_again == 'y' or Enter_again == 'Y'):
        # Step 1: Ask The User to enter two numbers that he want to make an operation on
        first_number = get_valid_number("Enter the first number: ")
        second_number = get_valid_number("Enter the second number: ")
        result = do_arithmeticOperations(number1=first_number, number2=second_number)         
        # Step 3: Display results
        print("\nResults:")
        for operation, value in result.items():
            print(operation, value)
            #print(f"{operation}: {first_number} , {second_number} = {value}")
        Enter_again = input("If you want to try again press y : ")
    print("Thanks for Trying our Simple Calculator Task")

    
if __name__ == "__main__":
    main()
