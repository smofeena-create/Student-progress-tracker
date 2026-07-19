import sqlite3
from datetime import date
conn = sqlite3.connect('student_progress.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS student(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS progress(
               progress_id INTEGER PRIMARY KEY AUTOINCREMENT,
               id INTEGER NOT NULL,
               date TEXT NOT NULL,
               study_hours INTEGER,
               dsa_problems_solved INTEGER,
               FOREIGN KEY(ID) REFERENCES student(id))''')
conn.commit()
conn.close()
def add_student(name):
    conn = sqlite3.connect('student_progress.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO student (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()
def add_progress(id,date, study_hours, dsa_problems_solved):
    conn = sqlite3.connect('student_progress.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO progress (id, date, study_hours, dsa_problems_solved) VALUES (?, ?, ?, ?)", (id, date, study_hours, dsa_problems_solved))
    conn.commit()
    conn.close()
def view_progress(id):
    conn = sqlite3.connect('student_progress.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM progress WHERE id=?", (id,))
    rows = cursor.fetchall()
    conn.close()
    return rows
def total_study_hours(id):
    conn = sqlite3.connect('student_progress.db')
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(study_hours) FROM progress WHERE id=?", (id,))
    total_hours = cursor.fetchone()[0]
    conn.close()
    return total_hours
def total_dsa_problems_solved(id):
    conn = sqlite3.connect('student_progress.db')
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(dsa_problems_solved) FROM progress WHERE id=?", (id,))
    total_problems = cursor.fetchone()[0]
    conn.close()
    return total_problems
def view_students():
    conn = sqlite3.connect('student_progress.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM student")
    rows = cursor.fetchall()
    conn.close()
    return rows
while True:
    try:
        choice=input("Enter your choice:\n1. Add Student\n2. Add Progress\n3. View Progress\n4. Total Study Hours\n5. Total DSA Problems Solved\n6. View Students\n")
        if choice == "1":
            name = input("Enter student name: ")
            add_student(name)
            print("Student added successfully.")
        elif choice == "2":
            id = int(input("Enter student ID: "))
            date = str(date.today())
            study_hours = int(input("Enter study hours: "))
            dsa_problems_solved = int(input("Enter DSA problems solved: "))
            add_progress(id, date, study_hours, dsa_problems_solved)
            print("Progress added successfully.")
        elif choice == "3":
            id = int(input("Enter student ID: "))
            rows = view_progress(id)
            for row in rows:
                print(row)
            print("Progress displayed successfully.")
        elif choice == "4":
            id = int(input("Enter student ID: "))
            total_hours = total_study_hours(id)
            print(f"Total study hours for student {id}: {total_hours}")
            print("Total study hours displayed successfully.")
        elif choice == "5":
            id = int(input("Enter student ID: "))
            total_problems = total_dsa_problems_solved(id)
            print(f"Total DSA problems solved for student {id}: {total_problems}")
            print("Total DSA problems solved displayed successfully.")
        elif choice=="6":
            students = view_students()
            for student in students:
                print(student)
            print("Students displayed successfully.")
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
    except Exception as e:
        print(f"An error occurred: {e}")
  