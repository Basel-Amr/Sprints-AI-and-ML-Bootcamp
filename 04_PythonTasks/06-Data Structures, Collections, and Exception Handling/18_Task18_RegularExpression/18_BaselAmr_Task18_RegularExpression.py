"""
Author: Basel Amr Barakat
Email: baselamr52@gmail.com
Date: 2024-12-18
Task Name : Data Structures, Collections, and Exception Handling - File Handling - Using Regular Expressions
Task Number : 18
Part :  File Handling
Module : Python Programming Language for AI / ML
Submit_Number : 1

Description:
This task introduces students to regular expressions for pattern matching, data extraction, and validation.
Students will practice creating regular expressions to solve common text-processing tasks

Requirement 1:
Description: 
Use regular expressions to extract all email addresses from a given text string.

Requirement 2:
Description: 
Implement a program that validates phone numbers in the format 
(XXX) XXX-XXXX and replaces any invalid numbers with ""Invalid Number"".

 

Requirement 3:
Description: 
Use regex with capturing groups to extract a date in the format DD-MM-YYYY from a string.
"""
import re

def extract_emails(text):
    """
    Extract all email addresses from a given text using regular expressions.

    Args:
        text (str): The input text containing potential email addresses.

    Returns:
        list: A list of extracted email addresses.
    """
    email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    return re.findall(email_pattern, text)

def validate_and_replace_phone_numbers(text: str) -> str:
    """
    Validates phone numbers in the text and replaces invalid ones with 'invalid'.
    
    Args:
        text (str): The input text containing phone numbers.
        
    Returns:
        str: The text with valid phone numbers unchanged and invalid ones replaced with 'invalid'.
    """
    # Regular expression to strictly match valid phone numbers (XXX) XXX-XXXX
    phone_pattern = re.compile(r'\(\d{3}\) \d{3}-\d{4}')
    
    def replace_invalid(match):
        phone = match.group()
        return phone if phone_pattern.fullmatch(phone) else 'invalid'
    
    # Replace all phone-like patterns
    result = re.sub(r'\(\d{1,4}\) \d{1,4}-\d{1,5}', replace_invalid, text)
    return result



def extract_dates(text: str) -> list:
    """
    Extracts all dates in the format DD-MM-YYYY from the given text using regular expressions.
    
    Args:
        text (str): The input text containing dates.
        
    Returns:
        list: A list of dates found in the text in DD-MM-YYYY format.
    """
    # Regular expression to match dates in DD-MM-YYYY format
    date_pattern = re.compile(r'\b(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(\d{4})\b')
    
    # Find all dates matching the pattern
    dates = date_pattern.findall(text)
    
    # Format the extracted tuples into a proper date string
    formatted_dates = [f"{day}-{month}-{year}" for day, month, year in dates]
    return formatted_dates

def main():
    print("Welcome to the Regular Expression Utility!")
    while True:
        print("\nChoose an option:")
        print("1. Extract email addresses from a text")
        print("2. Validate and replace phone numbers in a text")
        print("3. Extract dates in the format DD-MM-YYYY")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            text = input("Enter the text containing email addresses: ")
            emails = extract_emails(text)
            if emails:
                print("Extracted Emails:")
                for email in emails:
                    print(email)
            else:
                print("No email addresses found.")

        elif choice == '2':
            text = input("Enter the text containing phone numbers: ")
            updated_text = validate_and_replace_phone_numbers(text)
            print("Updated Text:")
            print(updated_text)

        elif choice == '3':
            text = input("Enter the text containing dates: ")
            formatted_dates = extract_dates(text)
            print("Updated Text:")
            print(formatted_dates)

        elif choice == '4':
            print("Exiting the utility. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
