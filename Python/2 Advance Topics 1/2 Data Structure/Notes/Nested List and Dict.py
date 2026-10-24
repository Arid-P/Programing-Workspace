# Advanced Data Structures: Nested Lists and Dictionaries

# 1. Nested Lists
# A nested list is simply a list within another list.

# Example: Creating a nested list
nested_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Accessing elements in a nested list
# Access the second row, third element (value: 6)
print(nested_list[1][2])

# Modifying elements in a nested list
nested_list[1][2] = 10  # Change the value 6 to 10
print(nested_list)

# Traversing a nested list using loops
for row in nested_list:
    for item in row:
        print(item, end=" ")
print()

# Real-world example: Representing a matrix
matrix = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]
print("Matrix representation:")
for row in matrix:
    print(row)


# 2. Nested Dictionaries
# A nested dictionary is a dictionary inside another dictionary.

# Example: Creating a nested dictionary
nested_dict = {
    "class_9A": {"student_1": "Ari", "student_2": "Sam"},
    "class_9B": {"student_1": "Mia", "student_2": "Liam"}
}

# Accessing elements in a nested dictionary
# Access student_1 in class_9A (value: 'Ari')
print(nested_dict["class_9A"]["student_1"])

# Modifying elements in a nested dictionary
nested_dict["class_9A"]["student_1"] = "Aridaman"
print(nested_dict)

# Adding a new key-value pair to a nested dictionary
nested_dict["class_9C"] = {"student_1": "Emma", "student_2": "Noah"}
print(nested_dict)

# Traversing a nested dictionary
for class_name, students in nested_dict.items():
    print(f"Class: {class_name}")
    for key, value in students.items():
        print(f"  {key}: {value}")


# 3. Applications of Nested Structures
# Example: Representing hierarchical data
file_system = {
    "home": {
        "user1": ["file1.txt", "file2.txt"],
        "user2": ["file3.txt", "file4.txt"]
    },
    "var": {
        "log": ["syslog", "kernel.log"]
    }
}

# Access a specific file
print(file_system["home"]["user1"][0])  # Outputs: 'file1.txt'

# Adding new files
file_system["home"]["user1"].append("file5.txt")
print(file_system)

# Example: Building JSON-like data structures
data = {
    "employees": [
        {"name": "Alice", "age": 30, "role": "Engineer"},
        {"name": "Bob", "age": 25, "role": "Designer"}
    ]
}

# Accessing data from JSON-like structures
for employee in data["employees"]:
    print(f"{employee['name']} is a {employee['role']}.")