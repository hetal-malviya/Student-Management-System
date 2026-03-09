from database import get_connection

def add_student():
    conn = get_connection()
    cursor = conn.cursor()

    name = input("Enter student name: ")
    roll_number = input("Enter roll number: ")
    course = input("Enter course: ")
    email = input("Enter email: ")

    query = "INSERT INTO students (name, roll_number, course, email) VALUES (%s, %s, %s, %s)"
    values = (name, roll_number, course, email)

    try:
        cursor.execute(query, values)
        conn.commit()
        print("Student added successfully.")
    except Exception as e:
        print("Error:", e)

    cursor.close()
    conn.close()

def view_students():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    if not students:
        print("No students found.")
    else:
        for student in students:
            print(student)

    cursor.close()
    conn.close()

def search_student():
    conn = get_connection()
    cursor = conn.cursor()

    roll_number = input("Enter roll number to search: ")
    query = "SELECT * FROM students WHERE roll_number = %s"
    cursor.execute(query, (roll_number,))
    student = cursor.fetchone()

    if student:
        print("Student found:", student)
    else:
        print("Student not found.")

    cursor.close()
    conn.close()

def update_student():
    conn = get_connection()
    cursor = conn.cursor()

    roll_number = input("Enter roll number of student to update: ")
    new_email = input("Enter new email: ")

    query = "UPDATE students SET email = %s WHERE roll_number = %s"
    cursor.execute(query, (new_email, roll_number))
    conn.commit()

    if cursor.rowcount > 0:
        print("Student updated successfully.")
    else:
        print("Student not found.")

    cursor.close()
    conn.close()

def delete_student():
    conn = get_connection()
    cursor = conn.cursor()

    roll_number = input("Enter roll number of student to delete: ")
    query = "DELETE FROM students WHERE roll_number = %s"
    cursor.execute(query, (roll_number,))
    conn.commit()

    if cursor.rowcount > 0:
        print("Student deleted successfully.")
    else:
        print("Student not found.")

    cursor.close()
    conn.close()

def menu():
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

menu()
