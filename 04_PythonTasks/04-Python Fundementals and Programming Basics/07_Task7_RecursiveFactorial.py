"""
Author: Basel Amr Barakat
Email: baselamr52@gmail.com
Date: 2024-12-14
Task Name : Recursive Factorial
Task Number : 7
Part : Functions
Module : Python Programming Language for AI / ML
Submit_Number : 1

Description:
This task helps you implement a recursive function in Python to calculate the factorial of a given number.
"""

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
            return int(user_input)
        except ValueError:
            # If the user entered an invalid number, we will reject it and ask the user to enter a number again
            print("Invalid input. Please enter a valid number. : ")
            invalid_number = True

def factorial(num : int):
    """
    Recursive function to calculate the factorial of a number.

    Args:
        num (int): The number for which the factorial is calculated.

    Returns:
        int: The factorial of the given number.

    Raises:
        ValueError: If the input is negative.
    """
    # If the user entered a negative number, raise an error and display message
    if num < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    # Base : if the functions reaches this point, it will return 1 and will end the recursion 
    if num == 0 or num == 1:
        return 1
    return num * factorial(num - 1)
    
def main():
    print("Welcome to the Factorial Calculator Task!")

    Enter_again = str('y')
    while(Enter_again=='Y' or Enter_again=='y'):
        try:
            user_input = get_valid_number("Enter a non-negative integer to calculate its factorial: ")
            result = factorial(user_input)
            print(f"The factorial of {user_input} is {result}.")
        except ValueError as error:
            print(f"Error: {error}. Please enter a valid non-negative integer.")
        Enter_again = input("If you want to try again press y : ")
    print("Thanks for Trying our Factorial Calculator Task")
    
if __name__ == "__main__":
    main()
