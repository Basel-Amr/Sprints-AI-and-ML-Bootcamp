"""
Author: Basel Amr Barakat
Email: baselamr52@gmail.com
Date: 2024-12-18
Task Name : Working with Dates and Times
Task Number : 17
Part :  File Handling
Module : Python Programming Language for AI / ML
Submit_Number : 1

Description:
This task focuses on performing date/time operations using Python’s datetime and calendar modules.
Students will practice working with date/time objects and performing arithmetic on dates.

Requirement 1:
Description: 
Create a datetime object for the current date and time. Format the date as YYYY-MM-DD and time as HH:MM:SS.

Requirement 2:
Description: 
Calculate the date 10 days from today and the date 10 days ago. Display both dates.

Requirement 3:
Description: 
Extract the year, month, day, hour, minute, and second from the current datetime object and print them.
"""

from datetime import datetime, timedelta

# Requirement 1:
def formate_current_datetime()->None:
    """
    This function is used to display the current date and time formated as
    - Date: YYYY-MM-DD
    - Time: HH:MM:SS
    """
    today = datetime.now().strftime("%Y-%m-%d")
    now = datetime.now().strftime("%H:%M:%S")
    print(f"Current Date: {today}")
    print(f"Current Time: {now}")

# Requirement 2:
def date_arithmetic() -> None:
    """
    Calculate and display:
    - The date 10 days from today.
    - The date 10 days ago.
    """
    today = datetime.now().date()
    after_tendays = today + timedelta(days=10)
    before_tendays = today - timedelta(days=10)
    print(f"Date 10 days from today: {after_tendays}")
    print(f"Date 10 days ago: {before_tendays}")

# Requirement 3:
def extract_datetime_components() -> None:
    """
    Extract and display individual components (year, month, day, hour, minute, second)
    from the current datetime object.
    """
    now = datetime.now()
    print("Current Date and Time Components:")
    print(f"Year   : {now.year}")
    print(f"Month  : {now.month}")
    print(f"Day    : {now.day}")
    print(f"Hour   : {now.hour}")
    print(f"Minute : {now.minute}")
    print(f"Second : {now.second}")

def main():
    print("\n--- Date/Time Operations Menu ---")
    print("Trying first requirement displaying current date in formate %YYYY-%MM-%DD and time in formate %H-%M-%S")
    formate_current_datetime()
    print("--"*15)
    print("Trying second requirement Calculate the date 10 days from today and the date 10 days ago. Display both dates.")
    date_arithmetic()
    print("--"*15)
    print("Trying third requirement  Extract and display individual components (year, month, day, hour, minute, second")
    extract_datetime_components()
    print("--"*15)
    print("Exiting the program. Have a great day!")
# Entry point for the script
if __name__ == "__main__":
    main()