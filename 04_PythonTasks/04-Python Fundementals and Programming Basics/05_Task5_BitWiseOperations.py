"""
Author: Basel Amr Barakat
Email: baselamr52@gmail.com
Date: 2024-12-14
Task Name : BitWise Operations
Task Number : 5
Part : Operators in Python
Module : Python Programming Language for AI / ML
Submit_Number : 1

Description:
This task helps you learn to use bitwise operators in Python and perform operations on binary data and this task consist of three requirments
Requirement 1:
Title: Bitwise Operators.
Description: Implement bitwise operators such as & (AND).

Requirement 2:
Title: Binary Representation.
Description: Convert integer inputs into their binary representation using Python's built-in functions. Display the binary form of both the input and the result of the bitwise operations.

Requirement 3:
Title: Functions to Perform Operations.
Description: Define a Python function that takes two integer arguments and returns the result of performing a bitwise operation (AND, OR, XOR) on them. Allow the user to input the integers interactively.
"""



#Requirement One
#Title: Bitwise Operators.
#Description:  Implement bitwise operators such as & (AND).
def bitwise_operations(number1 : int, number2 : int, shift_base: int):
    """
    This function is used to take two numbers and make bitwise operations on them also it do shift_left, shift_right to both numbers
    Args:
        number1 (int)  : The first integer
        number2 (int)  : The second integer
        shift_base (int) : The Base that the user want to make shift on the both numbers
    Returns:
        result  (dict) : Results of the bitwise operations 
    Examples: 
        input   4   ---->   100
        input   1   ---->   001
        input   8   ---->   100
    """
    Result = {
        f"{number1} AND {number2} " : number1 & number2,
        f"{number1} OR {number2} "  : number1 | number2,
        f"{number1} XOR {number2} " : number1 ^ number2,
        f"shift left number1 ({number1} << {shift_base})" : number1 << shift_base,
        f"shift right number1 ({number1} >> {shift_base})" : number1 >> shift_base,
        f"shift left number2 ({number2} << {shift_base})" : number2 << shift_base,
        f"shift left number2 ({number2} >> {shift_base})" : number2 >> shift_base
    }
    return Result
#Requirement two
#Title: Binary Representation.
#Description:  Convert integer inputs into their binary representation using Python's built-in functions. Display the binary form of both the input and the result of the bitwise operations.
def convert_to_binary(number : int):
    """
    This function is used to convert a number to it's binary representation
    Args:
        number (int) : The integer that the user want to convert to it's binary representation
    Returns:
        binary (int) : The binary representation of that number in dict format
    """
    return bin(number)
#Requirement Three
#Title: Functions to Perform Operations.
#Description: Define a Python function that takes two integer arguments and returns the result of performing a bitwise operation (AND, OR, XOR) on them. Allow the user to input the integers interactively.
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

def main():
    print("BitWise Operations Task!")
    print("This task helps you learn to use bitwise operators in Python and perform operations on binary data and this task consist of three requirments")
    Enter_again = str('y')
    # Step 1: Implement bitwise operators on two numbers
    result = bitwise_operations(number1=2,number2=4,shift_base=1)
    for key, value in result.items():
        print(key,value)
    # Step 2: Convert the Reulst into Binary Representation
    print("Converting To Binary Representation")
    for key, value in result.items():   
        print(f"{key} | Decimal_Formate: {value} | Binary_Formate: {convert_to_binary(value)}")
    # Step 3 : Ask the user two enter two numbers and then make the bitwise operation on them
    Enter_again = str('y')
    while(Enter_again=='Y' or Enter_again=='y'):
        num1 = get_valid_number("Enter the first number : ")
        num2 = get_valid_number("Enter the second number : ")
        shift = get_valid_number("Enter the shift_base : ")
        result = bitwise_operations(number1=num1,number2=num2,shift_base=shift)     
        # Display the result in all formates
        for key, value in result.items():
            print(f"{key} | Decimal_Format: {value} | Binary_Format: {convert_to_binary(value)}")
        Enter_again = input("If you want to try again press y : ")
    print("Thanks for Trying our Simple Calculator Task")
    
if __name__ == "__main__":
    main()
