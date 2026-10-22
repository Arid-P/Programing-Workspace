# CBSE Class 11 Computer Science (083)
## Practical Laboratory File & Program Record

This file records all official CBSE Class 11 practical programs, including their aims, algorithms, verified Python code implementations, and execution test outputs.

---

### Program 01: Find the Largest of Three Numbers
* **File:** [`p01_largest_of_three.py`](file:///home/hp/Programing-Workspace/CBSE_CS/Class11/programs/p01_largest_of_three.py)
* **Topic Alignment:** Unit 2 — Conditional Statements (`if-elif-else`)
* **Aim:** Input three numbers from the user and determine the maximum value among them using nested conditional logic without built-in helper functions.

#### Algorithm:
1. Input three numerical values $a, b, c$.
2. Compare $a$ and $b$:
   - If $a > b$: compare $a$ and $c$. If $a \ge c$, then $a$ is largest; otherwise $c$ is largest.
   - If $b \ge a$: compare $b$ and $c$. If $b \ge c$, then $b$ is largest; otherwise $c$ is largest.
3. Return and display the largest value.

#### Verified Student Implementation:
```python
"""
Program 01: Find the Largest of Three Numbers
CBSE Class 11 Practical File
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
```

#### Sample Execution Outputs:
```text
Test Run 1 (Distinct values):
Enter first number: 12.5
Enter second number: 45.2
Enter third number: 8.7
The largest number among 12.5, 45.2, and 8.7 is: 45.2

Test Run 2 (Negative values & equality):
Enter first number: -10
Enter second number: -5
Enter third number: -5
The largest number among -10.0, -5.0, and -5.0 is: -5.0
```

---

### Program 02: Prime vs Composite Number Verification
* **File:** [`p02_prime_check.py`](file:///home/hp/Programing-Workspace/CBSE_CS/Class11/programs/p02_prime_check.py)
* **Topic Alignment:** Unit 2 — Iterative Statements (`for` loop with `else:` suite and `break`)
* **Aim:** Input a positive integer $n > 1$ and determine whether it is prime or composite by testing trial divisors up to $\lfloor\sqrt{n}\rfloor$.

#### Algorithm:
1. Input positive integer $n$. If $n \le 1$, output that it is neither prime nor composite.
2. Iterate trial divisor $d$ from $2$ up to $\lfloor\sqrt{n}\rfloor$ (using range `range(2, int(sqrt(n)) + 1)`).
3. If $n \% d == 0$, $d$ is a factor: $n$ is composite; return `False`.
4. If loop completes with no factors found, $n$ is prime; return `True`.

#### Verified Student Implementation:
```python
"""
Program 02: Prime vs Composite Number Verification
CBSE Class 11 Practical File
"""

from math import sqrt

def is_prime(n: int) -> bool:
    for d in range(2, (int(sqrt(n)) + 1)):
        if n % d == 0:
            return False

    return True


if __name__ == "__main__":
    number = int(input("Enter an integer greater than 1: "))
    
    if number <= 1:
        print("Neither prime nor composite.")
    else:
        if is_prime(number):
            print(f"{number} is a PRIME number.")
        else:
            print(f"{number} is a COMPOSITE number.")
```

#### Sample Execution Outputs:
```text
Test Run 1 (Prime number):
Enter an integer greater than 1: 29
29 is a PRIME number.

Test Run 2 (Perfect square composite):
Enter an integer greater than 1: 25
25 is a COMPOSITE number.

Test Run 3 (Boundary prime):
Enter an integer greater than 1: 2
2 is a PRIME number.
```

---

### Program 03: Three Nested Loop Triangle Patterns
* **File:** [`p03_triangle_patterns.py`](file:///home/hp/Programing-Workspace/CBSE_CS/Class11/programs/p03_triangle_patterns.py)
* **Topic Alignment:** Unit 2 — Nested Loops (`for` inside `for`)
* **Aim:** Input the number of rows $n$ and display three classic right-angled triangle patterns using asterisks, numbers, and uppercase alphabets.

#### Algorithm:
1. Input row count $n$.
2. **Pattern A (Stars):** Outer loop $i$ from $0$ to $n-1$; inner loop $j$ from $0$ to $i$; print `*` followed by a space; newline after each row.
3. **Pattern B (Numbers):** Outer loop $i$ from $1$ to $n$; inner loop $j$ from $1$ to $i$; print $j$ followed by a space; newline after each row.
4. **Pattern C (Alphabets):** Outer loop $i$ from $0$ to $n-1$; inner loop $j$ from $0$ to $i$; print character with code `chr(65 + (j % 26))`; newline after each row.

#### Verified Student Implementation:
```python
"""
Program 03: Three Nested Loop Triangle Patterns
CBSE Class 11 Practical File
"""

def print_star_triangle(n: int) -> None:
    for i in range(n):
        for j in range(i + 1):
            print('*', end=' ')
        print()


def print_number_triangle(n: int) -> None:
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=' ')
        print()


def print_alphabet_triangle(n: int) -> None:
    alphabets = []
    for i in range(26):
        alphabets.append(chr(65 + i))

    for i in range(n):
        for j in range(i + 1):
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
```

#### Sample Execution Outputs:
```text
Enter number of rows (n): 4

--- Pattern A (Stars) ---
* 
* * 
* * * 
* * * * 

--- Pattern B (Numbers) ---
1 
1 2 
1 2 3 
1 2 3 4 

--- Pattern C (Alphabets) ---
A 
A B 
A B C 
A B C D 
```

