import sqlite3 as sq

db = sq.connect("Python +SQL\Practice databases\school.db") #type: ignore

cursor = db.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        number INTEGER,
        grade TEXT
    );
""")

db.commit()

cursor.execute("INSERT INTO students (id, number, grade) VALUES (?, ?, ?)", (233, 5450989879, "6-A"))
db.commit()

cursor.execute("SELECT * FROM students ORDER BY id ASC")
rows = cursor.fetchall()
print(rows)