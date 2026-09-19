# ------------------------------------------------------------
# LESSON 4 NOTES: Parameterized Queries & SQL Injection Prevention
# ------------------------------------------------------------

import sqlite3 as sq

db = sq.connect(r"Python +SQL\Practice databases\school.db")
cursor = db.cursor()

# ---------------------------
# Unsafe example (do NOT use)
# ---------------------------
user_input = "9-A' OR 1=1 --"
query = f"SELECT * FROM students WHERE grade = '{user_input}'"
# cursor.execute(query)  # unsafe, vulnerable to SQL injection

# ---------------------------
# Safe example using placeholder
# ---------------------------
cursor.execute("SELECT * FROM students WHERE grade = ?", (user_input,))
print(cursor.fetchall())

# ---------------------------
# Multiple parameters
# ---------------------------
cursor.execute(
    "SELECT * FROM students WHERE grade = ? AND number = ?",
    ("9-A", 29)
)
print(cursor.fetchall())

# ---------------------------
# Multiple inserts safely
# ---------------------------
students = [
    (401, 50, "10-A"),
    (402, 51, "10-B")
]
cursor.executemany(
    "INSERT INTO students (id, number, grade) VALUES (?, ?, ?)",
    students
)
db.commit()

# Close connection
db.close()
