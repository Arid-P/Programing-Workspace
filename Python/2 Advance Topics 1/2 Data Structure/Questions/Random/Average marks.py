from collections import namedtuple


def calculate_average_marks (students) -> dict :
    more_than_70_students = list(filter(lambda student: student.math_marks > 70 and student.science_marks > 70, students))
    
    average_marks = {
        student.name : (student.math_marks + student.science_marks) / 2 for
        student in more_than_70_students
    }
    
    return average_marks



def main () -> None :

    # Defining the namedtuple for student
    Student = namedtuple('Student', ['name', 'age', 'math_marks', 'science_marks'])
    
    # Create a list of students
    students: list[Student] = [
        Student(name="Alice", age=16, math_marks=85, science_marks=90),
        Student(name="Bob", age=17, math_marks=60, science_marks=75),
        Student(name="Charlie", age=15, math_marks=70, science_marks=72),
        Student(name="David", age=16, math_marks=88, science_marks=95),
        Student(name="Eve", age=17, math_marks=65, science_marks=60),
        Student(name="Frank", age=16, math_marks=90, science_marks=88),
        Student(name="Grace", age=15, math_marks=55, science_marks=80),
        Student(name="Hannah", age=16, math_marks=80, science_marks=78),
        Student(name="Isaac", age=17, math_marks=92, science_marks=91),
        Student(name="Jack", age=16, math_marks=74, science_marks=68)
    ]
    
    good_students = calculate_average_marks(students)
    
    for student_name, marks in good_students.items() :
        print(f"Name : {student_name} Marks : {marks}")
    
    return

if __name__ == "__main__" :
    main()