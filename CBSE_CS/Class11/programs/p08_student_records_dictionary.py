"""
Program 08: Student Records Dictionary (Roll, Name, Marks)
CBSE Class 11 Practical File

Objective:
1. Maintain student records in a dictionary mapping roll_number -> {"name": str, "marks": float}.
2. Display all student records in tabular format.
3. Filter and return a dictionary of students scoring strictly above 75 marks.
4. Safely search for a student's record by roll number using .get() (handling missing keys without crashing).
"""


def filter_top_students(
    students: dict[int, dict], threshold: float = 75.0
) -> dict[int, dict]:
    # TODO: Iterate through students and return a new dictionary containing only
    # students whose marks > threshold.
    result = {}
    for roll, info in students.items():
        if info["marks"] > threshold:
            result.update({roll: info})

    return result


def search_student(students: dict[int, dict], roll: int) -> dict | None:
    return students.get(roll, None)


if __name__ == "__main__":
    # Sample record dataset: {roll: {"name": str, "marks": float}}
    records = {
        101: {"name": "Aman Sharma", "marks": 88.5},
        102: {"name": "Rohit Verma", "marks": 68.0},
        103: {"name": "Priya Singh", "marks": 92.0},
        104: {"name": "Neha Gupta", "marks": 74.5},
        105: {"name": "Siddharth Jain", "marks": 81.0},
    }

    print("--- All Student Records ---")
    for roll, info in records.items():
        print(f"Roll: {roll} | Name: {info['name']} | Marks: {info['marks']}%")

    print("\n--- Students Scoring Above 75% ---")
    top_students = filter_top_students(records, 75.0)
    for roll, info in top_students.items():
        print(f"Roll: {roll} | Name: {info['name']} | Marks: {info['marks']}%")

    print("\n--- Search Student by Roll Number ---")
    search_roll = int(input("Enter roll number to search: "))
    found = search_student(records, search_roll)
    if found:
        print(f"Found: Name = {found['name']}, Marks = {found['marks']}%")
    else:
        print(f"Roll number {search_roll} not found in database.")
