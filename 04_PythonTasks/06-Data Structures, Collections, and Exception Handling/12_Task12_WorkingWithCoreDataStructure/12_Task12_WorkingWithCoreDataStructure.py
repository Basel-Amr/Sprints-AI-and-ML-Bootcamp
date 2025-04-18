"""
Author: Basel Amr Barakat
Email: baselamr52@gmail.com
Date: 2024-12-18
Task Name : Working with Core Data Structures
Task Number : 12
Part : Data Structures
Module : Python Programming Language for AI / ML
Submit_Number : 1

Description:
This task focuses on implementing and manipulating Python's core data structures: lists, tuples, sets, and dictionaries.
Students will practice adding, accessing, and modifying elements within these structures.

Requirement 1:
Title: Implement and Manipulate a List
Description: Implement a Python program that creates a list of integers. Add new elements, remove an element, and access specific elements using indexing.
Required Deliverable: Python Code File: Deliver a Python script showing the list creation, modification (add, remove), and element access via index.

Requirement 2:
Title: Work with Tuples and Sets
Description: Implement a tuple of strings and a set of integers. Demonstrate tuple access and set operations like adding elements and performing union/intersection.


Requirement 3:
Title: Implement and Manipulate a Dictionary
Description: Implement a dictionary where the keys are strings (e.g., name, age, city) and the values are corresponding data. Add, modify, and access key-value pairs.
"""

# Requirment One : Implement and Manipulate a List
def manipulate_List()->None:
    """
    This functionis used to manipulate list creation, element addition, removing an element and access by index
    """
    # Create a list of integers
    print("Hello in list manipulation")
    my_list = [int(x) for x in input("Enter The list elements separated by spaces: ").split()]
    print(f"The list is:  {my_list}")

    # Add a new element
    new_number = int(input("Enter a number to add to the list : "))
    my_list.append(new_number)
    print(f"The number {new_number} is succefully added to the list")
    print(f"List after adding {new_number}: {my_list}")

    # Removing an element
    try:
        element_to_remove = int(input("Please Enter a number to remove: "))
        my_list.remove(element_to_remove)
        print(f"The {element_to_remove} is succefully removed from the list")
        print(f"List after removing {element_to_remove}: {my_list}")
    except ValueError:
        print("The number is not in the list!")
    
    # Access a specific element
    try:
        index = int(input("Enter the index of the element you want to access: "))
        print(f"Element at index {index}: {my_list[index]}")
    except IndexError:
        print("Invalid index!")

# Requirement 2 : Work with Tuples and Sets
def manipulate_TupleandSet()->None:
    """
    This function Implement a tuple of strings and a set of integers.
    Demonstrate tuple access and set operations like adding elements and performing union/intersection.
    """
    print("Hello in tuble and set manipulation")
    # Tuple operations
    my_tuple = tuple(input("Enter tuple elements separated by space: ").split())
    print(f"Your tuple: {my_tuple}")

    # Access a Tuple
    try:
        index = int(input("Enter the index of the element you want to access in the tuple: "))
        print(f"Element at index {index}: {my_tuple[index]}")
    except IndexError:
        print("Invalid index!")        

    # Set operations
    my_set = set(map(int, input("Enter initial set elements separated by space: ").split()))
    print(f"Your set: {my_set}")

    # Adding an element to the set
    new_element = int(input("Enter a number to add to the set: "))
    my_set.add(new_element)
    print(f"Set after adding {new_element}: {my_set}")

    # Performing union and intersection
    another_set = set(map(int, input("Enter another set of integers separated by space: ").split()))
    print(f"Another set: {another_set}")
    print(f"Union of sets: {my_set.union(another_set)}")
    print(f"Intersection of sets: {my_set.intersection(another_set)}")

# Requirement 3: Implement and Manipulate a Dictionary
def manipulate_Dictionary()->None:
    """
    This function demonstrates dictionary creation, adding/modifying key-value pairs, 
    and accessing values by key.
    """
    print("Hello in Dictionary manipulation")

    my_dict = {}
    print("Let's create a dictionary!")
    while True:
        key = input("Enter a key (or type 'stop' to finish): ")
        if key.lower() == 'stop':
            break
        value = input(f"Enter the value for key '{key}': ")
        my_dict[key] = value
    print(f"Your dictionary: {my_dict}")

    # Adding or modifying a key-value pair
    key_to_modify = input("Enter a key to add/modify: ")
    value_to_modify = input(f"Enter the value for key '{key_to_modify}': ")
    my_dict[key_to_modify] = value_to_modify
    print(f"Dictionary after modification: {my_dict}")

    # Accessing a value by key
    key_to_access = input("Enter a key to access its value: ")
    try:
        print(f"Value for key '{key_to_access}': {my_dict[key_to_access]}")
    except:
        print("Key not found in the dictionary!")

def main():
    print("Welcome to Working with CoreDataStructure Task")
    while True:
        print("\nChoose an operation to perform:")
        print("1. List Operations")
        print("2. Tuple and Set Operations")
        print("3. Dictionary Operations")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            manipulate_List()
        elif choice == '2':
            manipulate_TupleandSet()
        elif choice == '3':
            manipulate_Dictionary()
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
        
