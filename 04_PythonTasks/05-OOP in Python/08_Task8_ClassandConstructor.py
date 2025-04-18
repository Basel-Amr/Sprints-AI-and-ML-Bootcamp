"""
Author: Basel Amr Barakat
Email: baselamr52@gmail.com
Date: 2024-12-16
Task Name : Create and Implement a Class with Constructor and Methods
Task Number : 8
Part : Classes in Python
Module : Python Programming Language for AI / ML
Submit_Number : 1

Description:
This task helps students practice defining and implementing Python classes, using constructors to initialize objects, and creating methods that define behaviors of those objects
and this task consist of  three requirments

Requirement 1:
Title: Define a Class with Attributes and Constructor
Description: Create a class Book with attributes title, author, and pages. Implement the __init__ constructor method to initialize these attributes.
Required Deliverable: Python Code File: Deliver the Python code containing the Book class, __init__ constructor, and the describe() method.

Requirement 2:
Title: Create a Method to Describe the Book
Description: Implement a method describe() in the Book class that outputs a string describing the book.
Required Deliverable:1. Screenshot: Provide a screenshot showing the instance of the Book class being created and the output of the describe() method.

Requirement 3:
Title: Instantiate and Test the Class.
Description: Create an instance of the Book class, initialize it with values for the attributes, and call the describe() method.
Required Deliverable: Code Output: Deliver the console output showing the description of the created book instance.
"""

# Requirment One
class Book():
    """
    This Book class represent a book description with its title, author and number of pages of the book
    This Class includes a constructor to initialize the book's attributes and providea description of the book
    This class also includes a method to change the information of the book if needed
    
    Attributes:
        title  (str) : The title of the book
        author (str) : The author of the book
        pages  (int) : The number of pages the book
    Methods:
        describe()   : Which display the information of the book
        changeInfo() : Whuch changes the information of the book
    """
    # Determining the constructor to intialize the attributes of the class title, author and number of pages
    def __init__(self, title:str = "" , author: str = "", pages : int = 0):
        """
        Constructor for the book class
        Args:
            title  (str) : The title of the book
            author (str) : The author of the book
            pages  (int) : The number of pages the book
        """
        # Initialize the attributes with the given arguments
        self.title=title
        self.author=author
        self.pages=pages
    # Reguirment Two
    # Creating a methode called Describe the book that prints all the information of the book title, author and number of pages
    def describe(self):
        """
        Print the information of the book and also return it to the user
        Returns:
            info (str) : A full description  for the book including  title, author and num_of_pages
        """
        print("-------------------------------------------------")
        print(f"The Title of the book           : {self.title} ")
        print(f"The Author of the book          : {self.author}")
        print(f"The No of Pages of the book     : {self.pages} ")
        print("-------------------------------------------------")
        info = f"'{self.title}' by {self.author}, {self.pages} pages."
        return info
    def changeInfo(self):
        """
        This Function is used by the user to change the info of the book, it asks the user
        about what he wants to change title, author and num_of_pages then it asks the user
        about the new data then it changes it for him
        """
        while(True):
            print("Press 1 to change The title of the book")
            print("Press 2 to change The author of the book")
            print("Press 3 to change The num_of_pages of the book")
            print("Press q to exit")
            choice = input("Enter Your Choice : ")
            if(choice=='1'):
                #title = input("Enter the new title of the book")
                self.title = input("Enter the new title of the book : ")
            elif(choice=='2'):
                #author = input("Enter the new author of the book")
                self.author = input("Enter the new author of the book : ")
            elif(choice=='3'):
                #num_of_pages = input("Enter the new num_of_pages of the book")
                self.pages = input("Enter the new num_of_pages of the book : ")
            elif(choice=='q'):
                print("Exiting the function")
                break
            else:
                print('Invalid Number ! ')

def main():
    print("Welcome to the Class and Constructor Task!")

    # Requirement 3: Instantiate and Test the Class
    # Create an instance of the Book class and call the describe method.
    # Book1 : Try attributes
    book1 = Book(title = "Python OOB Book",author="Steve McConnel",pages="500")
    # Book2 : Try default values
    book2 = Book()
    # Try Describe methode
    book1_info = book1.describe()
    book2_info = book2.describe()
    #Try changeInfo methode
    book2.changeInfo()
    book2.describe()
if __name__ == "__main__":
    main()
