import sqlite3

db_path = r"C:\Programming\Python +SQL\Projects\School Management System\0school.db"
conn = sqlite3.connect(db_path)
cur = conn.cursor()


# 2. Copy data
cur.execute("INSERT INTO students_new (id, name, grade) SELECT id, name, grade FROM students")

# 3. Drop old table
cur.execute("DROP TABLE students")

# 4. Rename new table
cur.execute("ALTER TABLE students_new RENAME TO students")

conn.commit()
conn.close()
