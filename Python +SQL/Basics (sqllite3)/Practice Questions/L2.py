"""
Create these tables:

classes (id, class_name, room_number)

marks (id, student_id, subject, score)

teachers (id, name, subject, phone) — phone must be UNIQUE

Then:

Use PRAGMA table_info() to display structure of all tables.

Drop the marks table and recreate it with an additional column max_score.
"""


import sqlite3 as sq

db = sq.connect("Python +SQL\Practice databases\school.db") #type: ignore

cursor = db.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS classes (
        id INTEGER PRIMARY KEY,
        class_name TEXT,
        room_number Integer
    );
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS marks (
        id INTEGER PRIMARY KEY,
        student_id INTEGER,
        subject TEXT,
        score INTEGER
    );
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS teachers (
        id INTEGER PRIMARY KEY,
        name TEXT,
        subject TEXT,
        phone INTEGER UNIQUE
    );
""")

db.commit()

print("\n\n")
cursor.execute("PRAGMA table_info(students)")
print(cursor.fetchall())
cursor.execute("PRAGMA table_info(classes)")
print(cursor.fetchall())
cursor.execute("PRAGMA table_info(marks)")
print(cursor.fetchall())
cursor.execute("PRAGMA table_info(teachers)")
print(cursor.fetchall(), "\n\n")

cursor.execute("DROP TABLE IF EXISTS marks")
db.commit()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS marks (
        id INTEGER PRIMARY KEY,
        student_id INTEGER,
        subject TEXT,
        score INTEGER,
        max_score INTEGER
    );
""")

cursor.execute("PRAGMA table_info(marks)")
print(cursor.fetchall(), "\n\n")