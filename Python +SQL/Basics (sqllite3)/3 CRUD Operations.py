# ------------------------------------------------------------
# LESSON 3 NOTES: CRUD OPERATIONS (INSERT, SELECT, UPDATE, DELETE)
# ------------------------------------------------------------

import sqlite3 as sq

# Connect using full path
db = sq.connect("Python +SQL\\Practice databases\\school.db")
cursor = db.cursor()

# ------------------------------------------------------------
# INSERT OPERATIONS
# ------------------------------------------------------------
cursor.execute(
    "INSERT INTO students (id, name, grade) VALUES (?, ?, ?)",
    (301, "Rohan", "9-A")
)
db.commit()

students_data = [
    (302, "Anuj", "9-B"),
    (303, "Sia", "9-A")
]

cursor.executemany(
    "INSERT INTO students (id, name, grade) VALUES (?, ?, ?)",
    students_data
)
db.commit()

# ------------------------------------------------------------
# SELECT OPERATIONS
# ------------------------------------------------------------
cursor.execute("SELECT * FROM students")
print(cursor.fetchall())

cursor.execute("SELECT name, grade FROM students WHERE grade = ?", ("9-A",))
print(cursor.fetchall())

cursor.execute("SELECT * FROM students ORDER BY name ASC")
print(cursor.fetchall())

# ------------------------------------------------------------
# UPDATE OPERATIONS
# ------------------------------------------------------------
cursor.execute(
    "UPDATE students SET grade = ? WHERE id = ?",
    ("10-A", 301)
)
db.commit()

cursor.execute(
    "UPDATE students SET grade = ? WHERE grade = ?",
    ("10-B", "9-B")
)
db.commit()

# ------------------------------------------------------------
# DELETE OPERATIONS
# ------------------------------------------------------------
cursor.execute("DELETE FROM students WHERE id = ?", (303,))
db.commit()

cursor.execute("DELETE FROM students")
db.commit()

# Close connection
db.close()
