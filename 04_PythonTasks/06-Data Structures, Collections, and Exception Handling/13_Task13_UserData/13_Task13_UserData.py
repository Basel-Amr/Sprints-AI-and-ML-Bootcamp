"""
Author: Basel Amr Barakat
Email: baselamr52@gmail.com
Date: 2024-12-18
Task Name : Compare and Use Data Structures in a Real-World Scenario
Task Number : 13
Part : Data Structures
Module : Python Programming Language for AI / ML
Submit_Number : 1

Description:
students will analyze different scenarios and decide which data structure (list, tuple, set, or dictionary)
is most suitable based on the needs of the application.

Requirement 1:
Title: Use a Dictionary for Efficient Data Storage
Description: Create a dictionary to store student records with keys such as name, age, grades.
Implement functions to add, update, and retrieve student records.

Requirement 2:
Title: Use a Set for Uniqueness
Description: Implement a set to track unique items in a shopping cart. Add and remove items from the cart while ensuring no duplicates.


Requirement 3:
Title: Use a Tuple for Immutable Data
Description: Use a tuple to store fixed configuration data for a software application (e.g., MAX_USERS, API_KEY, DATABASE_URL)."""

# Requirement 1 : Student Records Manager
class StudentManagmentSystem:
    """
    This class is used to manage student records

    Attributes:
        student_records (dict) : dictionary contains each student name, age, grades and avg grade

    methodes:
        add_record()       : This function is used to add a record to our system
        update_record()    : This function is used to update an existing record 
        retrieve_record()  : This function is used to retrieve a specific record 
        show_all_records() : This funciton is used to show all the existing records
    """
    # Constructor
    def __init__(self,records:dict=None)->None:
        self.students_records = {}
    # Function to calculate average_grades
    def average_grade(self,name:str)->float:
        """
        This function is used to calculate the average grades of the student
        Args:
            name (str) : The name of the student we want to calculate its average
        Return:
            avg_gradees (float) : The average grades of the student record
        """
       
        
        student = self.students_records[name]
        
        # Check if the grades are available for the student
        if "grades" not in student or not student["grades"]:
            print(f"No grades available for student: {name}")
            return 0.0  # Return 0.0 if no grades are available
        
        grades = student["grades"]
        
        # Calculate the average
        average = sum(grades) / len(grades)
        return average
    # Add Record
    def add_record(self, name:str=None, age:int=0, grades:list=[])->None:
        """
        This function is used to add a record to our system
        Args:
            name   (str)  : The Name of the student
            age    (int)  : The age of the student
            grades (list) : The grades of the student
        """
        self.students_records[name] = {"age": age, "grades": grades}
        avg_grades = self.average_grade(name)
        self.students_records[name]["avg_grades"] = avg_grades
        print(f"The Student record for {name} is added successfully!")
    
    # Update_Record
    def update_record(self, name:str=None, age:int=0, grades:list=[])->None:
        """
        This function is used to update a record to our system
        Args:
            name   (str)  : The Name of the student
            age    (int)  : The age of the student
            grades (list) : The grades of the student
        """
        if name in self.students_records:
            self.students_records[name] = {"age": age, "grades": grades}
            
            # After updating the record, calculate the average grade
            avg_grades = self.average_grade(name)
            self.students_records[name]["avg_grades"] = avg_grades
            
            print(f"Student record for {name} updated successfully!")
        else:
            print(f"No record found for student: {name}")

    # Retrieve record
    def retrieve_record(self, name:str=None)->None:
        """
        This function is used to retrieve a specific record in the system by its name
        Args:
            name (str) : The name of the student we want to retrieve
        """
        try:
            print(f"Record for student {name} : {self.students_records[name]}")
        except:
            print(f"No record found for student: {name}")
    
    def show_all_records(self)->None:
        """
        This function is used to show all the records in the system
        """
        print("All Student Records: ")
        for name, value in self.students_records.items():
            print(f"{name} : {value}")

# Requirement 2 : shopping cart
class ShoppingCartTracker:
    """
    This class is used to manage Shopping cart
    methodes:
        add_user()    : This function is used to add a new user to our cart
        add_item()    : This function is used to add an item to our cart
        remove_item() : This function is used to remove an existing item in our cart 
        show_items()  : This function is used to show all the items in our cart
    """
    # Constructor
    def __init__(self):
        self.carts = {}     # Dictionary to store user-specific carts, each name has its own set

    # add a new user
    def add_user(self, name:str)->None:
        """
        This function is used to add a new user with an empty cart
        """
        try:
            self.carts[name] = set()
            print(f"Cart created for user {name}.")
        except:
            print(f"User {name} already has a cart.")
    
    # add a new item
    def add_item(self, name:str, item)->None:
        """
        This function is used to add a new item to our user
        """
        try:
            if item in self.carts[name]:
                print(f"Item '{item}' is already in {name}'s cart.")
            else:
                self.carts[name].add(item)
                print(f"Item '{item}' added to {name}'s cart.")
            #self.carts[name].add(item)
            #print(f"Added '{item}' to {name}'s cart.")
        except:
            print(f"User {name} does not exist. User will be created first.")
            self.add_user(name=name)
            self.add_item(name,item)
            print(f"User {name} has been created with Cart {item}")

    # remove a new item
    def remove_item(self, name:str,item)->None:
        """
        This function is used to remove an item from our user's cart
        """
        try:
            self.carts[name].remove(item)
            print(f"Removed {item} from {name}'s cart")
        except KeyError:
            print(f"'{item}' not found in {name}'s cart.")
    
    # Show all items
    def show_items(self)->None:
        """
        This function is used to display all the users with their cart
        """
        print("\nAll Shopping Carts:")
        for name, cart in self.carts.items():
            print(f"{name}: {', '.join(cart) if cart else 'Empty cart'}")

# Requirement 3 : Configuration Data
class ConfigurationData:
    """"
    Stores immutable configuration data for a software application.
    methods:
        add_Configuration()       : This function is used to add a new configuration to our Data
        view_Configuration()      : This function is used to view the configration in our data
        retrieve_Configuration()  : This function is used to retrieve a specific configuration of a model
    """
    # Constructor
    def __init__(self)->None:
        # Initialize the configurations as an empty tuple
        self.config = ()
        
    # add Configuration
    def add_Configuration(self, model:str)->None:
        """
        Create a new configuration tuple with an additional key-value pair (e.g., MAX_USERS, API_KEY, DATABASE_URL)..
        Args:
            model (str): The configuration key.
        """
        # Concatenate a new tuple to the existing configuration
        Max_Users = input("Please enter max_users : ")
        API_KEY = input("Please enter API_KEY : ")
        DATABASE_URL = input("Please enter DATABASE_URL : ")
        value = (Max_Users,API_KEY,DATABASE_URL)
        # Create a new configuration tuple by adding the new item
        new_configuration = (model, value)
        self.config = self.config + (new_configuration,)
        print(f"Added new configuration: {model} = {value}")
    
    # view Configuration
    def view_Configuration(self)->None:
        """
        View the current configuration data.
        """
        print("Current Configuration:")
        if not self.config:
            print(f"No Configurations is added yet")
        else:
            print("Current Configurations:")
            for config in self.config:
                print(f"{config[0]}: {config[1]}")

    def retrieve_Configuration(self, key:str)->tuple:
        """
        Retrieve the value of a specific configuration key.

        Args:
            key (str): The configuration key to retrieve.

        Returns:
            value (tuple): The value of the specified key, or None if the key does not exist.
        """
        for config_key, value in self.config:
            if config_key == key:
                print(f"{config_key} | {value}")
                return value
        
        print(f"The key '{key}' does not exist.")
        return None

if __name__ == "__main__":
    print("Welcome to the Python Data Structures Demonstration!")
    student_manager = StudentManagmentSystem()
    shopping_cart = ShoppingCartTracker()
    config_viewer = ConfigurationData()

    while True:
        print("\nMain Menu:")
        print("1. Student Records Manager (Dictionary)")
        print("2. Shopping Cart Tracker (Set)")
        print("3. Configuration Viewer (Tuple)")
        print("4. Exit")
        main_choice = input("Enter your choice (1-4): ")

        if main_choice == "1":
            print("\n=== Student Records Manager ===")
            while True:
                print("\nOptions:")
                print("1. Add Student Record")
                print("2. Update Student Record")
                print("3. Retrieve Student Record")
                print("4. Show All Records")
                print("5. Back to Main Menu")
                choice = input("Enter your choice (1-5): ")

                if choice == "1":
                    name = input("Enter student name: ")
                    age = int(input("Enter student age: "))
                    grades = list(map(float, input("Enter student grades (comma-separated): ").split(',')))
                    student_manager.add_record(name, age, grades)

                elif choice == "2":
                    name = input("Enter the student name to update: ")
                    age = int(input("Enter updated age: "))
                    grades = list(map(float, input("Enter updated grades (comma-separated): ").split(',')))
                    student_manager.update_record(name, age, grades)

                elif choice == "3":
                    name = input("Enter the student name to retrieve: ")
                    student_manager.retrieve_record(name)

                elif choice == "4":
                    student_manager.show_all_records()

                elif choice == "5":
                    break

                else:
                    print("Invalid choice! Please select between 1-5.")

        elif main_choice == "2":
            print("\n=== Shopping Cart Tracker ===")
            while True:
                print("\nOptions:")
                print("1. Add a new user")
                print("2. Add Item to Cart")
                print("3. Remove Item from Cart")
                print("4. Show Items in Cart")
                print("5. Back to Main Menu")
                choice = input("Enter your choice (1-5): ")

                if choice == "1":
                     # Adding item to cart
                    name = input("Enter customer name: ")
                    shopping_cart.add_user(name)

                elif choice == "2":
                     # Adding item to cart
                    name = input("Enter customer name: ")
                    item = input("Enter item to add to cart: ")
                    shopping_cart.add_item(name, item)

                elif choice == "3":
                    # Removing item from cart
                    name = input("Enter customer name: ")
                    item = input("Enter item to remove from cart: ")
                    shopping_cart.remove_item(name, item)

                elif choice == "4":
                    # Showing all carts
                    shopping_cart.show_items()

                elif choice == "5":
                    break

                else:
                    print("Invalid choice! Please select between 1-4.")

        elif main_choice == "3":
            
            print("\n=== Configuration Viewer ===")
            while True:
                print("\nOptions:")
                print("1. View Configuration")
                print("2. Add Configuration")
                print("3. Retrieve Configuration")
                print("4. Exit")
                choice = input("Enter your choice (1-4): ")
                if choice == "1":
                    config_viewer.view_Configuration()
                elif choice == "2":
                    key = input("Enter the key for the new configuration: ")
                    config_viewer.add_Configuration(key)
                elif choice == "3":
                    key = input("Enter the key to retrieve: ")
                    value = config_viewer.retrieve_Configuration(key)
                elif choice == "4":
                    print("Exiting Configuration Viewer. Goodbye!")
                    break

        elif main_choice == "4":
            print("Exiting Program. Goodbye!")
            break

        else:
            print("Invalid choice! Please select between 1-4.")