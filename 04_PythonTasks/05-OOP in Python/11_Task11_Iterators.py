"""
Author: Basel Amr Barakat
Email: baselamr52@gmail.com
Date: 2024-12-16
Task Name : Use Iterators for Efficient Data Handling
Task Number : 11
Part : OOP in Python
Module : Python Programming Language for AI / ML
Submit_Number : 1

Description:
This task teaches students how to create and use iterators for efficient data handling, reducing memory consumption 
by processing large datasets one element at a time. Students will implement custom iterators and use them in loops.

Requirement 1:
Description: Create an iterator class LargeDatasetIterator that accepts a list of numbers. 
Implement the __iter__() and __next__() methods to allow iteration through the dataset one item at a time.

Requirement 2:
Description: Use the LargeDatasetIterator class to iterate over a list of numbers and print each number. 
Ensure the __next__() method raises StopIteration when all numbers have been iterated.

Requirement 3:
Description: Demonstrate the use of the LargeDatasetIterator by using a for loop to print all the elements from a large list of numbers (e.g., 1 to 1000).
 Ensure the iterator works efficiently without loading the entire list into memory.
"""
import sys
# Requirment 1 :
class LargeDatasetIterator:
    """
    It is a custome iterator class that is used to handle large datasets efficiently 

    Attributes:
    data (list) : The list of the numbers to iterate though
    """
    def __init__(self, data:list = []):
         """
         Initialize the LargeDatasetIterator with a dataset given
         Args:
            data (list) : The list of the numbers to iterate though
         """
         self.data = data
         self.index = 0
    
    def __iter__(self):
        """
        Returns the iterator object itself.

        Returns:
        LargeDatasetIterator: The iterator instance.
        """
        return self
    
    def __next__(self):
        """
        Return the next item in the dataset

        Raises Error:
            StopIteration : when all items in the dataset have been iterated
        """
        # If there are still items left to iterate
        if(self.index < len(self.data)):
            # Get the Current item
            result = self.data[self.index]
            # Move to the next index
            self.index+=1
            # Return the current element
            return result
        else:
            raise StopIteration
             

def main():
    print("Welcome to the I Use Iterators for Efficient Data Handling Task!")
    # Requirment 2:
    print("Making Requirment 2 on small dataset ")
    small_dataset = [1,2,4,1,2]
    iterator = LargeDatasetIterator(small_dataset)
    for data in small_dataset:
        print(data)
    # Requirement 3: Demonstrating the iterator with a large dataset.
    large_dataset = list(range(1000))
    iterator =  LargeDatasetIterator(large_dataset)
    # Measure memory usage for the list (all elements are in memory)
    list_memory = sys.getsizeof(large_dataset)
    # Measure memory usage for the iterator (only the current element and index are in memory)
    iterator_memory = sys.getsizeof(iterator)

    # Measure memory usage for the iterator (only the current element and index are in memory)
    # Output memory usage comparison
    print(f"Memory used by the list: {list_memory} bytes")
    print(f"Memory used by the iterator: {iterator_memory} bytes\n")
    print("Using LargeDataSetIteratorwith a large dataset from 0 to 100")
    iterator_memory = sys.getsizeof(iterator)
    for data in iterator:
        print(data, end=" ")
if __name__ == "__main__":
    main()
