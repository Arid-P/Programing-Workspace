/* ---------------------------------------------------------
   SQL LESSON 1 — BASICS
   Concepts: CREATE DATABASE, CREATE TABLE, INSERT, SELECT,
             WHERE, ORDER BY
---------------------------------------------------------- */

/* ----------------------
   1. CREATE A DATABASE
   CREATE DATABASE -> creates a new database
   USE -> selects it for running queries
----------------------- */
CREATE DATABASE testdb;
USE testdb;


/* ----------------------
   2. CREATE A TABLE
   id  : primary key, auto increase
   name: text up to 50 chars
   age : integer
   grade: small string
----------------------- */
CREATE TABLE students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    age INT,
    grade VARCHAR(10)
);


/* ----------------------
   3. INSERT DATA
   INSERT INTO -> adds new rows
----------------------- */
INSERT INTO students (name, age, grade)
VALUES 
('Ari', 16, '10A'),
('Riya', 15, '9B'),
('Sam', 17, '11C'),
('Rahul', 14, '8A'),
('Tanya', 16, '10B');


/* ----------------------
   4. SELECT DATA
   SELECT * -> shows all records
----------------------- */
SELECT * FROM students;


/* ----------------------
   5. WHERE Clause
   WHERE -> filters rows based on condition
   Comparison operators:
     = (equal)
     > (greater than)
     < (less than)
     <> (not equal)
----------------------- */
SELECT * FROM students
WHERE age = 16;


/* ----------------------
   6. ORDER BY Clause
   ORDER BY -> sorting results
     ASC  : ascending (default)
     DESC : descending
----------------------- */
SELECT * FROM students
ORDER BY age DESC;



/* =========================================================
   MINI PROJECT SECTION
   Create another table: courses
========================================================== */

/* ----------------------
   Create courses table
----------------------- */
CREATE TABLE courses (
    course_id INT PRIMARY KEY AUTO_INCREMENT,
    course_name VARCHAR(50),
    instructor VARCHAR(50)
);

/* ----------------------
   Insert sample courses
----------------------- */
INSERT INTO courses (course_name, instructor)
VALUES
('Math', 'John'),
('Physics', 'Tina'),
('Computer', 'Aman');

/* ----------------------
   Display sorted result
----------------------- */
SELECT * FROM courses
ORDER BY course_name ASC;
