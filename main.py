students = []

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    
    student = {
        "name": name,
        "roll": roll
    }
    
    students.append(student)
    print("Student added successfully")

def view_students():
    if not students:
        print("No students found")
    else:
        for student in students:
            print(student)

def menu():
    while True:
        print("\n1. Add Student")
        print("2. View Students")
        print("3. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            break
        else:
            print("Invalid choice")

menu()
