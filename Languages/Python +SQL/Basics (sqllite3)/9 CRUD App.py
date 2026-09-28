# ----------------------------------------------------
# LESSON 9 NOTES: CRUD App with SQLite (Python)
# ----------------------------------------------------
# What is CRUD?
# C - Create (insert)
# R - Read (select)
# U - Update
# D - Delete
# We build functions for each and call them from main()

import sqlite3

DB_PATH = r"Python +SQL\Practice databases\crud_demo.db"

# Connection function
def get_connection():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    return conn, cursor

# Create table
def create_table():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER,
                grade TEXT
            )
        """)
        conn.commit()

# CREATE
def add_student(name, age, grade):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO students (name, age, grade) VALUES (?, ?, ?)",
            (name, age, grade)
        )
        conn.commit()

# READ (all students)
def get_all_students():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        return cursor.fetchall()

# READ (one student)
def get_student_by_id(student_id):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
        return cursor.fetchone()

# UPDATE
def update_grade(student_id, new_grade):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE students SET grade = ? WHERE id = ?",
            (new_grade, student_id)
        )
        conn.commit()

# DELETE
def delete_student(student_id):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
        conn.commit()

def main():
    create_table()

    # Insert sample records
    add_student("Aarav", 15, "9-A")
    add_student("Riya", 14, "8-B")

    print("All Students:", get_all_students())

    print("Student with ID 1:", get_student_by_id(1))

    update_grade(1, "10-A")
    print("After Update:", get_all_students())

    delete_student(2)
    print("After Delete:", get_all_students())

if __name__ == "__main__":
    main()
