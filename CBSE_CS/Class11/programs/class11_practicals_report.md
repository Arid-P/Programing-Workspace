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
