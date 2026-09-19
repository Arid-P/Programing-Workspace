# ------------------------------------------------------------
# LESSON 6 NOTES: Error Handling in Database Code
# ------------------------------------------------------------

import sqlite3 as sq

try:
    db = sq.connect(r"Python +SQL\Basics (sqllite3)\Practice databases\school.db")
    cursor = db.cursor()

    # ---------------------------
    # Example: Inserting duplicate primary key
    # ---------------------------
    cursor.execute("INSERT INTO students (id, number, grade) VALUES (?, ?, ?)", (301, 100, "9-A"))
    db.commit()

except sq.IntegrityError as e:
    print("Integrity error:", e)

except sq.OperationalError as e:
    print("Operational error:", e)

except Exception as e:
    print("Some other error:", e)

finally:
    db.close()

# ---------------------------
# Raising a custom error if no row found
# ---------------------------
try:
    db = sq.connect(r"Python +SQL\Practice databases\school.db")
    cursor = db.cursor()

    cursor.execute("SELECT * FROM students WHERE id=?", (999,))
    result = cursor.fetchone()
    if result is None:
        raise ValueError("No student found with this ID")

except ValueError as e:
    print(e)

finally:
    db.close()
