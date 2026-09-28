/* ---------------------------------------------------------
   SQL LESSON 2 — UPDATE, DELETE & BASIC CONSTRAINTS
---------------------------------------------------------- */

USE testdb;

/* ---------------------------------------------------------
   UPDATE STATEMENT
   UPDATE -> modify existing records in a table
   Syntax:
      UPDATE table_name
      SET column = value
      WHERE condition;
   Always use WHERE or entire table will update.
---------------------------------------------------------- */

-- Example: Change Tanya's grade
UPDATE students
SET grade = '10A'
WHERE name = 'Tanya';

SELECT * FROM students;


/* ---------------------------------------------------------
   DELETE STATEMENT
   DELETE -> remove records from a table
   Syntax:
      DELETE FROM table_name
      WHERE condition;
   WARNING: If you forget WHERE, all rows get deleted.
---------------------------------------------------------- */

-- Example: Delete student Rahul
DELETE FROM students
WHERE name = 'Rahul';

SELECT * FROM students;


/* =========================================================
   BASIC CONSTRAINTS
   Constraints maintain data correctness.
   Types:
     - NOT NULL  : value cannot be empty
     - UNIQUE    : no duplicate values allowed
     - DEFAULT   : assigns default value if none provided
========================================================== */

-- Create table teachers to demonstrate constraints
CREATE TABLE teachers (
    teacher_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,     -- must have a value
    subject VARCHAR(50) UNIQUE,    -- all subjects must be unique
    experience INT DEFAULT 1       -- default = 1 year
);

-- Insert sample teachers
INSERT INTO teachers (name, subject, experience)
VALUES
('Amit', 'Physics', 5),
('Neha', 'Math', 3),
('John', NULL, 2);  -- allowed because subject is not NOT NULL

-- Example of DEFAULT usage
INSERT INTO teachers (name, subject)
VALUES ('Tina', 'Computer');

SELECT * FROM teachers;


/* ---------------------------------------------------------
   PRACTICE (your tasks)
   1. Update experience of Neha -> 4
   2. Delete teacher where subject is NULL
   3. Try inserting another teacher with subject 'Math'
      Result: ERROR (duplicate entry for UNIQUE constraint)
---------------------------------------------------------- */


/* =========================================================
   MINI PROJECT — Books Table
   Create a table with constraints and perform operations
========================================================== */

-- Create books table
CREATE TABLE books (
    book_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    author VARCHAR(100) NOT NULL,
    price INT DEFAULT 200
);

-- Insert records
INSERT INTO books (title, author, price)
VALUES
('Atomic Habits', 'James Clear', 350),
('The Alchemist', 'Paulo Coelho', 250),
('Deep Work', 'Cal Newport', 300);

-- Update price of one book
UPDATE books
SET price = 400
WHERE title = 'Deep Work';

-- Delete one book
DELETE FROM books
WHERE title = 'The Alchemist';

-- View books
SELECT * FROM books;
