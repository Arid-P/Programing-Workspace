# ----------------------------------------------------
# LESSON 8 NOTES: Using Functions with SQLite (Python)
# ----------------------------------------------------
# Why use functions?
# - Avoid repeating connection code
# - Organise logic cleanly
# - Reuse functions anywhere
# - Cleaner main program

import sqlite3

DB_PATH = "Python +SQL\\Practice databases\\example.db"

# Function: Create and return connection + cursor
def get_connection():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    return conn, cursor

# Function: Create table
def create_students_table():
    conn, cursor = get_connection()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            grade TEXT
        )
    """)
    conn.commit()
    conn.close()

# Function: Insert student
def add_student(name, age, grade):
    conn, cursor = get_connection()
    cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", (name, age, grade))
    conn.commit()
    conn.close()

# Function: Fetch all students
def get_all_students():
    conn, cursor = get_connection()
    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()
    conn.close()
    return data

# Function: Fetch by age
def get_students_by_age(age):
    conn, cursor = get_connection()
    cursor.execute("SELECT * FROM students WHERE age = ?", (age,))
    data = cursor.fetchall()
    conn.close()
    return data

# Function: Update grade
def update_grade(student_id, new_grade):
    conn, cursor = get_connection()
    cursor.execute("UPDATE students SET grade = ? WHERE id = ?", (new_grade, student_id))
    conn.commit()
    conn.close()

# Function: Delete student
def remove_student(student_id):
    conn, cursor = get_connection()
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    conn.close()


def main () -> None :
    """It is the starting function. From it you can understand a basic flow of the whole program"""
    create_students_table()

    add_student(546, 4636434658, "10-A")
    add_student(353, 9898709708, "9-B")

    print(get_all_students())
    print(get_students_by_age("9B"))

    update_grade(1, "10A+")
    remove_student(353)
    remove_student(546)


if __name__ == '__main__' :
    main() 