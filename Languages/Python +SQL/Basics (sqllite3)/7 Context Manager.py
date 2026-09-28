# --------------------------------------------
# LESSON 7 NOTES: Using Context Managers in SQLite
# --------------------------------------------
# Why use context managers?
# - Ensures the database connection closes automatically
# - Prevents database locking issues
# - Auto-commit on success, auto-rollback on error
# - Cleaner, safer, shorter code

# Basic pattern:
# with sqlite3.connect("example.db") as conn:
#     cursor = conn.cursor()
#     cursor.execute("YOUR SQL HERE")

import sqlite3

# Example 1: Selecting data using context manager
with sqlite3.connect("Python +SQL\\Practice databases\\example.db") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()

print("All students:", data)

# Example 2: Inserting data safely
with sqlite3.connect("Python +SQL\\Basics (sqllite3)\\Practice databases\\example.db") as conn:
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO students (name, age, grade)
        VALUES ('Ari', 16, '10A')
    """)

# Example 3: Nested context manager (advanced)
# Saving backup of table into a text file
with sqlite3.connect("Python +SQL\\Basics (sqllite3)\\Practice databases\\example.db") as conn:
    cursor = conn.cursor()
    with open("students_backup.txt", "w") as file:
        for row in cursor.execute("SELECT * FROM students"):
            file.write(str(row) + "\n")
