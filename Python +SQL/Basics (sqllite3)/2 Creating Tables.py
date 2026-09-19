# ------------------------------------------------------------
# LESSON 2 NOTES: Creating Tables Through Python (Deep Dive)
# ------------------------------------------------------------

# SQLite uses only five real storage classes:
# INTEGER, REAL, TEXT, BLOB, NULL.
# Other types (VARCHAR, CHAR, BOOLEAN, etc.) are accepted but internally
# mapped to one of these storage classes.

import sqlite3 as sq

# Connect to database in the required directory
db = sq.connect("Python +SQL\\Practice databases\\school.db")
cursor = db.cursor()

# ------------------------------------------------------------
# 1. CREATING TABLES
# ------------------------------------------------------------
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        grade TEXT
    );
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS subjects (
        subject_id INTEGER PRIMARY KEY,
        subject_name TEXT
    );
""")

db.commit()

# ------------------------------------------------------------
# 2. TABLE WITH CONSTRAINTS
# ------------------------------------------------------------
cursor.execute("""
    CREATE TABLE IF NOT EXISTS teachers (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        subject TEXT NOT NULL,
        joining_year INTEGER DEFAULT 2024
    );
""")
db.commit()

# ------------------------------------------------------------
# 3. DROP A TABLE
# ------------------------------------------------------------
cursor.execute("DROP TABLE IF EXISTS temp_table")
db.commit()

# ------------------------------------------------------------
# 4. CHECK TABLE STRUCTURE USING PRAGMA
# ------------------------------------------------------------
cursor.execute("PRAGMA table_info(students)")
print(cursor.fetchall())

# Close the database
db.close()
