# Simple Student Manager Program

students = []

def add_student():
    name = input("Enter student name: ")
    students.append(name)
    print("Student added successfully!\n")

def view_students():
    if len(students) == 0:
        print("No students found.\n")
    else:
        print("Student List:")
        for s in students:
            print("-", s)
        print()

def menu():
    while True:
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit")
        
        choice = input("Enter choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            print("Exiting program...")
            break
        else:
            print("Invalid choice!\n")

menu()