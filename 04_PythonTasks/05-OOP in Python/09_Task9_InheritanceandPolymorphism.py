"""
Author: Basel Amr Barakat
Email: baselamr52@gmail.com
Date: 2024-12-16
Task Name : Apply Inheritance and Polymorphism
Task Number : 9
Part : OOP in Python
Module : Python Programming Language for AI / ML
Submit_Number : 1

Description:
This task focuses on reinforcing concepts of inheritance and polymorphism in object-oriented programming. 
Students will practice creating parent and child classes, overriding methods, and demonstrating polymorphic behavior.

Requirement 1:
Title: Create a Parent Class Car
Description: Implement a class Car with attributes make, model, and year. Define a method start() that prints a message 
indicating the car is starting.

Requirement 2:
Title: Create a Subclass Electric Car
Description: Implement a subclass Electric Car that inherits from Car and overrides the start() method to print a message 
indicating the electric car is starting silently.

Requirement 3:
Title: Demonstrate Polymorphism
Description: Create instances of both Car and ElectricCar. Call the start() method on both instances to demonstrate polymorphism.
"""

# Requirment One : Create a Parent Class Car
class Car():
    """
    This is parent class car which represents a general car with its make, model and year.
    This Class provides a methode to simulate starting the car
    
    Attributes:
        make  (str) : The manufacturer of the car.
        model (str) : The model of the car.
        year  (int) : The year of the car when it was manufactured
    Methods:
        start()   : Which simulate starting the car
        changeInfo() : Whuch changes the information of the book
    """
    # Determining the constructor to intialize the attributes of the class make, model and year
    def __init__(self, make:str = "" , model: str = "", year : int = 0):
        # Initialize the attributes with the given arguments
        self.make=make
        self.model=model
        self.year=year
    def start(self):
        """
        This function simulates starting the car, it takes nothing and print the info of the
        car and that it is starting and returns nothing
        """
        print(f"The {self.model}  {self.make} {self.year} is starting....!")
    
# Requirment Two : Create a Subclass Electric Car
class ElectricCar(Car):
    """
    The ElectricCar class reprensents an electric car, inherting from Car class
    It overrides the start methode of the Car class to reflect starting of electric car silently
    """
    def start(self):
        """
        Simulates starting the electric car silently.
        Prints a message indicating the electric car is starting silently.
        """
        print(f"The {self.model}  {self.make} {self.year} is starting silently....!")
def main():
    # Requirement 3: Demonstrate Polymorphism
    # Create instances of both Car and ElectricCar and demonstrate polymorphic behavior.
    print("Welcome to the Inheritance and Polymorphism Task!")
    Normal_Car = Car(make="Hyundai",model="Accent",year=2018)
    Electric_Car = ElectricCar(make="Tesla",model="Model_1",year=2024)
    Normal_Car.start()
    Electric_Car.start()

if __name__ == "__main__":
    main()
