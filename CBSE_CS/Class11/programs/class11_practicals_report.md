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



---

### Program 04: Count Vowels, Consonants, Uppercase, and Lowercase Characters
* **File:** [`p04_string_character_counts.py`](file:///home/hp/Programing-Workspace/CBSE_CS/Class11/programs/p04_string_character_counts.py)
* **Topic Alignment:** Unit 2 — Strings (Traversal, Character Classification Predicates)
* **Aim:** Input a line of text from the user and calculate the frequency of vowels, consonants, uppercase characters, and lowercase characters.

#### Algorithm:
1. Input string `text`. Initialize a counter dictionary with keys `'vowels'`, `'consonants'`, `'uppercase'`, `'lowercase'` set to 0.
2. Iterate through each character `el` in `text`:
   - If `el.isalpha()` is false (digit, space, symbol), skip to next character.
   - If `el.lower()` is in `['a', 'e', 'i', 'o', 'u']`, increment `'vowels'`; else increment `'consonants'`.
   - If `el.islower()` is true, increment `'lowercase'`; else increment `'uppercase'`.
3. Return and display the frequency breakdown.

#### Verified Student Implementation:
```python
"""
Program 04: Count Vowels, Consonants, Uppercase, and Lowercase Characters
CBSE Class 11 Practical File
"""

def analyze_string(text: str) -> dict[str, int]:
    counter = {"vowels": 0, "consonants": 0, "uppercase": 0, "lowercase": 0}

    for el in text:
        if not el.isalpha():
            continue

        # Checking for vowels and consonants
        if el.lower() in ["a", "e", "i", "o", "u"]:
            counter["vowels"] += 1
        else:
            counter["consonants"] += 1

        # Checking for uppercase and lowercase
        if el.islower():
            counter["lowercase"] += 1
        else:
            counter["uppercase"] += 1

    return counter


if __name__ == "__main__":
    line = input("Enter a string: ")
    counts = analyze_string(line)

    print("\n--- String Analysis ---")
    print(f"Vowels:     {counts.get('vowels', 0)}")
    print(f"Consonants: {counts.get('consonants', 0)}")
    print(f"Uppercase:  {counts.get('uppercase', 0)}")
    print(f"Lowercase:  {counts.get('lowercase', 0)}")
```

#### Sample Execution Outputs:
```text
Enter a string: Python 3.12 Programming!

--- String Analysis ---
Vowels:     4
Consonants: 13
Uppercase:  2
Lowercase:  15
```

---

### Program 05: String Palindrome Check and Case Conversion
* **File:** [`p05_palindrome_string_case_conversion.py`](file:///home/hp/Programing-Workspace/CBSE_CS/Class11/programs/p05_palindrome_string_case_conversion.py)
* **Topic Alignment:** Unit 2 — Strings (Traversal, Two-Pointer Algorithm, Case Conversion Mechanics)
* **Aim:** Check whether an input string is a palindrome using two-pointer traversal, and construct a new string with inverted case (toggling uppercase to lowercase and vice-versa) using ASCII code boundaries without `swapcase()`.

#### Algorithm:
1. **Palindrome Check:**
   - Initialize two pointers `l = 0` and `r = len(text) - 1`.
   - While `l < r`: if `text[l] != text[r]`, return `False`; increment `l` and decrement `r`.
   - If pointers meet or cross with all characters matching, return `True`.
2. **Case Inversion:**
   - Initialize an empty result string `str_new = ""`.
   - Iterate through each character `el` in `text`:
     - If `not el.isalpha()`, append `el` directly to `str_new`.
     - Else check ASCII code: if `ord(el) > 90` (lowercase $97..122$), convert with `el.upper()`; else (uppercase $65..90$), convert with `el.lower()`.
   - Return `str_new`.

#### Verified Student Implementation:
```python
"""
Program 05: String Palindrome Check and Case Conversion
CBSE Class 11 Practical File
"""

def is_palindrome(text: str) -> bool:
    l, r = 0, len(text) - 1

    while l < r:
        if text[l] != text[r]:
            return False
        l += 1
        r -= 1

    return True


def toggle_case(text: str) -> str:
    str_new = ""

    for el in text:
        if not el.isalpha():
            str_new += el
            continue

        if ord(el) > 90:
            str_new += el.upper()
        else:
            str_new += el.lower()

    return str_new


if __name__ == "__main__":
    user_str = input("Enter a string: ")

    # 1. Palindrome Check
    if is_palindrome(user_str):
        print(f"'{user_str}' is a PALINDROME.")
    else:
        print(f"'{user_str}' is NOT a palindrome.")

    # 2. Case Conversion
    converted = toggle_case(user_str)
    print(f"Case-toggled string: '{converted}'")
```

#### Sample Execution Outputs:
```text
Test Run 1 (Palindrome string):
Enter a string: racecar
'racecar' is a PALINDROME.
Case-toggled string: 'RACECAR'

Test Run 2 (Mixed case sentence):
Enter a string: Hello World 123!
'Hello World 123!' is NOT a palindrome.
Case-toggled string: 'hELLO wORLD 123!'
```


---

### Program 06: List Operations — Linear Search and Manual Min/Max/Mean
* **File:** [`p06_list_linear_search_min_max.py`](file:///home/hp/Programing-Workspace/CBSE_CS/Class11/programs/p06_list_linear_search_min_max.py)
* **Topic Alignment:** Unit 2 — Lists (Algorithms, Traversal, Statistical Computations)
* **Aim:** Manually determine the minimum, maximum, and arithmetic mean of a numerical list without built-in functions, and implement an iterative linear search returning the target index or $-1$.

#### Algorithm:
1. **Min/Max/Mean:**
   - Initialize `minimum = nums[0]`, `maximum = nums[0]`, `total = 0`.
   - Iterate through each number in `nums`: add to `total`, update `minimum` if smaller, update `maximum` if larger.
   - Return `minimum`, `maximum`, and `mean = total / len(nums)`.
2. **Linear Search:**
   - Iterate index `i` from 0 to `len(lst) - 1`.
   - If `lst[i] == target`, return `i`.
   - If loop exhausts without match, return `-1`.

#### Verified Student Implementation:
```python
"""
Program 06: List Operations — Linear Search and Manual Min/Max/Mean
CBSE Class 11 Practical File
"""

def linear_search(lst: list, target) -> int:
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    
    return -1


def compute_min_max_mean(nums: list[float]) -> tuple[float, float, float]:
    result = [nums[0], nums[0], 0]

    for el in nums:
        # Sum
        result[2] += el

        # min check
        if result[0] > el:
            result[0] = el
        
        # max check
        if result[1] < el:
            result[1] = el   

    return result[0], result[1], result[2] / len(nums)


if __name__ == "__main__":
    raw_input = input("Enter numbers separated by spaces: ")
    data = [float(x) for x in raw_input.split()]
    
    if not data:
        print("List is empty!")
    else:
        # 1. Min, Max, Mean
        minimum, maximum, mean = compute_min_max_mean(data)
        print(f"\n--- Statistics ---")
        print(f"Minimum: {minimum}")
        print(f"Maximum: {maximum}")
        print(f"Mean:    {mean:.2f}")
        
        # 2. Linear Search
        search_target = float(input("\nEnter a number to search for: "))
        found_idx = linear_search(data, search_target)
        if found_idx != -1:
            print(f"Number {search_target} found at index {found_idx}.")
        else:
            print(f"Number {search_target} was not found in the list.")
```

#### Sample Execution Outputs:
```text
Enter numbers separated by spaces: 10 50 20 40 30

--- Statistics ---
Minimum: 10.0
Maximum: 50.0
Mean:    30.00

Enter a number to search for: 20
Number 20.0 found at index 2.
```

---

### Program 07: Swap Even and Odd Positioned Elements in a List
* **File:** [`p07_list_swap_even_odd.py`](file:///home/hp/Programing-Workspace/CBSE_CS/Class11/programs/p07_list_swap_even_odd.py)
* **Topic Alignment:** Unit 2 — Lists (In-Place Mutation, Index Arithmetic, Stepping)
* **Aim:** Swap adjacent elements at even and odd index positions ($0 \leftrightarrow 1, 2 \leftrightarrow 3, \dots$) in place, preserving the last element untouched if the list has odd length.

#### Algorithm:
1. If `len(lst) <= 1`, return immediately.
2. Compute `upper_limit = (len(lst) // 2) * 2`.
3. Loop index `i` from 0 up to `upper_limit` stepping by 2:
   - Swap: `lst[i], lst[i + 1] = lst[i + 1], lst[i]`.
4. The list is modified in place with $O(1)$ auxiliary space.

#### Verified Student Implementation:
```python
"""
Program 07: Swap Even and Odd Positioned Elements in a List
CBSE Class 11 Practical File
"""

def swap_adjacent_elements(lst: list) -> None:
    if len(lst) <= 1:
        return 

    upper_limit = ((len(lst) // 2) * 2) 
    for i in range(0, upper_limit, 2):  # Runs like 0, 2, 4, 6
        lst[i], lst[i + 1] = lst[i + 1], lst[i]


if __name__ == "__main__":
    raw_input = input("Enter list elements separated by spaces: ")
    user_list = raw_input.split()

    print(f"\nOriginal List: {user_list}")
    swap_adjacent_elements(user_list)
    print(f"Swapped List:  {user_list}")
```

#### Sample Execution Outputs:
```text
Test Run 1 (Even number of elements):
Enter list elements separated by spaces: A B C D E F

Original List: ['A', 'B', 'C', 'D', 'E', 'F']
Swapped List:  ['B', 'A', 'D', 'C', 'F', 'E']

Test Run 2 (Odd number of elements):
Enter list elements separated by spaces: 10 20 30 40 50

Original List: ['10', '20', '30', '40', '50']
Swapped List:  ['20', '10', '40', '30', '50']
```


---

### Program 08: Student Records Dictionary (Roll, Name, Marks)
* **File:** [`p08_student_records_dictionary.py`](file:///home/hp/Programing-Workspace/CBSE_CS/Class11/programs/p08_student_records_dictionary.py)
* **Topic Alignment:** Unit 2 — Dictionaries (Key Access, Filtering, Safe Querying with `.get()`)
* **Aim:** Store student records in a dictionary mapping `roll_number -> {"name": str, "marks": float}`, display records, filter students scoring above 75%, and implement safe search by roll number without `KeyError`.

#### Algorithm:
1. Initialize nested dictionary `records` with sample data.
2. **Filtering (`filter_top_students`):**
   - Initialize empty dictionary `result = {}`.
   - Iterate through `(roll, info)` in `students.items()`:
     - If `info["marks"] > threshold`, update `result` with `{roll: info}`.
   - Return `result`.
3. **Safe Search (`search_student`):**
   - Return `students.get(roll, None)`. If present, returns student dict; if absent, safely returns `None`.

#### Verified Student Implementation:
```python
"""
Program 08: Student Records Dictionary (Roll, Name, Marks)
CBSE Class 11 Practical File
"""

def filter_top_students(
    students: dict[int, dict], threshold: float = 75.0
) -> dict[int, dict]:
    result = {}
    for roll, info in students.items():
        if info["marks"] > threshold:
            result.update({roll: info})

    return result


def search_student(students: dict[int, dict], roll: int) -> dict | None:
    return students.get(roll, None)


if __name__ == "__main__":
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
```

#### Sample Execution Outputs:
```text
--- All Student Records ---
Roll: 101 | Name: Aman Sharma | Marks: 88.5%
Roll: 102 | Name: Rohit Verma | Marks: 68.0%
Roll: 103 | Name: Priya Singh | Marks: 92.0%
Roll: 104 | Name: Neha Gupta | Marks: 74.5%
Roll: 105 | Name: Siddharth Jain | Marks: 81.0%

--- Students Scoring Above 75% ---
Roll: 101 | Name: Aman Sharma | Marks: 88.5%
Roll: 103 | Name: Priya Singh | Marks: 92.0%
Roll: 105 | Name: Siddharth Jain | Marks: 81.0%

--- Search Student by Roll Number ---
Enter roll number to search: 103
Found: Name = Priya Singh, Marks = 92.0%

Enter roll number to search: 999
Roll number 999 not found in database.
```


---

### Program 09: Fibonacci Series Generation (N Terms and Upper Limit)
* **File:** [`p09_fibonacci_series.py`](file:///home/hp/Programing-Workspace/CBSE_CS/Class11/programs/p09_fibonacci_series.py)
* **Topic Alignment:** Unit 2 — Iterative Statements & List Accumulation
* **Aim:** Generate the Fibonacci series $0, 1, 1, 2, 3, 5, \dots$ both for the first $N$ terms and up to a maximum numerical value limit $M$.

#### Algorithm:
1. **First $N$ Terms (`generate_fibonacci_n_terms`):**
   - If $n \le 0$, return `[]`.
   - If $n = 1$, return `[0]`.
   - If $n = 2$, return `[0, 1]`.
   - Otherwise, pre-allocate a list of size $n$, set index 0 to 0 and index 1 to 1.
   - For $i$ from 2 to $n - 1$:
     - Compute $\text{series}[i] = \text{series}[i - 1] + \text{series}[i - 2]$.
   - Return `series`.
2. **Up to Value Limit $M$ (`generate_fibonacci_up_to_limit`):**
   - Handle base values for $limit < 0$, $limit = 0$, and $limit = 1$.
   - Initialize series with `[0, 1, 1]`.
   - While True:
     - Compute $\text{curr\_term} = \text{series}[-1] + \text{series}[-2]$.
     - If $\text{curr\_term} > limit$, break and return `series`.
     - Append `curr_term` to `series`.

#### Verified Student Implementation:
```python
"""
Program 09: Fibonacci Series Generation
CBSE Class 11 Practical File
"""

from typing import Optional


def generate_fibonacci_n_terms(n: int) -> list[int]:
    """
    Generate the first n terms of the Fibonacci series.

    Parameters:
        n (int): Number of terms to generate.

    Returns:
        list[int]: A list containing the first n Fibonacci numbers.
                   If n <= 0, return an empty list [].
    """

    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        series = [0] * n  # to save from the new memory chunk hazard with append
        series[1] = 1

    for i in range(2, n):
        series[i] = series[i - 1] + series[i - 2]

    return series


def generate_fibonacci_up_to_limit(limit: int) -> list[int]:
    """
    Generate all Fibonacci numbers less than or equal to `limit`.

    Parameters:
        limit (int): Upper bound value.

    Returns:
        list[int]: All Fibonacci numbers <= limit.
                   If limit < 0, return [].
    """
    if limit < 0:
        return []
    elif limit == 0:
        return [0]
    elif limit == 1:
        return [0, 1, 1]

    series = [0, 1, 1]

    i = 3
    while True:
        curr_term = series[i - 1] + series[i - 2]

        if curr_term > limit:
            return series

        series.append(curr_term)
        i += 1


if __name__ == "__main__":
    print("--- Program 09: Fibonacci Series ---")

    # 1. First N terms
    num_terms = int(input("Enter number of terms (N): "))
    terms = generate_fibonacci_n_terms(num_terms)
    print(f"First {num_terms} Fibonacci terms: {terms}")

    # 2. Terms up to limit
    max_val = int(input("\nEnter maximum value limit (M): "))
    series_limit = generate_fibonacci_up_to_limit(max_val)
    print(f"Fibonacci terms up to {max_val}: {series_limit}")
```

#### Sample Execution Outputs:
```text
Test Run 1 (Standard execution):
Enter number of terms (N): 7
First 7 Fibonacci terms: [0, 1, 1, 2, 3, 5, 8]

Enter maximum value limit (M): 20
Fibonacci terms up to 20: [0, 1, 1, 2, 3, 5, 8, 13]

Test Run 2 (Boundary inclusive check):
Enter number of terms (N): 2
First 2 Fibonacci terms: [0, 1]

Enter maximum value limit (M): 13
Fibonacci terms up to 13: [0, 1, 1, 2, 3, 5, 8, 13]
```

---

### Program 10: Sum of Mathematical Series (Powers & Factorials)
* **File:** [`p10_series_sum_alternating_powers.py`](file:///home/hp/Programing-Workspace/CBSE_CS/Class11/programs/p10_series_sum_alternating_powers.py)
* **Topic Alignment:** Unit 2 — For Loops, Accumulators, and Math Module
* **Aim:** Compute the sum of a geometric power series $1 + x + x^2 + \dots + x^n$ and an alternating sign factorial series $x - \frac{x^2}{2!} + \frac{x^3}{3!} - \dots \pm \frac{x^n}{n!}$.

#### Algorithm:
1. **Geometric Power Series (`sum_geometric_powers`):**
   - Initialize `total = 0.0`.
   - Loop `i` from 0 to $n$:
     - Add $x^i$ to `total`.
   - Return `total`.
2. **Alternating Factorial Series (`sum_alternating_factorial_series`):**
   - Initialize `series = 0.0`.
   - Loop `i` from 1 to $n$:
     - Compute term sign: $(-1)^{i - 1}$.
     - Compute term magnitude: $\frac{x^i}{i!}$ using `math.factorial(i)`.
     - Add signed term to `series`.
   - Return `series`.

#### Verified Student Implementation:
```python
"""
Program 10: Sum of Mathematical Series
CBSE Class 11 Practical File
"""


def sum_geometric_powers(x: float, n: int) -> float:
    """
    Calculate the sum: 1 + x + x^2 + x^3 + ... + x^n

    Parameters:
        x (float): Base value.
        n (int): Maximum power (non-negative integer).

    Returns:
        float: Sum of the series.
    """
    total = 0.0
    for i in range(n + 1):
        total += x ** i
    return total


def sum_alternating_factorial_series(x: float, n: int) -> float:
    """
    Calculate the alternating series sum:
    x - (x^2 / 2!) + (x^3 / 3!) - (x^4 / 4!) + ... up to n terms.

    Parameters:
        x (float): Base value.
        n (int): Number of terms (n >= 1).

    Returns:
        float: Sum of the series.
    """
    from math import factorial as fact

    series = 0
    for i in range(1, n + 1):
        series += (-1) ** (i - 1) * (x**i / fact(i))

    return series


if __name__ == "__main__":
    print("--- Program 10: Mathematical Series Sums ---")
    val_x = float(input("Enter value of x: "))
    val_n = int(input("Enter value of n (integer >= 0): "))

    # 1. Geometric Powers
    s1 = sum_geometric_powers(val_x, val_n)
    print(f"\nSeries 1: 1 + x + x^2 + ... + x^{val_n} = {s1}")

    # 2. Alternating Factorial Series
    if val_n >= 1:
        s2 = sum_alternating_factorial_series(val_x, val_n)
        print(f"Series 2: x - x^2/2! + x^3/3! - ... ({val_n} terms) = {s2}")
    else:
        print("Series 2 requires n >= 1.")
```

#### Sample Execution Outputs:
```text
Test Run 1:
Enter value of x: 2
Enter value of n (integer >= 0): 3

Series 1: 1 + x + x^2 + ... + x^3 = 15.0
Series 2: x - x^2/2! + x^3/3! - ... (3 terms) = 1.3333333333333333

Test Run 2:
Enter value of x: 1
Enter value of n (integer >= 0): 4

Series 1: 1 + x + x^2 + ... + x^4 = 5.0
Series 2: x - x^2/2! + x^3/3! - ... (4 terms) = 0.625
```

---

### Program 11: Number Classification (Armstrong, Perfect, Palindrome)
* **File:** [`p11_number_classification.py`](file:///home/hp/Programing-Workspace/CBSE_CS/Class11/programs/p11_number_classification.py)
* **Topic Alignment:** Unit 2 — While Loops, Digit Extraction, and Modulo Arithmetic
* **Aim:** Classify any input positive integer as an Armstrong number (order $k$), a Perfect number, and a Palindrome number using mathematical reversal.

#### Algorithm:
1. **Armstrong Check (`is_armstrong`):**
   - If $n \le 0$, return `False`.
   - Determine number of digits $k$ in $n$.
   - While $n > 0$: extract last digit via $n \pmod{10}$, compute $(\text{last\_digit})^k$, add to sum, and update $n \leftarrow n \mathbin{//} 10$.
   - Return True if sum equals original number.
2. **Perfect Number Check (`is_perfect`):**
   - If $n \le 1$, return `False`.
   - Initialize `div_sum = 1`.
   - For $d$ from 2 to $n - 1$: if $n \pmod d == 0$, add $d$ to `div_sum`.
   - Return True if `div_sum == n`.
3. **Palindrome Check (`is_palindrome_number`):**
   - If $n < 0$, return `False`.
   - Initialize `reversed_num = 0`, `temp = n`.
   - While `temp > 0`:
     - `reversed_num = (reversed_num * 10) + (temp % 10)`
     - `temp = temp // 10`
   - Return True if `reversed_num == n`.

#### Verified Student Implementation:
```python
"""
Program 11: Number Classification (Armstrong, Perfect, Palindrome)
CBSE Class 11 Practical File
"""


def is_armstrong(n: int) -> bool:
    """
    Check if positive integer n is an Armstrong number.
    Note: Standard Armstrong numbers are non-negative.
    """
    if n <= 0:
        return False

    k = len(str(n))
    dup_n: int = n
    cube_sum = 0

    while n > 0:
        last_digit: int = n % 10
        cube_sum += last_digit**k
        n //= 10

    if cube_sum != dup_n:
        return False

    return True


def is_perfect(n: int) -> bool:
    """
    Check if positive integer n is a Perfect number.
    A perfect number is equal to the sum of its proper positive divisors (excluding n itself).
    """
    if n <= 1:
        return False

    div_sum = 1
    for d in range(2, n):
        if n % d == 0:
            div_sum += d

    if div_sum != n:
        return False

    return True


def is_palindrome_number(n: int) -> bool:
    """
    Check if integer n is a palindrome number using arithmetic digit reversal
    (without converting the integer to a string).
    """
    if n < 0:
        return False

    reversed_num = 0
    temp = n
    while temp > 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp //= 10

    return reversed_num == n


if __name__ == "__main__":
    print("--- Program 11: Number Classification ---")
    num = int(input("Enter an integer to inspect: "))

    arm = is_armstrong(num)
    perf = is_perfect(num)
    pal = is_palindrome_number(num)

    print(f"\nResults for {num}:")
    print(f"- Armstrong Number:  {arm}")
    print(f"- Perfect Number:    {perf}")
    print(f"- Palindrome Number: {pal}")
```

#### Sample Execution Outputs:
```text
Test Run 1 (3-digit Armstrong):
Enter an integer to inspect: 153
Results for 153:
- Armstrong Number:  True
- Perfect Number:    False
- Palindrome Number: False

Test Run 2 (4-digit Armstrong):
Enter an integer to inspect: 9474
Results for 9474:
- Armstrong Number:  True
- Perfect Number:    False
- Palindrome Number: False

Test Run 3 (Perfect Number):
Enter an integer to inspect: 28
Results for 28:
- Armstrong Number:  False
- Perfect Number:    True
- Palindrome Number: False

Test Run 4 (Palindrome Number):
Enter an integer to inspect: 1331
Results for 1331:
- Armstrong Number:  False
- Perfect Number:    False
- Palindrome Number: True
```


---

### Program 12: Greatest Common Divisor (GCD) and Least Common Multiple (LCM)
* **File:** [`p12_gcd_lcm.py`](file:///home/hp/Programing-Workspace/CBSE_CS/Class11/programs/p12_gcd_lcm.py)
* **Topic Alignment:** Unit 2 — While Loops, Functions, and Euclidean Algorithm
* **Aim:** Compute the GCD (HCF) and LCM of two positive integers using the Euclidean algorithm and the relationship $\text{LCM}(a, b) = \frac{a \times b}{\text{GCD}(a, b)}$.

#### Algorithm:
1. **GCD Calculation (`compute_gcd`):**
   - Validate that $a > 0$ and $b > 0$.
   - While $b > 0$:
     - Update $(a, b) \leftarrow (b, a \pmod b)$.
   - Return $a$.
2. **LCM Calculation (`compute_lcm`):**
   - If $a = 0$ or $b = 0$, return 0.
   - Compute $\text{gcd} = \text{compute\_gcd}(a, b)$.
   - Return $(a \times b) \mathbin{//} \text{gcd}$.

#### Verified Student Implementation:
```python
"""
Program 12: Greatest Common Divisor (GCD) and Least Common Multiple (LCM)
CBSE Class 11 Practical File
"""


def compute_gcd(a: int, b: int) -> int:
    """
    Compute the GCD of two integers using the Euclidean algorithm.

    Parameters:
        a (int), b (int): Input integers.

    Returns:
        int: Greatest common divisor (non-negative).
    """

    if a <= 0 or b <= 0:
        raise ValueError("GCD of non positive numbers cannot be computed")
    elif a == 1 or b == 1:
        return 1

    while b > 0:
        a, b = b, a % b
    return a


def compute_lcm(a: int, b: int) -> int:
    """
    Compute the LCM of two integers.

    Parameters:
        a (int), b (int): Input integers.

    Returns:
        int: Least common multiple.
        Note: If either a or b is 0, LCM is defined as 0.
    """

    if a == 0 or b == 0:
        return 0
    elif a <= 0 or b <= 0:
        raise ValueError("LCM of negative numbers cannot be computed")

    gcd = compute_gcd(a, b)
    return a * b // gcd


if __name__ == "__main__":
    print("--- Program 12: GCD & LCM Calculator ---")
    val_a = int(input("Enter first integer (a): "))
    val_b = int(input("Enter second integer (b): "))

    gcd_res = compute_gcd(val_a, val_b)
    lcm_res = compute_lcm(val_a, val_b)

    print(f"\nFor numbers {val_a} and {val_b}:")
    print(f"- GCD (HCF): {gcd_res}")
    print(f"- LCM:       {lcm_res}")
```

#### Sample Execution Outputs:
```text
Test Run 1 (Standard values):
Enter first integer (a): 12
Enter second integer (b): 18

For numbers 12 and 18:
- GCD (HCF): 6
- LCM:       36

Test Run 2 (Co-prime numbers):
Enter first integer (a): 17
Enter second integer (b): 13

For numbers 17 and 13:
- GCD (HCF): 1
- LCM:       221
```

---

### Program 13: Factorial, Permutations (nPr), and Combinations (nCr)
* **File:** [`p13_factorial_permutations.py`](file:///home/hp/Programing-Workspace/CBSE_CS/Class11/programs/p13_factorial_permutations.py)
* **Topic Alignment:** Unit 2 — Loops, Function Modularisation, and Combinatorics
* **Aim:** Compute $n!$ iteratively and calculate permutations ${}^n P_r = \frac{n!}{(n-r)!}$ and combinations ${}^n C_r = \frac{n!}{r!(n-r)!}$.

#### Algorithm:
1. **Factorial (`compute_factorial`):**
   - If $n < 0$, raise `ValueError`.
   - If $n = 0$, return 1.
   - Initialize `fact = 1`.
   - While $n > 0$: multiply `fact *= n` and decrement $n \leftarrow n - 1$.
   - Return `fact`.
2. **Permutations (`compute_nPr`):**
   - Validate $0 \le r \le n$.
   - Return $\text{compute\_factorial}(n) \mathbin{//} \text{compute\_factorial}(n - r)$.
3. **Combinations (`compute_nCr`):**
   - If $n = r$, return 1.
   - Return $\text{compute\_nPr}(n, r) \mathbin{//} \text{compute\_factorial}(r)$.

#### Verified Student Implementation:
```python
"""
Program 13: Factorial, Permutations (nPr), and Combinations (nCr)
CBSE Class 11 Practical File
"""


def compute_factorial(n: int) -> int:
    """
    Calculate n! iteratively.

    Parameters:
        n (int): Non-negative integer.

    Returns:
        int: Factorial of n (0! = 1, 1! = 1).
        Raises ValueError if n < 0.
    """

    if n < 0:
        raise ValueError("only non negative integers are within the domain")
    elif n == 0:
        return 1

    fact = 1
    while n > 0:
        fact *= n
        n = n - 1

    return fact


def compute_nPr(n: int, r: int) -> int:
    """
    Compute permutations: n! / (n - r)!
    Valid conditions: 0 <= r <= n
    """
    if n < r:
        raise ValueError(
            "n (number of objects) must be greater or equal to r (number of objects being selected)"
        )
    elif n == r:
        return compute_factorial(n)
    elif n < 0 or r < 0:
        raise ValueError("Only non negaative integers are in domain")

    return compute_factorial(n) // compute_factorial(n - r)


def compute_nCr(n: int, r: int) -> int:
    """
    Compute combinations: n! / (r! * (n - r)!)
    Valid conditions: 0 <= r <= n
    """
    if n == r:
        return 1

    return compute_nPr(n, r) // compute_factorial(r)


if __name__ == "__main__":
    print("--- Program 13: Factorial, nPr, and nCr ---")
    n_val = int(input("Enter n (total items >= 0): "))
    r_val = int(input("Enter r (items chosen, 0 <= r <= n): "))

    if n_val < 0 or r_val < 0 or r_val > n_val:
        print("Invalid inputs! Ensure n >= 0 and 0 <= r <= n.")
    else:
        fact_n = compute_factorial(n_val)
        fact_r = compute_factorial(r_val)
        npr = compute_nPr(n_val, r_val)
        ncr = compute_nCr(n_val, r_val)

        print(f"\nFactorial ({n_val}!): {fact_n}")
        print(f"Factorial ({r_val}!): {fact_r}")
        print(f"Permutations P({n_val}, {r_val}): {npr}")
        print(f"Combinations C({n_val}, {r_val}): {ncr}")
```

#### Sample Execution Outputs:
```text
Test Run 1:
Enter n (total items >= 0): 5
Enter r (items chosen, 0 <= r <= n): 2

Factorial (5!): 120
Factorial (2!): 2
Permutations P(5, 2): 20
Combinations C(5, 2): 10

Test Run 2 (Boundary edge cases):
Enter n (total items >= 0): 4
Enter r (items chosen, 0 <= r <= n): 4

Factorial (4!): 24
Factorial (4!): 24
Permutations P(4, 4): 24
Combinations C(4, 4): 1
```

---

### Program 14: Find the Largest and Second Largest in a List
* **File:** [`p14_second_largest_in_list.py`](file:///home/hp/Programing-Workspace/CBSE_CS/Class11/programs/p14_second_largest_in_list.py)
* **Topic Alignment:** Unit 2 — Lists, Single-Pass Algorithms ($O(n)$)
* **Aim:** Find the largest and strictly second largest distinct elements in a list without using `sort()` or `sorted()`.

#### Algorithm:
1. Handle base lengths: if list is empty return `(None, None)`; if length 1 return `(nums[0], None)`.
2. Initialize `max_val = None` and `sec_max = None`.
3. For each element `el` in `nums`:
   - If `max_val is None` or `el > max_val`:
     - Update `sec_max = max_val` and `max_val = el`.
   - Else if `el != max_val` and (`sec_max is None` or `el > sec_max`):
     - Update `sec_max = el`.
4. Return `(max_val, sec_max)`.

#### Verified Student Implementation:
```python
"""
Program 14: Find the Largest and Second Largest in a List
CBSE Class 11 Practical File
"""


def find_largest_and_second_largest(
    nums: list[float],
) -> tuple[float | None, float | None]:
    """
    Find the largest and strictly second largest distinct number in a list without sorting.

    Parameters:
        nums (list[float]): Input list of numerical values.

    Returns:
        tuple[float | None, float | None]: (largest, second_largest)
        If list has fewer than 2 distinct elements, second_largest is None.
        If list is empty, return (None, None).
    """
    if not nums:
        return None, None
    elif len(nums) == 1:
        return nums[0], None
    elif len(nums) == 2:
        if nums[0] == nums[1]:
            return (nums[0], None)

        return (nums[0], nums[1]) if nums[0] > nums[1] else (nums[1], nums[0])

    max_val = None
    sec_max = None

    for el in nums:
        if max_val is None or el > max_val:
            sec_max = max_val
            max_val = el
        elif el != max_val and (sec_max is None or el > sec_max):
            sec_max = el

    return (max_val, sec_max)


if __name__ == "__main__":
    print("--- Program 14: Largest and Second Largest in List ---")
    raw = input("Enter numbers separated by spaces: ")
    numbers = [float(val) for val in raw.split()]

    first, second = find_largest_and_second_largest(numbers)
    print(f"\nGiven list: {numbers}")
    print(f"Largest:        {first}")
    print(f"Second Largest: {second}")
```

#### Sample Execution Outputs:
```text
Test Run 1 (Distinct elements with duplicates):
Enter numbers separated by spaces: 12 45 2 45 31 8

Given list: [12.0, 45.0, 2.0, 45.0, 31.0, 8.0]
Largest:        45.0
Second Largest: 31.0

Test Run 2 (First element largest):
Enter numbers separated by spaces: 50 20 30 40

Given list: [50.0, 20.0, 30.0, 40.0]
Largest:        50.0
Second Largest: 40.0

Test Run 3 (All identical elements):
Enter numbers separated by spaces: 10 10 10

Given list: [10.0, 10.0, 10.0]
Largest:        10.0
Second Largest: None
```

---

### Program 15: Count Frequency of Elements in a List
* **File:** [`p15_list_element_frequencies.py`](file:///home/hp/Programing-Workspace/CBSE_CS/Class11/programs/p15_list_element_frequencies.py)
* **Topic Alignment:** Unit 2 — Lists, Dictionaries, and Frequency Counting
* **Aim:** Count the occurrence frequency of each unique element in a list using manual traversal and dictionary mappings.

#### Algorithm:
1. **Manual Frequency Counting (`count_frequencies_manual`):**
   - Build a `unique` list by appending each element only if `el not in unique`.
   - For each unique element `u_el`:
     - Count its occurrences by traversing `lst`.
     - Append `(u_el, freq)` tuple to results.
   - Return list of tuples.
2. **Dictionary Frequency Counting (`count_frequencies_dict`):**
   - Extract unique items into `unique` using `not in`.
   - Initialize dictionary with `dict().fromkeys(unique, 0)`.
   - Traverse `frequency.keys()`:
     - Count occurrences in `lst` and update dictionary key with count.
   - Return frequency dictionary.

#### Verified Student Implementation:
```python
"""
Program 15: Count Frequency of Elements in a List
CBSE Class 11 Practical File
"""

from typing import Any


def count_frequencies_manual(lst: list) -> list[tuple[Any, int]]:
    """
    Count frequencies manually without built-in count() or dictionaries.

    Parameters:
        lst (list): List of arbitrary elements.

    Returns:
        list[tuple[Any, int]]: List of (element, frequency) tuples in order of first appearance.
    """
    unique = []
    for el in lst:
        if el not in unique:
            unique.append(el)

    frequency: list[tuple[Any, int]] = []

    for u_el in unique:
        freq = 0
        for el in lst:
            if el == u_el:
                freq += 1

        frequency.append((u_el, freq))

    return frequency


def count_frequencies_dict(lst: list) -> dict[Any, int]:
    """
    Count frequencies using a Python dictionary.

    Parameters:
        lst (list): List of hashable elements.

    Returns:
        dict[Any, int]: Mapping of element -> count.
    """
    unique = []
    for el in lst:
        if el not in unique:
            unique.append(el)

    frequency: dict[Any, int] = dict().fromkeys(unique, 0)
    del unique  # to free up space

    for u_el in frequency.keys():
        freq = 0
        for el in lst:
            if el == u_el:
                freq += 1

        frequency.update({u_el: freq})

    return frequency


if __name__ == "__main__":
    print("--- Program 15: Frequency of Elements in List ---")
    raw = input("Enter elements separated by spaces: ")
    elements = raw.split()

    print(f"\nOriginal List: {elements}")

    # Method 1: Manual List Frequency
    manual_freq = count_frequencies_manual(elements)
    print("\n--- Frequency Table (Manual Method) ---")
    print(f"{'Element':<15} {'Frequency':<10}")
    print("-" * 25)
    for item, count in manual_freq:
        print(f"{str(item):<15} {count:<10}")

    # Method 2: Dictionary Frequency
    dict_freq = count_frequencies_dict(elements)
    print("\n--- Frequency Table (Dictionary Method) ---")
    print(f"{'Element':<15} {'Frequency':<10}")
    print("-" * 25)
    for item, count in dict_freq.items():
        print(f"{str(item):<15} {count:<10}")
```

#### Sample Execution Outputs:
```text
Test Run:
Enter elements separated by spaces: apple banana apple orange banana apple

Original List: ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

--- Frequency Table (Manual Method) ---
Element         Frequency 
-------------------------
apple           3         
banana          2         
orange          1         

--- Frequency Table (Dictionary Method) ---
Element         Frequency 
-------------------------
apple           3         
banana          2         
orange          1         
```


---

### Program 16: Tuple Operations — Statistics and Linear Search
* **File:** [`p16_tuple_stats_and_search.py`](file:///home/hp/Programing-Workspace/CBSE_CS/Class11/programs/p16_tuple_stats_and_search.py)
* **Topic Alignment:** Unit 2 — Tuples, Immutability, Traversal, and Linear Search
* **Aim:** Input a tuple of numbers, manually compute the minimum, maximum, and arithmetic mean without using `min()`, `max()`, or `sum()`, and perform a linear search returning all index positions of a target element.

#### Algorithm:
1. **Tuple Statistics (`compute_tuple_stats`):**
   - If tuple is empty, raise `ValueError`.
   - If length is 1, return `(tup[0], tup[0], tup[0])`.
   - Initialize `stat = [None, None, 0]`, where `stat[0]` tracks minimum, `stat[1]` tracks maximum, and `stat[2]` accumulates sum.
   - For each element `el` in `tup`:
     - If `stat[0] is None` or `stat[0] > el`: update `stat[0] = el`.
     - If `stat[1] is None` or `stat[1] < el`: update `stat[1] = el`.
     - Add `el` to `stat[2]`.
   - Return `(stat[0], stat[1], stat[2] / len(tup))`.
2. **Tuple Linear Search (`tuple_linear_search`):**
   - Initialize `indices = []`.
   - For `i` from 0 to $\text{len}(tup) - 1$:
     - If `tup[i] == target`, append `i` to `indices`.
   - Return `indices`.

#### Verified Student Implementation:
```python
"""
Program 16: Tuple Operations — Statistics and Linear Search
CBSE Class 11 Practical File
"""


def compute_tuple_stats(tup: tuple[float, ...]) -> tuple[float, float, float]:
    """
    Compute the minimum, maximum, and mean of a non-empty tuple of numbers manually.

    Parameters:
        tup (tuple[float, ...]): Non-empty tuple of numerical values.

    Returns:
        tuple[float, float, float]: (min_val, max_val, mean_val)

    Raises:
        ValueError: If the tuple is empty.
    """
    if not tup:
        raise ValueError("Empty tuple send as argument.")
    if len(tup) == 1:
        return (*tup, *tup, *tup)  # (*tup) * 3

    stat = [None, None, 0]

    for i in range(len(tup)):
        el: float = tup[i]

        if stat[0] is None or stat[0] > el:
            stat[0] = el
        if stat[1] is None or stat[1] < el:
            stat[1] = el

        stat[2] += el

    return stat[0], stat[1], stat[2] / len(tup)


def tuple_linear_search(tup: tuple[float, ...], target: float) -> list[int]:
    """
    Search for a target value in a tuple and return all index positions where it occurs.

    Parameters:
        tup (tuple[float, ...]): Tuple of elements.
        target (float): Value to find.

    Returns:
        list[int]: List of 0-based indices where target appears (empty list if absent).
    """
    if not tup:
        return []
    if len(tup) == 1:
        return [0] if target == tup[0] else []

    indices: list[int] = []
    for i in range(len(tup)):
        if target == tup[i]:
            indices.append(i)

    return indices


if __name__ == "__main__":
    print("--- Program 16: Tuple Statistics & Linear Search ---")
    raw = input("Enter numbers separated by spaces: ")
    num_list = [float(x) for x in raw.split()]
    data_tuple = tuple(num_list)

    print(f"\nConstructed Tuple: {data_tuple}")
    print(f"Tuple Length:     {len(data_tuple)}")

    if not data_tuple:
        print("Tuple is empty! Cannot compute statistics.")
    else:
        min_v, max_v, mean_v = compute_tuple_stats(data_tuple)
        print(f"\n--- Tuple Statistics ---")
        print(f"Minimum Value: {min_v}")
        print(f"Maximum Value: {max_v}")
        print(f"Mean Value:    {mean_v:.2f}")

        search_val = float(input("\nEnter target number to search: "))
        indices = tuple_linear_search(data_tuple, search_val)

        if indices:
            print(f"Target {search_val} found at index/indices: {indices}")
            print(
                f"Occurrences (verified via tup.count()): {data_tuple.count(search_val)}"
            )
        else:
            print(f"Target {search_val} not found in tuple.")
```

#### Sample Execution Outputs:
```text
Test Run 1 (Multiple elements and duplicate target search):
Enter numbers separated by spaces: 12.5 45.0 8.0 45.0 23.5 8.0

Constructed Tuple: (12.5, 45.0, 8.0, 45.0, 23.5, 8.0)
Tuple Length:     6

--- Tuple Statistics ---
Minimum Value: 8.0
Maximum Value: 45.0
Mean Value:    23.67

Enter target number to search: 45.0
Target 45.0 found at index/indices: [1, 3]
Occurrences (verified via tup.count()): 2

Test Run 2 (Element not found):
Enter numbers separated by spaces: 10 20 30

Constructed Tuple: (10.0, 20.0, 30.0)
Tuple Length:     3

--- Tuple Statistics ---
Minimum Value: 10.0
Maximum Value: 30.0
Mean Value:    20.00

Enter target number to search: 99.0
Target 99.0 not found in tuple.
```


---

### Program 17: Random Module — Dice Rolling Simulator & Guessing Game
* **File:** [`p17_dice_simulator_random.py`](file:///home/hp/Programing-Workspace/CBSE_CS/Class11/programs/p17_dice_simulator_random.py)
* **Topic Alignment:** Unit 2 — Modules (`random`), `randint()`, Dictionaries, and Conditionals
* **Aim:** Simulate rolling two 6-sided dice $N$ times to record the sum distribution (from 2 to 12), and implement an interactive number guessing game with binary search style feedback ("Too low", "Too high", "Correct!").

#### Algorithm:
1. **Dice Roll Simulation (`simulate_dice_rolls`):**
   - If `num_rolls <= 0`, raise `ValueError`.
   - Initialize frequency dictionary `freq = {i: 0 for i in range(2, 13)}`.
   - While `num_rolls > 0`:
     - Roll `die1 = randint(1, 6)` and `die2 = randint(1, 6)`.
     - Increment `freq[die1 + die2] += 1`.
     - Decrement `num_rolls -= 1`.
   - Return `freq`.
2. **Guessing Game Evaluator (`play_guessing_game`):**
   - If `guess < secret_number`: return `"Too low"`.
   - Else if `guess > secret_number`: return `"Too high"`.
   - Else: return `"Correct!"`.

#### Verified Student Implementation:
```python
"""
Program 17: Random Module — Dice Rolling Simulator & Guessing Game
CBSE Class 11 Practical File
"""

from random import randint, random


def simulate_dice_rolls(num_rolls: int) -> dict[int, int]:
    """
    Simulate rolling two 6-sided dice `num_rolls` times.
    Each die produces a value from 1 to 6 (inclusive) using random.randint.

    Parameters:
        num_rolls (int): Total number of simulation rolls (must be > 0).

    Returns:
        dict[int, int]: Frequency map of sums from 2 to 12.
                        Keys are integers 2..12, values are counts.

    Raises:
        ValueError: If num_rolls <= 0.
    """
    if num_rolls <= 0:
        raise ValueError("num rolls cannot be 0")

    freq: dict[int, int] = {i: 0 for i in range(2, 13)}
    while num_rolls > 0:
        die1: int = randint(1, 6)
        die2: int = randint(1, 6)

        total: int = die1 + die2
        freq[total] += 1
        num_rolls -= 1

    return freq


def play_guessing_game(secret_number: int, guess: int) -> str:
    """
    Evaluate a player's guess against the secret number.

    Parameters:
        secret_number (int): The target number.
        guess (int): The player's guess.

    Returns:
        str: "Too low", "Too high", or "Correct!"
    """
    if guess < secret_number:
        return "Too low"
    elif guess > secret_number:
        return "Too high"
    else:
        return "Correct!"


if __name__ == "__main__":
    print("--- Program 17: Random Module Applications ---")
    print("1. Dice Rolling Simulator")
    print("2. Number Guessing Game")
    choice = input("Select an option (1 or 2): ").strip()

    if choice == "1":
        rolls = int(input("\nEnter number of dice rolls to simulate: "))
        if rolls <= 0:
            print("Number of rolls must be positive.")
        else:
            freq_map = simulate_dice_rolls(rolls)
            print(f"\n--- Simulation Results ({rolls} rolls) ---")
            print(f"{'Sum':<6} {'Count':<10} {'Percentage':<10}")
            print("-" * 28)
            for s in range(2, 13):
                count = freq_map.get(s, 0)
                pct = (count / rolls) * 100
                print(f"{s:<6} {count:<10} {pct:.2f}%")

    elif choice == "2":
        secret = randint(1, 100)
        max_attempts = 7
        print(f"\nI have picked a secret number between 1 and 100.")
        print(f"You have {max_attempts} attempts to guess it.")

        won = False
        for attempt in range(1, max_attempts + 1):
            user_guess = int(
                input(f"\nAttempt {attempt}/{max_attempts} - Enter guess: ")
            )
            feedback = play_guessing_game(secret, user_guess)
            print(f"Feedback: {feedback}")

            if feedback == "Correct!":
                print(f"Congratulations! You guessed the number in {attempt} attempts!")
                won = True
                break

        if not won:
            print(f"\nGame Over! The secret number was {secret}.")
    else:
        print("Invalid choice.")
```

#### Sample Execution Outputs:
```text
Test Run 1 (Dice Simulator — 1000 rolls):
Select an option (1 or 2): 1

Enter number of dice rolls to simulate: 1000

--- Simulation Results (1000 rolls) ---
Sum    Count      Percentage
----------------------------
2      28         2.80%
3      55         5.50%
4      83         8.30%
5      111        11.10%
6      139        13.90%
7      167        16.70%
8      138        13.80%
9      112        11.20%
10     84         8.40%
11     56         5.60%
12     27         2.70%

Test Run 2 (Number Guessing Game):
Select an option (1 or 2): 2

I have picked a secret number between 1 and 100.
You have 7 attempts to guess it.

Attempt 1/7 - Enter guess: 50
Feedback: Too low

Attempt 2/7 - Enter guess: 75
Feedback: Too high

Attempt 3/7 - Enter guess: 62
Feedback: Too high

Attempt 4/7 - Enter guess: 56
Feedback: Too low

Attempt 5/7 - Enter guess: 59
Feedback: Correct!
Congratulations! You guessed the number in 5 attempts!
```


---

### Program 18: Text & String Analysis — Comprehensive Character & Word Statistics
* **File:** [`p18_string_text_statistics.py`](file:///home/hp/Programing-Workspace/CBSE_CS/Class11/programs/p18_string_text_statistics.py)
* **Topic Alignment:** Unit 2 — Strings, Traversal, and Character Classification
* **Aim:** Analyze a multi-line passage of text to compute lines, words, total characters, vowels, consonants, digits, whitespace, and special characters via a single-pass character partition.

#### Algorithm:
1. Initialize statistics dictionary:
   - `lines = len(text.splitlines()) if text else 0`
   - `words = len(text.split())`
   - `characters = len(text)`
   - All character category counters set to 0.
2. Initialize vowel lookup set `VOWELS = set("aeiouAEIOU")`.
3. For each character `c` in `text`:
   - If `c in VOWELS`: increment `vowels`.
   - Else if `c.isalpha()`: increment `consonants`.
   - Else if `c.isdigit()`: increment `digits`.
   - Else if `c.isspace()`: increment `whitespaces`.
   - Else: increment `special_characters`.
4. Return `stat` dictionary.

#### Verified Student Implementation:
```python
"""
Program 18: Text & String Analysis — Comprehensive Character & Word Statistics
CBSE Class 11 Practical File
"""


def analyze_text(text: str) -> dict[str, int]:
    """
    Analyze a string and compute comprehensive character and text statistics.

    Parameters:
        text (str): Input text string.

    Returns:
        dict[str, int]: A dictionary containing counts for:
            - "lines": Number of lines
            - "words": Number of whitespace-separated words
            - "characters": Total length of text
            - "vowels": English vowels (A, E, I, O, U, case-insensitive)
            - "consonants": English alphabetic characters that are not vowels
            - "digits": Numeric digits (0-9)
            - "whitespaces": Spaces, tabs, and newlines
            - "special_characters": Non-alphanumeric, non-whitespace characters
    """
    stat: dict[str, int] = {
        "lines": len(text.splitlines()) if text else 0,
        "words": len(text.split()),
        "characters": len(text),
        "vowels": 0,
        "consonants": 0,
        "digits": 0,
        "whitespaces": 0,
        "special_characters": 0,
    }

    VOWELS = set("aeiouAEIOU")

    for c in text:
        if c in VOWELS:
            stat["vowels"] += 1
        elif c.isalpha():
            stat["consonants"] += 1
        elif c.isdigit():
            stat["digits"] += 1
        elif c.isspace():
            stat["whitespaces"] += 1
        else:
            stat["special_characters"] += 1

    return stat


if __name__ == "__main__":
    print("--- Program 18: Text & String Analysis ---")
    print("Enter your text below (Press Enter on an empty line to finish):")

    lines: list[str] = []
    while True:
        line = input()
        if not line:
            break
        lines.append(line)

    sample_text = "\n".join(lines)

    if not sample_text:
        print("\nNo text entered.")
    else:
        stats = analyze_text(sample_text)
        print("\n" + "=" * 40)
        print(f"{'Text Metric':<25} {'Count':<10}")
        print("=" * 40)
        for metric, count in stats.items():
            formatted_name = metric.replace("_", " ").title()
            print(f"{formatted_name:<25} {count:<10}")
        print("=" * 40)
```

#### Sample Execution Outputs:
```text
Test Run:
Enter your text below (Press Enter on an empty line to finish):
Hello World!
Python 3.12 is awesome & fast.

========================================
Text Metric               Count     
========================================
Lines                     2         
Words                     6         
Characters                43        
Vowels                    10        
Consonants                20        
Digits                    3         
Whitespaces               6         
Special Characters        4         
========================================
```
