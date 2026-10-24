questions = """
1. INSERT
Add 3 students
Add 2 classes
Add 2 teachers

2. SELECT
Show all teachers ordered by name
Show all classes where room_number > 200
Show all students with grade “9-A”

3. UPDATE
Change one student’s grade
Change a teacher’s subject

4. DELETE
Delete one class
Delete one student
"""

import sqlite3 as sq

db = sq.connect(r'Python +SQL\Practice databases\school.db')

cursor = db.cursor()

#1. INSERT
students = [
    (384, 45, '10-B'),
    (498, 29, '9-A'),
    (397, 48, '10-D')
]

classes = [
    (64, '10-A', 31),
    (69, '10-C', 33),
    (183, '1-B', 346),
    (134, '3-C', 295)
]

teachers = [
    (64, 'Rahul Verma', "Gunda Gardi", 3197429724),
    (69, 'Mohit Sirvastav', "Physics",3332179487)
]

cursor.executemany("INSERT INTO students (id, number, grade) VALUES (?, ?, ?)", students)
cursor.executemany("INSERT INTO classes (id, class_name, room_number) VALUES (?, ?, ?)", classes)
cursor.executemany("INSERT INTO teachers (id, name, subject, phone) VALUES (?, ?, ?, ?)", teachers)
db.commit()

#2. SELECT
print(cursor.execute("SELECT * FROM teachers ORDER BY name").fetchall())
print(cursor.execute("SELECT * FROM classes WHERE room_number > ?", (200,)).fetchall())
print(cursor.execute("SELECT * FROM students WHERE grade=?", ('9-A',)).fetchall())
db.commit()

#3. UPDATE
cursor.execute("UPDATE students SET grade=? WHERE id=?", ('11-C', 397))
cursor.execute("UPDATE teachers SET subject=? WHERE name=?", ('Physical Education', 'Rahul Verma'))
db.commit()

#4. DELETE
cursor.execute("DELETE FROM classes WHERE id=?", (183,))
cursor.execute("DELETE FROM students WHERE id=?", (397,))
db.commit()

db.close()