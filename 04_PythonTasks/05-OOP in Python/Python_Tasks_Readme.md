# Python Programming Tasks

## Author
**Name:** Basel Amr Barakat  
**Email:** baselamr52@gmail.com  
**Date:** 2024-12-16  

## Overview
This repository contains Python tasks focused on object-oriented programming (OOP) concepts, including classes, inheritance, polymorphism, and generator functions.

---

## Task 8: Create and Implement a Class with Constructor and Methods

### Description
This task helps students practice defining and implementing Python classes, using constructors to initialize objects, and creating methods that define behaviors of those objects. The task consists of three requirements:

### Requirements
1. **Define a Class with Attributes and Constructor**  
   - Create a class `Book` with attributes `title`, `author`, and `pages`.  
   - Implement the `__init__` constructor method to initialize these attributes.
   - **Deliverable:** Python code file containing the `Book` class, `__init__` constructor, and `describe()` method.

2. **Create a Method to Describe the Book**  
   - Implement a method `describe()` in the `Book` class that outputs a string describing the book.  
   - **Deliverable:** Screenshot showing an instance of the `Book` class being created and the output of `describe()` method.

3. **Instantiate and Test the Class**  
   - Create an instance of the `Book` class, initialize it with values for the attributes, and call the `describe()` method.  
   - **Deliverable:** Console output showing the description of the created book instance.

---

## Task 9: Apply Inheritance and Polymorphism

### Description
This task focuses on reinforcing concepts of inheritance and polymorphism in object-oriented programming. Students will practice creating parent and child classes, overriding methods, and demonstrating polymorphic behavior.

### Requirements
1. **Create a Parent Class `Car`**  
   - Implement a class `Car` with attributes `make`, `model`, and `year`.  
   - Define a method `start()` that prints a message indicating the car is starting.

2. **Create a Subclass `ElectricCar`**  
   - Implement a subclass `ElectricCar` that inherits from `Car`.  
   - Override the `start()` method to print a message indicating the electric car is starting silently.

3. **Demonstrate Polymorphism**  
   - Create instances of both `Car` and `ElectricCar`.  
   - Call the `start()` method on both instances to demonstrate polymorphism.

---

## Task 10: Implement and Use a Generator Function

### Description
This task introduces students to Python generator functions and their benefits. Students will implement a generator to handle large datasets efficiently and explore the difference between generator functions and traditional approaches.

### Requirements
1. **Create a Fibonacci Generator Function**  
   - Implement a generator function `fibonacci(n)` that yields Fibonacci numbers.  
   - The function should accept an integer `n` to specify how many Fibonacci numbers to generate.

2. **Use the Generator Function**  
   - Use the `fibonacci()` generator function to generate and print the first 10 Fibonacci numbers using a for loop.

3. **Compare with a Traditional List-Based Approach**  
   - Compare the generator function with a traditional list-based approach for generating the Fibonacci sequence.  
   - Verify that the generator function uses less memory by testing with a large value of `n`.

---

## Execution
Each task contains a `main()` function that demonstrates the implementation. To run the tasks, execute the respective Python scripts.

```bash
python task8.py  # For the Book class task
python task9.py  # For the Car and ElectricCar task
python task10.py # For the Fibonacci generator task
```

## Contact
For any questions or suggestions, feel free to reach out via email at **baselamr52@gmail.com**.
