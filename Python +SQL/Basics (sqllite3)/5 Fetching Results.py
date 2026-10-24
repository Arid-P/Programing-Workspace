# ------------------------------------------------------------
# LESSON 5 NOTES: Fetching Results with fetchone and fetchall
# ------------------------------------------------------------

import sqlite3 as sq

db = sq.connect(r"Python +SQL\Practice databases\school.db")
cursor = db.cursor()

# ---------------------------
# fetchall() example
# ---------------------------
cursor.execute("SELECT * FROM students")
all_students = cursor.fetchall()  # returns list of tuples
print(all_students)

# ---------------------------
# fetchone() example
# ---------------------------
cursor.execute("SELECT * FROM students WHERE grade=?", ('9-A',))
student = cursor.fetchone()  # returns a single tuple
print(student)

# ---------------------------
# fetchone() multiple calls
# ---------------------------
cursor.execute("SELECT * FROM students WHERE grade=?", ('9-A',))
print(cursor.fetchone())  # first row
print(cursor.fetchone())  # second row (if exists)

# ---------------------------
# Iterating over cursor (memory-efficient)
# ---------------------------
cursor.execute("SELECT * FROM classes")
for row in cursor:
    print(row)

# Close connection
db.close()
