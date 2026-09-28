import sqlite3 as sq


with sq.connect(r'Python +SQL\Practice databases\school.db') as conn:
    cursor = conn.cursor()

    with open(r"Python +SQL\Practice databases\backup.txt", "w") as file:
        for row in cursor.execute("SELECT * FROM classes"):
            file.write(str(row) + "\n")
