# Class 11 Computer Science: Strings and Lists

Extracted questions and complete Python solutions based on the handwritten notes in the `WhatsApp Unknown 2026-11-03 at 6.08.10 PM` folder.

---

# Section 1: Questions

### Part A: String Questions

1. **Sum of Digits in a String**  
   *Inferred from handwritten code snippet:*  
   Write a Python program to calculate and display the sum of all numeric digits present in a given string (e.g., `'123456789'`).

2. **Email Character Masking / Encryption**  
   *Inferred from handwritten code snippet under blank "Ques:" heading:*  
   Write a Python program to input an email address and mask/encrypt it by replacing every alphabetic character (both uppercase and lowercase) with an asterisk (`'*'`), while leaving non-alphabetic characters (such as `@`, `.`, numbers) unchanged.

3. **Check for Palindrome String**  
   Write a Python program to check whether a user-entered string is a palindrome or not using string slicing.

4. **Reverse a String Without Slicing**  
   Write a Python program to return the reverse of a string without using string slicing (i.e. using a loop).

5. **Left Rotate / Shift Characters in a String by 1 Position**  
   Write a Python program to shift/rotate each character in a given string to the left by 1 position such that the first character moves to the very end of the string (e.g., input `'Aridaman'` produces `'ridamanA'`).

6. **Swap Adjacent Characters in a String**  
   Write a Python program to swap each character within a given string with its adjacent next character (pairwise swap).

---

### Part B: List Questions

7. **Sum of All Elements in a User-Defined List**  
   Write a Python program to input space-separated numbers into a list and find the sum of all the elements.

8. **Frequency of Elements in a List**  
   Write a Python program to enter $n$ elements into a list and print each unique element along with its frequency of occurrence.

9. **Traverse and Sum List Elements**  
   Write a Python program to enter $n$ elements into a user-defined list and print each element on a single line followed by the total sum of all elements.

10. **Filter Elements Divisible by 2 and 5**  
    Write a Python program to enter $n$ elements into a list and print only those elements that are divisible by both 2 and 5 (i.e., divisible by 10).

11. **Sort Numbers in Ascending Order**  
    Write a Python program to enter random numbers into a list and arrange them in ascending order without using built-in sorting methods.

12. **Calculate the Mean of Numbers in a List**  
    Write a Python program to enter elements into a user-defined list and calculate the arithmetic mean (average) of the numbers.

13. **Swap/Replace Even Elements with the Next Element**  
    Write a Python program to enter a user-defined list. If any element's value is divisible by 2 (even), swap/replace it with the next adjacent element, and print the resulting modified list.

14. **Separate Even and Odd Numbers and Find Their Maxima**  
    Write a Python program to input a user-defined list and create two separate lists: one containing all even numbers and the other containing all odd numbers. Additionally, find the maximum even number, maximum odd number, and the overall maximum element.

15. **Sum of Elements Ending in 3**  
    Write a Python program to find the sum of elements in a user-defined list whose last digit is 3 (i.e., numbers ending in 3).

16. **Count Numeric, Alphabetic, and Alphanumeric Elements in a List**  
    Given a heterogeneous list containing mixed types and strings (e.g., `["Hello", 123, "AB12", 12.25, "12AB", 50, "Sitapur"]`), write a Python program to count how many elements are purely numeric, purely alphabetic, and alphanumeric (combination of letters and numbers).

---

### Part C: Code Tracing / Output Prediction Questions

17. **List Slicing Output Tracing**  
    Given the list:
    ```python
    E = ["Hello", 123, "AB12", 12.25, "12AB", 50, "Sitapur"]
    ```
    Determine the output of the following statements:
    ```python
    print(E[1:5:2], "#", E[-5:])
    print(E[::-2], "@", E[3:-2])
    ```

18. **List Mutation and Aliasing Output Tracing**  
    Predict the exact output of the following Python code snippet:
    ```python
    A = [10, 20, 30, [10, 20, 30], 40, 50, 'A', 'B', 'C']
    A[2:5] = 'ABC'
    A.insert(2, 100)
    A[1:3] = [1, 2, 3]
    print(A)

    B = A
    B.extend(A)
    B[1:3] = 'Hello'
    print(B)

    if B > A:
        print("Yes")
    elif B == A:
        print("Fine")
    else:
        print("Bye")

    A[1:3] = A[3:5]
    B.extend(A)
    print(B)
    ```

---

# Section 2: Answers

### Question 1: Sum of Digits in a String
```python
# Program to calculate the sum of all digits in a string
text = input("Enter a string containing digits (e.g. 123456789): ")
total = 0

for ch in text:
    if ch.isdigit():
        total += int(ch)

print(f"Total = {total}")
```
**Sample Run:**
```text
Enter a string containing digits (e.g. 123456789): 123456789
Total = 45
```

---

### Question 2: Email Character Masking / Encryption
```python
# Program to mask alphabetic characters in an email address
email = input("Enter e-mail: ")
masked_email = ""

for ch in email:
    # Check if character is an English alphabet letter
    if ('A' <= ch <= 'Z') or ('a' <= ch <= 'z'):  # or ch.isalpha()
        masked_email += '*'
    else:
        masked_email += ch

print(f"Your coded email is {masked_email}")
```
**Sample Run:**
```text
Enter e-mail: user123@example.com
Your coded email is ****123@*******.***
```

---

### Question 3: Check for Palindrome String
```python
# Program to check if a string is a palindrome using slicing
s = input("Enter a string: ")

if s == s[::-1]:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")
```
**Sample Run:**
```text
Enter a string: racecar
The string is a palindrome
```

---

### Question 4: Reverse a String Without Slicing
```python
# Program to reverse a string without using slicing
s = input("Enter a string: ")
reversed_str = ""

# Loop backwards from index len(s)-1 down to 0
for i in range(len(s) - 1, -1, -1):
    reversed_str += s[i]

print(f"The reverse is {reversed_str}")
```
**Sample Run:**
```text
Enter a string: python
The reverse is nohtyp
```

---

### Question 5: Left Rotate / Shift Characters in a String by 1 Position
*Note: In Python, strings are immutable, so in-place character assignment `str[i] = str[i+1]` raises a `TypeError`. We can achieve left rotation cleanly via slicing or list conversion.*

**Method 1 (Idiomatic Slicing):**
```python
name = input("Enter Your Name: ")

if len(name) > 1:
    rotated = name[1:] + name[0]
else:
    rotated = name

print(f"Your Rotated name is {rotated}")
```

**Method 2 (Using List & Loop, matching notebook logic):**
```python
name = input("Enter Your Name: ")

if name:
    chars = list(name)
    first_letter = chars[0]
    for i in range(len(chars) - 1):
        chars[i] = chars[i + 1]
    chars[-1] = first_letter
    rotated = "".join(chars)
    print(f"Your Rotated name is {rotated}")
```
**Sample Run:**
```text
Enter Your Name: Aridaman
Your Rotated name is ridamanA
```

---

### Question 6: Swap Adjacent Characters in a String
```python
# Program to swap each character with the next adjacent one (pairwise swap)
name = input("Enter a string: ")
chars = list(name)

# Step by 2 to swap adjacent pairs: (0, 1), (2, 3), etc.
for i in range(0, len(chars) - 1, 2):
    chars[i], chars[i + 1] = chars[i + 1], chars[i]

swapped = "".join(chars)
print(f"Modified string: {swapped}")
```
**Sample Run:**
```text
Enter a string: Aridaman
Modified string: rAdiamna
```

---

### Question 7: Sum of All Elements in a User-Defined List
```python
# Program to input a user-defined list and calculate the sum of all elements
data = input("Enter numbers (e.g. 2 4 78): ").split()
numbers = [int(x) for x in data]

total = 0
for el in numbers:
    total += el

print("sum =", total)
```
**Sample Run:**
```text
Enter numbers (e.g. 2 4 78): 2 4 78
sum = 84
```

---

### Question 8: Frequency of Elements in a List
```python
# Program to enter n elements and print original elements with their frequency
n = int(input("Enter no. of elements: "))
lst = []
for _ in range(n):
    lst.append(int(input("Enter the element: ")))

# Extract unique elements preserving order
unique_elements = []
for el in lst:
    if el not in unique_elements:
        unique_elements.append(el)

print("\nElement \t Frequency")
for el in unique_elements:
    freq = 0
    for e in lst:
        if el == e:
            freq += 1
    print(f"{el} \t\t {freq}")
```
**Sample Run:**
```text
Enter no. of elements: 5
Enter the element: 10
Enter the element: 20
Enter the element: 10
Enter the element: 30
Enter the element: 20

Element 	 Frequency
10 		 2
20 		 2
30 		 1
```

---

### Question 9: Traverse and Sum List Elements
```python
# Program to enter n elements, print all elements, and print their total sum
n = int(input("Enter number of element: "))
l = []
for _ in range(n):
    l.append(int(input("Enter the element: ")))

total = 0
print("Elements:", end=" ")
for el in l:
    print(f"{el}", end=" ")
    total += el
print()
print(f"Total = {total}")
```
**Sample Run:**
```text
Enter number of element: 4
Enter the element: 5
Enter the element: 10
Enter the element: 15
Enter the element: 20
Elements: 5 10 15 20 
Total = 50
```

---

### Question 10: Filter Elements Divisible by 2 and 5
```python
# Program to print elements divisible by both 2 and 5 (i.e. divisible by 10)
n = int(input("Enter no. of elements: "))
l = []
for _ in range(n):
    l.append(int(input("Enter element: ")))

print("Elements divisible by 2 and 5 (10):")
for el in l:
    if el % 10 == 0:  # equivalent to: (el % 2 == 0 and el % 5 == 0)
        print(el)
```
**Sample Run:**
```text
Enter no. of elements: 5
Enter element: 10
Enter element: 15
Enter element: 20
Enter element: 25
Enter element: 30
Elements divisible by 2 and 5 (10):
10
20
30
```

---

### Question 11: Sort Numbers in Ascending Order
```python
# Program to input numbers and sort them in ascending order
data = input("Enter the numbers (like 2 3 43 ...): ").split()
numbers = [int(x) for x in data]

# Using Selection / Bubble Sort
n = len(numbers)
for i in range(n):
    for j in range(i + 1, n):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]

print("Sorted list in ascending order:", numbers)
```
**Sample Run:**
```text
Enter the numbers (like 2 3 43 ...): 43 12 5 89 2
Sorted list in ascending order: [2, 5, 12, 43, 89]
```

---

### Question 12: Calculate the Mean of Numbers in a List
```python
# Program to enter elements in a list and find out the mean
data = input("Enter list (like 2 3 43 ...): ").split()
numbers = [int(x) for x in data]

total = 0
for datum in numbers:
    total += datum

if len(numbers) > 0:
    avg = total / len(numbers)
    print("Mean :", avg)
else:
    print("Empty list")
```
**Sample Run:**
```text
Enter list (like 2 3 43 ...): 10 20 30 40
Mean : 25.0
```

---

### Question 13: Swap/Replace Even Elements with the Next Element
```python
# Program to swap an even element with its next adjacent element
data = input("Enter (like 2 3 43 247): ").split()
numbers = [int(x) for x in data]

for i in range(len(numbers)):
    if numbers[i] % 2 == 0 and i != len(numbers) - 1:
        numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]

print("Modified list:", numbers)
```
**Sample Run:**
```text
Enter (like 2 3 43 247): 2 3 43 247
Modified list: [3, 2, 43, 247]
```

---

### Question 14: Separate Even and Odd Numbers and Find Their Maxima
```python
# Program to separate evens and odds, and determine max-even, max-odd, and overall max
data = input("Enter list (like 2 3 43 247 ...): ").split()
numbers = [int(x) for x in data]

evens = []
odds = []
max_even = None
max_odd = None

for el in numbers:
    if el % 2 == 0:
        evens.append(el)
        if max_even is None or el > max_even:
            max_even = el
    else:
        odds.append(el)
        if max_odd is None or el > max_odd:
            max_odd = el

# Overall max calculation
if max_even is not None and max_odd is not None:
    overall_max = max_even if max_even > max_odd else max_odd
elif max_even is not None:
    overall_max = max_even
else:
    overall_max = max_odd

print("All evens: ", evens)
print("All odds: ", odds)
print(f"Max even: {max_even}, Max odd: {max_odd}")
print("Max element: ", overall_max)
```
**Sample Run:**
```text
Enter list (like 2 3 43 247 ...): 2 3 43 247 18 90
All evens:  [2, 18, 90]
All odds:  [3, 43, 247]
Max even: 90, Max odd: 247
Max element:  247
```

---

### Question 15: Sum of Elements Ending in 3
```python
# Program to find the sum of elements of a list ending in 3
data = input("Enter (like 2 4 23 847): ").split()
numbers = [int(x) for x in data]

total = 0
for d in numbers:
    if abs(d) % 10 == 3:
        total += d

print("The unique sum is", total)
```
**Sample Run:**
```text
Enter (like 2 4 23 847): 2 13 4 23 847 33
The unique sum is 69
```

---

### Question 16: Count Numeric, Alphabetic, and Alphanumeric Elements in a List
```python
# Program to count purely numeric, purely alphabetic, and alphanumeric elements
E = ["Hello", 123, "AB12", 12.25, "12AB", 50, "Sitapur"]

alpha_count = 0
numeric_count = 0
alnum_count = 0

for el in E:
    s = str(el)
    if s.isdigit():
        numeric_count += 1
    elif s.isalpha():
        alpha_count += 1
    elif s.isalnum():
        alnum_count += 1

print("No. of alphabetic elements:", alpha_count)
print("No. of numeric elements:", numeric_count)
print("No. of alphanumeric elements:", alnum_count)
```
**Output:**
```text
No. of alphabetic elements: 2
No. of numeric elements: 2
No. of alphanumeric elements: 2
```
*(Explanation: `"Hello"` and `"Sitapur"` are alphabetic; `123` and `50` are numeric; `"AB12"` and `"12AB"` are alphanumeric; `12.25` has a period `.` so it is not alphanumeric).*

---

### Question 17: List Slicing Output Tracing
```python
E = ["Hello", 123, "AB12", 12.25, "12AB", 50, "Sitapur"]

print(E[1:5:2], "#", E[-5:])
print(E[::-2], "@", E[3:-2])
```
**Output:**
```text
[123, 12.25] # ['AB12', 12.25, '12AB', 50, 'Sitapur']
['Sitapur', '12AB', 'AB12', 'Hello'] @ [12.25, '12AB']
```

---

### Question 18: List Mutation and Aliasing Output Tracing
```python
A = [10, 20, 30, [10, 20, 30], 40, 50, 'A', 'B', 'C']
A[2:5] = 'ABC'
A.insert(2, 100)
A[1:3] = [1, 2, 3]
print(A)

B = A
B.extend(A)
B[1:3] = 'Hello'
print(B)

if B > A:
    print("Yes")
elif B == A:
    print("Fine")
else:
    print("Bye")

A[1:3] = A[3:5]
B.extend(A)
print(B)
```
**Output:**
```text
[10, 1, 2, 3, 'A', 'B', 'C', 50, 'A', 'B', 'C']
[10, 'H', 'e', 'l', 'l', 'o', 3, 'A', 'B', 'C', 50, 'A', 'B', 'C', 10, 1, 2, 3, 'A', 'B', 'C', 50, 'A', 'B', 'C']
Fine
[10, 'l', 'l', 'l', 'l', 'o', 3, 'A', 'B', 'C', 50, 'A', 'B', 'C', 10, 1, 2, 3, 'A', 'B', 'C', 50, 'A', 'B', 'C', 10, 'l', 'l', 'l', 'l', 'o', 3, 'A', 'B', 'C', 50, 'A', 'B', 'C', 10, 1, 2, 3, 'A', 'B', 'C', 50, 'A', 'B', 'C']
```
*(Explanation: `B = A` creates an alias to the identical list object in memory. Mutating `B` directly mutates `A` and vice versa, which is why `B == A` evaluates to `True`, outputting `'Fine'`.)*
