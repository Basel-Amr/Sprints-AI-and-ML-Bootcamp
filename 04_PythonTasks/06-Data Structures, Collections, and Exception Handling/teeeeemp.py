import os

# Student record class to structure student data
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

    def to_file_format(self):
        return f"{self.name},{self.age},{self.grade}"

    def from_file_format(data):
        name, age, grade = data.split(',')
        return Student(name.strip(), int(age.strip()), grade.strip())

# File handling functions
def save_student_to_file(student, filename="students.txt"):
    with open(filename, "a") as file:
        file.write(student.to_file_format() + "\n")

def read_all_students_from_file(filename="students.txt"):
    if not os.path.exists("students.txt"):
        return []
    
    students = []
    with open("students.txt", "r") as file:
        for line in file.readlines():
            students.append(Student.from_file_format(line.strip()))
    return students

def search_student_by_name(name, filename="students.txt"):
    students = read_all_students_from_file(filename)
    found_students = [student for student in students if student.name.lower() == name.lower()]
    return found_students

# Program functions
def add_student():
    name = input("Enter student's name: ")
    age = input("Enter student's age: ")
    grade = input("Enter student's grade: ")

    # Validate input
    if not age.isdigit():
        print("Error: Age must be a number!")
        return
    elif (int(age) < 0 or int(age)>45):
        print("Invalid Age! Enter Age from 0 to 45")
        return
    student = Student(name, int(age), grade)
    save_student_to_file(student)
    print(f"Student {name} added successfully!")

def view_all_students():
    students = read_all_students_from_file()
    if students:
        for student in students:
            print(student)
    else:
        print("No student records found.")

def search_student():
    name = input("Enter student's name to search: ")
    students = search_student_by_name(name)
    if students:
        for student in students:
            print(student)
    else:
        print("No student found with that name.")
def delete_file(filename="students.txt"):
    """Deletes the file containing student records."""
    if os.path.exists(filename):
        os.remove(filename)
        print(f"{filename} has been deleted.")
    else:
        print(f"{filename} not found!")

def main():
    while True:
        print("\n--- Student Management System ---")
        print("1. Add a student record")
        print("2. View all records")
        print("3. Search a student by name")
        print("4. Delete all student records (Delete File)")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            view_all_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_file()  # Call delete file function
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
