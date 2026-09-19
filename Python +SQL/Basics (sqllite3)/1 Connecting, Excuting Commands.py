# ------------------------------------------------------------
# LESSON 1 NOTES: Connecting Python to SQLite & Running Queries
# ------------------------------------------------------------

# SQLite is a serverless database engine built into Python.
# Using the sqlite3 module, we can:
# 1. Connect to a database file (it will be created automatically if missing)
# 2. Create a cursor to execute SQL queries
# 3. Run SQL commands (CREATE, INSERT, SELECT, UPDATE, DELETE)
# 4. Commit changes to save data
# 5. Close the connection properly

import sqlite3  # Built-in module for SQLite

# -----------------------------
# 1. CONNECT TO A DATABASE FILE
# -----------------------------
# "example.db" will be created in the working directory if it doesn't exist.
conn = sqlite3.connect("Python +SQL\Practice databases\example.db") # type: ignore

# ------------------------
# 2. CREATE A CURSOR OBJECT
# ------------------------
cursor = conn.cursor()

# ---------------------------------------
# 3. RUN THE FIRST SQL QUERY: CREATE TABLE
# ---------------------------------------
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    );
""")

# Save changes.
#We do .commit so that all the changes or command that we have excuted be saved
#as on cursor.execute the changes are present as temporary.
conn.commit()

# -------------------------------------
# 4. INSERT SAMPLE DATA INTO THE TABLE
# -------------------------------------
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Ari", 16))
conn.commit()

# ---------------------------
# 5. RETRIEVE AND PRINT DATA
# ---------------------------
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
print(rows)

# --------------------------
# 6. CLOSE THE DB CONNECTION
# --------------------------
conn.close()
