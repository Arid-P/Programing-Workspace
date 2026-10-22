"""
Program 03: Three Nested Loop Triangle Patterns
CBSE Class 11 Practical File

Objective:
Input an integer n and display three classic patterns:
Pattern A: Stars (*)
*
* *
* * *

Pattern B: Numbers
1
1 2
1 2 3

Pattern C: Alphabets (Hint: use chr(65 + j))
A
A B
A B C
"""

#I am supposing that n means number of rows

def print_star_triangle(n: int) -> None:
    for i in range(n):
        for j in range(i+1):
            print('*', end=' ')
        print()


def print_number_triangle(n: int) -> None:
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end=' ')
        print()

#I am supposing that user can enter n greater than 26 as well
def print_alphabet_triangle(n: int) -> None:
    alphabets = []
    for i in range(26):
        alphabets.append(chr(65+i))

    for i in range(n):
        for j in range(i+1):
            j = j % 26
            print(alphabets[j], end=' ')
        print()


if __name__ == "__main__":
    rows = int(input("Enter number of rows (n): "))
    
    print("\n--- Pattern A (Stars) ---")
    print_star_triangle(rows)
    
    print("\n--- Pattern B (Numbers) ---")
    print_number_triangle(rows)
    
    print("\n--- Pattern C (Alphabets) ---")
    print_alphabet_triangle(rows)

