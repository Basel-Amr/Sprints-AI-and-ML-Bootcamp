"""
Author: Basel Amr Barakat
Email: baselamr52@gmail.com
Date: 2024-12-16
Task Name : Implement and Use a Generator Function
Task Number : 10
Part : OOP in Python
Module : Python Programming Language for AI / ML
Submit_Number : 1

Description:
This task introduces students to Python generator functions and their benefits. 
Students will implement a generator to handle large datasets efficiently and explore the difference between 
generator functions and traditional approaches.

Requirement 1:
Description: Create a generator function fibonacci(n) that yields Fibonacci numbers. 
The function should accept an integer n to specify how many Fibonacci numbers to generate..

Requirement 2:
Description: Use the fibonacci() generator function to generate and print the first 10 Fibonacci numbers using a for loop.

Requirement 3:
Description: Compare the generator function with a traditional list-based approach for generating the Fibonacci sequence. 
Verify that the generator function uses less memory by testing with a large value of n.
"""
# Import sys library to compare size, time library to compare time 
import sys
import time
# Requirment One: 
def fibonacci_generator(n:int):
    """
    This function is used to yield the first n Fabonacci numbers.

    Args:
        n (int) : The number of Fabonacci numbers to generate
    """
    # Initialize the first two Fabonacci numbers in the series
    cur_num , next_num = 0, 1
    for _ in range(n):
        yield cur_num   # Yield the current Fibonacci number
        cur_num, next_num = next_num, cur_num + next_num  # Update the next Fibonacci numbers in the series




# Requirement 2: Compare the generator with a list-based approach
def fibonacci_List(n:int):
    """
    Generate the first n Fibonacci numbers using a list.

    Args:
        n (int): The number of Fibonacci numbers to generate.

    Returns:
        list: A list of Fibonacci numbers.
    """
    fibonacci_list = []
    cur_number, next_number = 0, 1
    for _ in range(n):
        fibonacci_list.append(cur_number)
        cur_number, next_number = next_number, cur_number + next_number
    return fibonacci_list
     

        

def main():
    print("Welcome to the Implement and Use a Generator Function Task!")
    # Requirement 3: 
    # Define the number of Fibonacci numbers to generate.
    print("First 10 Fibonacci numbers using the generator:")
    for number in fibonacci_generator(10):
        print(number, end=" ")
    print("\n")  # Add a newline for better readability

    n_large = 150000  # Number of Fibonacci numbers to test for performance and memory usage.
    # Measure memory usage of the generator
    fib_gen = fibonacci_generator(n_large)  # Create a generator object
    gen_memory = sys.getsizeof(fib_gen)

    # Measure memory usage of the list-based approach
    fib_list_obj = fibonacci_List(n_large)
    list_memory = sys.getsizeof(fib_list_obj)

    # Output memory comparison
    print(f"Memory used by the generator for {n_large} Fibonacci numbers: {gen_memory} bytes")
    print(f"Memory used by the list for {n_large} Fibonacci numbers: {list_memory} bytes\n")

    # Measure time taken by the generator
    start_time_gen = time.time()
    for _ in fibonacci_generator(n_large):
        pass
    end_time_gen = time.time()

    # Measure time taken by the list-based approach
    start_time_list = time.time()
    fib_list_obj = fibonacci_List(n_large)  # Generate the list
    end_time_list = time.time()

    # Output time comparison
    print(f"Time taken by the generator: {end_time_gen - start_time_gen:.6f} seconds")
    print(f"Time taken by the list-based approach: {end_time_list - start_time_list:.6f} seconds")

    print("##################Summary##################")
    print(f"We Concluded that the generator methode use less memory compared to list-based methode {gen_memory} vs {list_memory} in bytes" )
    print(f"We Concluded that the generator methode use less time compared to list-based methode {end_time_gen - start_time_gen:.6f} vs {end_time_list - start_time_list:.6f} in bytes" )
if __name__ == "__main__":
    main()
 