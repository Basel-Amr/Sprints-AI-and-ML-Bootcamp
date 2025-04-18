"""
Author: Basel Amr Barakat
Email: baselamr52@gmail.com
Date: 2024-12-18
Task Name : Reading and Writing Files
Task Number : 16
Part :  File Handling
Module : Python Programming Language for AI / ML
Submit_Number : 1

Description:
This task focuses on file reading and writing operations.
Students will practice managing file paths, handling file exceptions, and performing basic file operations.

Requirement 1:
Title: Open and Read from a File
Description: Write a Python script that reads data from a text file and prints the contents to the console.
Handle possible FileNotFoundError exceptions.

Requirement 2:
Title:Write to a File
Description:Implement a Python script that writes a list of strings to a new text file. Handle file access permissions.

Requirement 3:
Title Use with for File Handling
Description: Use the with statement to read from one file, modify the content, and write the modified content to another file."
"""
import os
# Requirement 1: Open and Read from a File
def read_file(file_path:str)->None:
    """
    Reads data from a text file and prints its contents to the console.

    Args:
        file_path (str): Path to the file to be read.

    Raises:
        FileNotFoundError: If the specified file is not found.
    """
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print("\nContents of the file:")
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")

# Requirement 2: Write to a File
def write_to_file(file_path:str, data:list)->None:
    """
    Writes a list of strings to a text file.

    Args:
        file_path (str): Path to the file to write to.
        data (list): List of strings to write.

    Raises:
        IOError: If there is an issue with file access permissions.
    """
    try:
        with open(file_path, 'w') as file:
            file.writelines(f"{line}\n" for line in data)
            print(f"\nData successfully written to '{file_path}'.")
    except IOError:
        print(f"Error: Could not write to the file '{file_path}'. Check your file permissions.")


# Requirement 3: Use 'with' for File Handling
def read_modify_write(source_file, target_file, modifier):
    """
    Reads content from one file, modifies it, and writes it to another file.

    Args:
        source_file (str): Path to the source file.
        target_file (str): Path to the target file where modified content will be written.
        modifier (function): Function to apply modifications to the content.

    Raises:
        FileNotFoundError: If the source file does not exist.
    """
    try:
        with open(source_file, 'r') as src:
            content = src.readlines()
        
        modified_content = [modifier(line) for line in content]

        with open(target_file, 'w') as tgt:
            tgt.writelines(modified_content)
            print(f"\nModified content written to '{target_file}'.")

    except FileNotFoundError:
        print(f"Error: The source file '{source_file}' was not found.")

def list_files_in_folder(folder_path:str=os.getcwd()):
    """
    Lists all files in the specified folder.

    Args:
        folder_path (str): The path of the folder to list files from. Defaults to the current directory.

    Returns:
        None
    """
    try:
        print("\nFiles in folder:")
        files = os.listdir(folder_path)
        if files:
            for idx, file in enumerate(files, 1):
                print(f"{idx}. {file}")
        else:
            print("The folder is empty.")
    except FileNotFoundError:
        print(f"Error: The folder '{folder_path}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied for folder '{folder_path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
# Main Function
def main():
    print("\n=== File Reading and Writing Operations ===")

    while True:
        print("\nChoose an operation:")
        print("1. Read from a file")
        print("2. Write to a file")
        print("3. Read, modify, and write between files")
        print("4. List all files in a folder")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            file_path = input("Enter the path of the file to read: ")
            read_file(file_path)
        elif choice == '2':
            file_path = input("Enter the path of the file to write to: ")
            data = []
            print("Enter the data to write (type 'DONE' to finish):")
            while True:
                line = input()
                if line.upper() == 'DONE':
                    break
                data.append(line)
            write_to_file(file_path, data)
        elif choice == '3':
            source_file = input("Enter the path of the source file: ")
            target_file = input("Enter the path of the target file: ")
            print("All content will be converted to uppercase.")
            read_modify_write(source_file, target_file, str.upper)
        elif choice == "4":
            list_files_in_folder()
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
