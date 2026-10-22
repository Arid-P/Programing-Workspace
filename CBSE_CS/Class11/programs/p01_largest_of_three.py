"""
Program 01: Find the Largest of Three Numbers
CBSE Class 11 Practical File

Objective:
Input three numbers from the console and determine the largest among them
using conditional statements (if-elif-else).
"""

def find_largest(a: float, b: float, c: float) -> float:
    if a > b:
        if a >= c:
            return a
        else:
            return c
    else:
        if b >= c:
            return b
        else:
            return c
    


if __name__ == "__main__":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    num3 = float(input("Enter third number: "))
    
    result = find_largest(num1, num2, num3)
    print(f"The largest number among {num1}, {num2}, and {num3} is: {result}")

