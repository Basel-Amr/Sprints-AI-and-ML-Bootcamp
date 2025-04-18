"""
Author: Basel Amr Barakat
Email: baselamr52@gmail.com
Date: 2024-12-14
Task Name : FizzBuzz Control Flow
Task Number : 6
Part : Python Control FLow
Module : Python Programming Language for AI / ML
Submit_Number : 1

Description:
This task helps you practice control flow using conditional statements and loops to solve the FizzBuzz problem and this task consist of three requirments
Requirement 1:
Title: Control Flow with if, elif, else.
Description: Use if, elif, and else statements to implement the FizzBuzz logic: Print ""Fizz"" if a number is divisible by 3, ""Buzz"" if divisible by 5, and ""FizzBuzz"" if divisible by both 3 and 5.

Requirement 2:
Title: Loops (e.g., for loop).
Description: Use a for loop to iterate over a range of numbers (e.g., 1 to 100) and apply the FizzBuzz logic to each number in the sequence. Ensure that the loop correctly prints the required output for each case.

Requirement 3:
Title: User Input .
Description:  Allow the user to enter a custom range for the FizzBuzz sequence (e.g., starting number and ending number). Validate that the user inputs valid integers and handle any errors gracefully.
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

def fizzbuzzDisplay(start: int, end: int):
    """
    This function takes start,end as an integer and print fizzbuzz according to the input
    args:
        start (int) : The beginning of the sequence
        end   (int) : The end of the sequence
    Returns:
        None
    """
    for i in range(start,end+1,1):
        #Print FizzBuzz if a number is divisable by 3 and 5
        if (i % 3 == 0 and i % 5 == 0):
            print(f"{i} : FizzBuzz")
        #Print Fizz if a number is divisable by 3
        elif(i%3==0):
            print(f"{i} : Fizz")
        #Print Buzz if a number is dibisable by 5 
        elif(i%5==0):
            print(f"{i} : Buzz")
        
    
def main():
    print("FizzBuzz Control Flow Task!")
    print("This task helps you to practice Control Flow")
    Enter_again = str('y')
    # Requirment1 and Requirment2 : Try the function on Custome Range from 1 to 100
    fizzbuzzDisplay(start=1,end=100)
    # Requirement 3: User Input
    Enter_again = str('y')
    while(Enter_again=='Y' or Enter_again=='y'):
        st = get_valid_number("Enter the beginning of the sequence : ")
        en = get_valid_number("Enter the end of the sequence  : ")  
        fizzbuzzDisplay(start=st,end=en)
        Enter_again = input("If you want to try again press y : ")
    print("Thanks for Trying our FizzBuzz Control Flow Task")
    
if __name__ == "__main__":
    main()
