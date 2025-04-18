"""
Author: Basel Amr Barakat
Email: baselamr52@gmail.com
Date: 2024-12-18
Task Name : Utilize Specialized Collections
Task Number : 14
Part : Exception Handling
Module : Python Programming Language for AI / ML
Submit_Number : 1

Description:
This task introduces students to the specialized collections in Python’s collections module.
They will apply collections like Counter, namedtuple, deque, OrderedDict, and defaultdict to solve real-world problems.

Requirement 1:
Description: Use the Counter class to count the frequency of words in a given text file.

Requirement 2:
Description: Create a namedtuple to store information about a book (e.g., title, author, year, ISBN).


Requirement 3:
Description: Use deque to implement a queue where you enqueue and dequeue elements efficiently.
"""
from collections import Counter, deque, namedtuple
from typing import List
# Requirement 1 : Use the Counter class to count the frequency of words in a given text file.
class WordCounter():
    """
    This Class is used to count the frequency of words in a given text file
    by using Python's Counter class
    
    Methods:
        count_word_frequency(file_path:str) -> Counter: Counts the frequency of each word in the give text file
        display_top_n_words(n:int) -> None : Displays the top n words in the give file
    """
    # Constructor
    def __init__(self):
        self.word_counter = Counter()
    
    # Count word frequency
    def count_word_frequency(self, file_path:str)->Counter:
        """
        This functions takes the file path as an element and count the frequency of words
        Args:
            file_path (str): The path to the text file to analyze.
            Counter: Counts the frequency of each word in the give text file
        """
        try:
            with open(file_path, 'r') as file:
                text = file.read().lower().split()  # Convert to lowercase and split by spaces
                self.word_counter = Counter(text)
            print("Word frequency counting completed.")
            print(self.word_counter)
            return self.word_counter
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
        
    def display_top_n_words(self, n: int) -> None:
        """
        Displays the top N most frequent words.

        Args:
            n (int): The number of top words to display.
        """
        print(f"\nTop {n} most common words:")
        for word, count in self.word_counter.most_common(n):
            print(f"{word}: {count}")

# Requirement 2: Create a namedtuple to store information about a book (e.g., title, author, year, ISBN).
Book = namedtuple('Book', ['title', 'author', 'year', 'isbn', 'num_of_pages'])

class BookManager():
    """
    This class is used to manage info of books using namedtuple for storing book information.
    Attributes:
        books (dict): Contains the information of the book (e.g., title, author, year, ISBN, number_of_pages).
    Methods:
        add_book(title:str, author: str, year: int, ISBN:str, num_of_pages:int) -> None : Adds a new book to the collection.
        display_info() -> None : Displays all books in the collection.
    """
    # Constructor
    def __init__(self):
        self.books = {}

    # Add a book using namedtuple
    def add_book(self, title:str, author: str, year: int, ISBN:str, num_of_pages:int)->None:
        """
        Adds a book record to the collection.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            year (int): The year the book was published.
            isbn (str): The ISBN of the book.
            num_of_pages (int) : The number of pages of the book
        """
        # Create a Book namedtuple and add it to the dictionary with title as the key
        book = Book(title, author, year, ISBN, num_of_pages)
        self.books[title] = book
        print(f"Book '{title}' added successfully.")

    # Display information of all books
    def display_info(self)->None:
        """
        Displays the details of all books in the collection.
        """
        if self.books:
            print("\nAll Books in the Collection:")
            print("-" * 40)
            for idx, (title, book) in enumerate(self.books.items(), start=1):
                print(f"Book {idx}:")
                print(f"  Title       : {book.title}")
                print(f"  Author      : {book.author}")
                print(f"  Year        : {book.year}")
                print(f"  ISBN        : {book.isbn}")
                print(f"  Pages       : {book.num_of_pages}")
                print("-" * 40)
        else:
            print("No books in the collection yet.")
        

# Requirement 3 : Use deque to implement a queue where you enqueue and dequeue elements efficiently.
class QueueUsingDeque:
    """
    This class demonstrates the use of deque for implementing a queue.
    Attributes:
        deque()
    Methods:
        enqueue(item) -> None: Adds an item to the queue.
        dequeue() -> str: Removes and returns the item at the front of the queue.
        display_queue() -> None: Displays the current state of the queue.
        append(item) -> None: Adds an item to the end of the queue (same as enqueue).
        popleft() -> str: Removes and returns the item at the front of the queue (same as dequeue).
    """
    # Constructor
    def __init__(self):
        self.queue = deque()

    # Append a new element
    def enqueue(self, item: str) -> None:
        """
        Adds an item to the queue.

        Args:
            item (str): The item to add to the queue.
        """
        self.queue.append(item)
        print(f"Enqueued: {item}")

    # Popleft()
    def dequeue(self) -> str:
        """
        Removes and returns the item at the front of the queue.

        Returns:
            str: The item that was dequeued.
        """
        if self.queue:
            dequeued_item = self.queue.popleft()
            print(f"Dequeued: {dequeued_item}")
            return dequeued_item
        else:
            print("Queue is empty.")
            return None
        

    def display_queue(self) -> None:
        """
        Displays the current state of the queue.
        """
        print(f"Current Queue: {list(self.queue)}")

    


def main():
    word_counter = WordCounter()

    # Word frequency counting
    file_path = input("Enter the path to a text file for word counting: ")
    word_counter.count_word_frequency(file_path)
    word_counter.display_top_n_words(int(input("How many top words to display? ")))

    book_manager = BookManager()

    while True:
        print("\nBook Manager Menu:")
        print("1. Add a new book")
        print("2. Display all books")
        print("3. Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter the book title: ")
            author = input("Enter the author's name: ")
            year = int(input("Enter the publication year: "))
            isbn = input("Enter the ISBN: ")
            number_of_pages = int(input("Enter The Number of pages: "))
            book_manager.add_book(title, author, year, isbn,number_of_pages)
        elif choice == "2":
            book_manager.display_info()
        elif choice == "3":
            print("Exiting Book Manager.")
            break
        else:
            print("Invalid choice, please try again.")

    # Queue using deque
    queue = QueueUsingDeque()
    
    while True:
        print("\nQueue Menu:")
        print("1. Enqueue an item")
        print("2. Dequeue an item")
        print("3. Display the queue")
        print("4. Exit")
        
        queue_choice = input("Choose an option: ")

        if queue_choice == "1":
            item = input("Enter item to enqueue: ")
            queue.enqueue(item)
        elif queue_choice == "2":
            queue.dequeue()
        elif queue_choice == "3":
            queue.display_queue()
        elif queue_choice == "4":
            print("Exiting Queue operations.")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()