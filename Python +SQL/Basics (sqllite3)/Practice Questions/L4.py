import sqlite3 as sq

db = sq.connect(r'Python +SQL\Practice databases\school.db')
cursor = db.cursor()
print('\n')

question = "Using students table: Take a grade input from the user and fetch all students with that grade."

grade = input("Enter a Grade (like 9 A):").replace(" ", "-")
print(cursor.execute("SELECT * FROM students WHERE grade=?", (grade,)).fetchall())

db.close()