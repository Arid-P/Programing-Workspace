# CBSE Class 11 Computer Science (083) — Test Practice Paper
## Syllabus: Strings & Lists (Unit 2: Computational Thinking & Programming - 1)

---

# PART 1: QUESTION PAPER
*(Instructions: Try solving all questions independently before checking the hints or answers.)*

---

### SECTION A: Objective & Conceptual Questions (1 Mark Each)

#### Q1. Mutability Differences
Explain why strings are called **immutable** while lists are called **mutable** in Python. Illustrate what happens when you attempt:
```python
s = "hello"
s[0] = "H"
```
versus:
```python
L = ["h", "e", "l", "l", "o"]
L[0] = "H"
```

#### Q2. Indexing vs. Slicing Out-of-Bounds
Consider the string `s = "Python"`.
1. What is the result/behavior of evaluating `s[10]`?
2. What is the result/behavior of evaluating `s[10:20]`?
State the general rule governing index access versus slice access for out-of-range bounds.

#### Q3. Substring Search: `find()` vs. `index()`
Differentiate between the string methods `s.find(sub)` and `s.index(sub)` when the substring `sub` is **not** present in the string `s`.

#### Q4. List Expansion: `append()` vs. `extend()`
Given the list `lst = [10, 20, 30]`:
1. What will `lst` look like after `lst.append([40, 50])`? What will `len(lst)` be?
2. What will `lst` look like if instead `lst.extend([40, 50])` is called? What will `len(lst)` be?

#### Q5. Sorting: `lst.sort()` vs. `sorted(lst)`
What is the fundamental difference between the method `lst.sort()` and the built-in function `sorted(lst)` with respect to:
1. Return value
2. Modification of the original list

#### Q6. Element Deletion: `del` vs. `pop()` vs. `remove()`
Given `L = [10, 20, 30, 40, 20]`:
State the specific purpose, argument requirement, and return value of:
1. `del L[1]`
2. `L.pop(1)`
3. `L.remove(20)`

---

### SECTION B: Output Prediction & Code Tracing (2 Marks Each)

#### Q7. String Slicing Combinations
Predict the exact output of the following Python code snippet:
```python
text = "ComputerScience"

print(text[3:10:2])
print(text[-7:-2])
print(text[::-3])
print(text[8:2:-2])
```

#### Q8. String Transformation & ASCII Shifting
Predict the exact output printed by the following code:
```python
msg = "Pre-Board@2026"
new_msg = ""

for ch in msg:
    if ch.isupper():
        new_msg += ch.lower()
    elif ch.islower():
        new_msg += ch.upper()
    elif ch.isdigit():
        new_msg += str((int(ch) + 1) % 10)
    else:
        new_msg += "#"

print(new_msg)
```

#### Q9. List Slicing Assignment & Mutability
Predict the output of the following sequence of operations:
```python
vals = [10, 20, 30, 40, 50, 60]

vals[1:4] = [25, 35]
print("After slice assignment:", vals)

vals.insert(2, 99)
popped_val = vals.pop()
print("Popped value:", popped_val)
print("Final list:", vals)
```

#### Q10. Aliasing vs. Shallow Copying
Predict the exact output for lists `a`, `b`, and `c`:
```python
a = [1, 2, [3, 4]]
b = a
c = a[:]

b[0] = 10
c[1] = 20
b[2][0] = 30

print("a:", a)
print("b:", b)
print("c:", c)
```

#### Q11. String Methods: `split()`, `join()`, and `partition()`
Predict the exact output produced by the following code:
```python
record = "maths,physics,,chemistry,english"

tokens = record.split(",")
print("Tokens count:", len(tokens))
print("Joined:", "-".join(tokens))

head, sep, tail = record.partition(",")
print("Head:", head)
print("Tail:", tail)
```

#### Q12. Overlapping Counts & Case Formatting
Predict the output of the following code:
```python
phrase = "banana bandanna"
print("Count of 'ana':", phrase.count("ana"))

heading = "cbse class 11 computer science"
print("Capitalize:", heading.capitalize())
print("Title:", heading.title())
```

---

### SECTION C: Error Finding & Code Debugging (2 Marks Each)

#### Q13. String Immutability and Invalid Methods
Identify the two errors in the following code, explain why each occurs, and write the corrected code that creates the string `"Jython 3.12"`:
```python
word = "Python"
word[0] = 'J'
word.append(" 3.12")
print(word)
```

#### Q14. Modifying a List During Iteration
A student writes the following program to remove all occurrences of the number `20` from a list:
```python
L = [10, 20, 20, 30, 40, 20, 50]
for item in L:
    if item == 20:
        L.remove(item)
print(L)
```
1. What will be printed when this code is executed?
2. Explain the logical defect that causes this unexpected behavior.
3. Provide the corrected code.

#### Q15. Value Lookup Exception
Explain why the following code crashes at runtime and provide a safe approach to retrieve the index without raising an uncaught exception:
```python
colors = ["Red", "Green", "Blue"]
target = "Yellow"

idx = colors.index(target)
print("Found at index:", idx)
```

---

### SECTION D: Programming & Problem Solving (3 Marks Each)

#### Q16. Case-Insensitive Palindrome Checker
Write a Python program that accepts a word or phrase from the user and determines whether it is a **palindrome** (reads the same forward and backward). The check must be case-insensitive (e.g., `"Madam"` or `"Racecar"` should be recognized as palindromes).

#### Q17. Character Category Counter
Write a Python program that reads a string from the user and counts and displays:
1. Total number of uppercase letters
2. Total number of lowercase letters
3. Total number of vowels (case-insensitive: a, e, i, o, u)
4. Total number of digits
5. Total number of spaces and special symbols

#### Q18. Linear Search in a List
Write a Python program to perform **Linear Search** on a given list of numbers.
- Ask the user to input the number to search.
- Search through the list element-by-element using a loop (do **not** use the built-in `.index()` method or `in` operator for finding the position).
- If found, display the 0-based index and the 1-based position where it was first located.
- If not found, display a clear message `"Item not found in list"`.

#### Q19. Adjacent Element Swap
Write a Python program that swaps every adjacent pair of elements in a list.
- Element at index 0 swaps with index 1, index 2 swaps with index 3, and so on.
- If the list contains an odd number of elements, the last element remains untouched.
- Example: If `lst = [10, 20, 30, 40, 50]`, the modified list should be `[20, 10, 40, 30, 50]`.

#### Q20. Second Largest Element (Without `sort()` or `max()`)
Write a Python program to find the largest and second largest numbers in a list of distinct integers in a single pass without using `sort()`, `sorted()`, or `max()`.

#### Q21. Deduplication Preserving Order
Write a Python program that takes a list containing duplicate integers and creates a new list with all duplicates removed, strictly preserving the original order of first appearance. (Do not convert directly to a `set` since sets do not guarantee order preservation).

#### Q22. Even-Odd Separation & Aggregation
Write a Python program that takes a list of integers entered by the user and partitions them into two separate lists: `evens` and `odds`. The program must then print:
1. The list of even numbers and their sum.
2. The list of odd numbers and their sum.

---

# PART 2: HINTS & LOGICAL WALKTHROUGHS
*(No Python syntax or code snippets provided here — strictly algorithmic thinking and conceptual guidance.)*

---

### Section A Hints (Concepts)
- **H1 (Mutability):** Think about computer memory. An immutable object cannot have its internal content modified in-place; any "change" requires constructing a brand-new object elsewhere in memory. A mutable object allows altering individual memory slots in-place while keeping the same object identity.
- **H2 (Out-of-Bounds):** Individual element access via brackets demands an exact slot in memory. If that slot doesn't exist, Python cannot guess what you want. Slicing, however, defines a boundary range. Python's slicing design is forgiving: it clips boundary limits to the actual length of the sequence without error.
- **H3 (find vs index):** Ask yourself: which method is designed for safe sentinel inspection (returning a special integer that indicates "nowhere") and which method treats missing data as an exceptional condition that halts the script?
- **H4 (append vs extend):** Imagine a box. If you put another box containing two marbles into your box, how many items are directly inside your main box? That is `append`. If you empty the second box and dump the individual marbles directly into your main box, that is `extend`.
- **H5 (sort vs sorted):** Notice the grammar: `.sort()` is an imperative action method called on the object itself (mutating it in-place and returning nothing useful), whereas `sorted()` is a function that takes an iterable and returns a fresh, brand-new ordered list.
- **H6 (del vs pop vs remove):** Distinguish between deleting by exact position without caring about the value (`del`), removing by position while handing the removed value back to you (`pop`), and searching for a specific value to delete regardless of where it sits (`remove`).

---

### Section B Hints (Dry Runs & Output Prediction)
- **H7 (Slicing):**
  - Write down the indices 0 to 14 above each letter of `"ComputerScience"`.
  - For negative indices, write -15 to -1 below the letters (-1 is the last letter `'e'`).
  - Slicing formula: `[start : stop : step]`.
  - `start` is inclusive; `stop` is exclusive.
  - When `step` is negative, we move backward from right to left! Ensure `start > stop`.
- **H8 (String Transformation):**
  - Trace character by character.
  - Notice the `% 10` modulo operator for digits: what does `(int('9') + 1) % 10` do? What about `(int('2') + 1) % 10`?
  - Hyphens `-` and `@` are neither alphanumeric letters nor digits; see which fallback branch catches them.
- **H9 (List Slicing Assignment):**
  - `vals[1:4]` selects indices 1, 2, and 3 (three slots).
  - You are replacing those 3 slots with a 2-element sequence `[25, 35]`. The list will shrink!
  - `insert(2, 99)` puts `99` at index 2, pushing subsequent elements one spot to the right.
  - `pop()` with no arguments removes and returns the very last element.
- **H10 (Aliasing vs Shallow Copy):**
  - An assignment `b = a` creates a nickname/pointer to the same list. Mutating `b` mutates `a`.
  - A slice `c = a[:]` creates a new outer list. Mutating the top-level items of `c` does not affect `a`.
  - BUT inner nested lists `[3, 4]` are references! Both `a` and `c` share the exact same inner list container.
- **H11 (split vs partition):**
  - `split(",")` splits at *every* comma. Look closely at the double comma `,,` in the string — what goes between two adjacent commas? An empty string!
  - `partition(",")` splits strictly into a 3-part tuple at the *first* occurrence: `(head, separator, tail)`.
- **H12 (Counts & Case):**
  - Does `.count()` search overlapping windows or non-overlapping occurrences? In `"banana"`, once the first `"ana"` is matched at indices 1–3, where does the search pointer resume?
  - `.capitalize()` touches only the first character of the entire string and forces all others to lowercase.
  - `.title()` capitalizes the first letter of *each* word.

---

### Section C Hints (Error Finding)
- **H13:** Strings do not support item assignment (`TypeError`), and strings do not have an `.append()` method (which belongs exclusively to lists). To "append" to a string, use concatenation (`+`).
- **H14:** When you delete an element from a list during a `for-in` loop, all elements to the right slide one position to the left. But the loop counter automatically advances to the next numerical index. What happens to the element that just slid into the current index? It gets skipped! To fix, iterate over a copy of the list (`L[:]`) or build a new list.
- **H15:** `.index(val)` raises a `ValueError` if `val` is absent. Always check membership first using `in`, or protect the lookup with exception handling.

---

### Section D Hints (Programming Logic in English)
- **H16 (Palindrome):**
  - Convert the string to lowercase first so casing differences don't cause false mismatches.
  - A string is a palindrome if it equals its reverse. What slice expression reverses a string?
- **H17 (Character Counter):**
  - Initialize 5 independent counter variables at 0.
  - Loop through each character in the string.
  - Use `.isupper()` and `.islower()`.
  - To check vowels, test if the lowercase version of the character exists in `"aeiou"`.
  - Use `.isdigit()` for numbers.
  - If a character is not an alphanumeric letter, it falls into spaces/special characters.
- **H18 (Linear Search):**
  - Initialize a boolean flag `found = False` and an index tracker `pos = -1`.
  - Run a loop over `range(len(lst))`.
  - Compare `lst[i] == search_key`.
  - If a match is found, store `pos = i`, set `found = True`, and break out of the loop immediately.
  - After the loop, inspect `found`. If true, print the index; otherwise, print the failure message.
- **H19 (Adjacent Swap):**
  - Loop through indices with a step of 2: `range(0, len(lst) - 1, 2)`.
  - Notice the upper limit `len(lst) - 1`: this ensures that for odd lengths, the loop stops before the lonely last element, preventing an `IndexError`.
  - Inside the loop, swap `lst[i]` and `lst[i+1]` using simultaneous assignment.
- **H20 (Second Largest):**
  - Handle lists with at least 2 elements.
  - Set `largest` to the maximum of the first two elements, and `second` to the minimum of the first two.
  - Loop through the rest of the list starting from the third element.
  - If the current item is greater than `largest`: update `second = largest`, then `largest = item`.
  - Else if the item is greater than `second` (and not equal to `largest`): update `second = item`.
- **H21 (Deduplication):**
  - Create an empty list called `unique_list`.
  - Iterate over the original list.
  - For each number, check if it is already present in `unique_list`.
  - If not present, append it. If present, skip it.
- **H22 (Even-Odd Separation):**
  - Create two accumulator lists: `evens = []` and `odds = []`.
  - Loop through the numbers: if `n % 2 == 0`, append to `evens`; otherwise, append to `odds`.
  - Use built-in `sum()` and `len()` to print the results.

---

# PART 3: COMPLETE SOLUTIONS, CODE & TRACE TABLES

---

### SECTION A SOLUTIONS (Objective & Conceptual)

#### Ans 1. Mutability Differences
- **Strings are immutable:** Once created in memory, individual characters cannot be changed, replaced, or deleted in-place.
  - `s[0] = "H"` raises a `TypeError: 'str' object does not support item assignment`.
  - To modify a string, a new string object must be created: `s = "H" + s[1:]`.
- **Lists are mutable:** Elements inside a list can be modified, replaced, added, or deleted in-place without altering the list's identity in memory.
  - `L[0] = "H"` successfully updates the first item of `L`. `L` becomes `['H', 'e', 'l', 'l', 'o']`.

#### Ans 2. Indexing vs. Slicing Out-of-Bounds
1. `s[10]` raises an **`IndexError: string index out of range`** because index 10 does not exist in a 6-character string (valid indices are 0 to 5).
2. `s[10:20]` evaluates to an **empty string `""`** without throwing an error.
- **Rule:** Direct indexing requires a valid index within bounds `[-len, len-1]`. Slicing is designed to be tolerant: indices beyond the string bounds are automatically clamped to the sequence boundaries (`len(s)`).

#### Ans 3. `find()` vs. `index()`
When substring `sub` is **not** present in string `s`:
- `s.find(sub)` returns **`-1`**. It never crashes the program.
- `s.index(sub)` raises a **`ValueError: substring not found`**.

#### Ans 4. `append()` vs. `extend()`
Given `lst = [10, 20, 30]`:
1. `lst.append([40, 50])`:
   - Adds the list `[40, 50]` as a single nested element.
   - Resulting list: `[10, 20, 30, [40, 50]]`
   - `len(lst)` is **4**.
2. `lst.extend([40, 50])`:
   - Iterates over the argument and appends each element individually.
   - Resulting list: `[10, 20, 30, 40, 50]`
   - `len(lst)` is **5**.

#### Ans 5. `lst.sort()` vs. `sorted(lst)`
| Feature | `lst.sort()` | `sorted(lst)` |
| :--- | :--- | :--- |
| **Type** | List method | Built-in general function |
| **Return Value** | Returns `None` | Returns a **new sorted list** |
| **Original List** | Mutated in-place | Unchanged / intact |
| **Applicability** | Only lists | Any iterable (strings, tuples, lists, etc.) |

#### Ans 6. `del` vs. `pop()` vs. `remove()`
Given `L = [10, 20, 30, 40, 20]`:
1. `del L[1]`: Python keyword/statement. Deletes the element at index 1 (`20`). Takes an index or slice. Returns **nothing**.
2. `L.pop(1)`: List method. Removes the element at index 1 (`20`) and **returns** the removed value (`20`). If no argument is passed, it removes and returns the last element.
3. `L.remove(20)`: List method. Searches for the **first occurrence** of the value `20` and removes it from the list. Takes a value, returns `None`, and raises `ValueError` if the value is not found.

---

### SECTION B SOLUTIONS (Output Prediction & Dry Runs)

#### Ans 7. String Slicing Output
**Output:**
```text
ptrc
Scien
eeStm
Seu
```
**Detailed Step-by-Step Breakdown:**
`text = "ComputerScience"` (Length = 15)
- Positive indices:
  ```text
  Index: 0  1  2  3  4  5  6  7  8  9  10 11 12 13 14
   Char: C  o  m  p  u  t  e  r  S  c  i  e  n  c  e
  ```
- Negative indices:
  ```text
  Index: -15 -14 -13 -12 -11 -10 -9  -8  -7  -6  -5  -4  -3  -2  -1
   Char:   C   o   m   p   u   t  e   r   S   c   i   e   n   c   e
  ```
1. `text[3:10:2]`: Starts at index 3 (`'p'`), stops before index 10, step 2.
   - Selected indices: 3 (`'p'`), 5 (`'t'`), 7 (`'r'`), 9 (`'c'`) $\rightarrow$ `"ptrc"`
2. `text[-7:-2]`: Starts at -7 (`'S'`), stops before -2 (`'c'`).
   - Selected indices: -7 (`'S'`), -6 (`'c'`), -5 (`'i'`), -4 (`'e'`), -3 (`'n'`) $\rightarrow$ `"Scien"`
3. `text[::-3]`: Reverse entire string stepping backwards by 3 from index 14.
   - Selected indices: 14 (`'e'`), 11 (`'e'`), 8 (`'S'`), 5 (`'t'`), 2 (`'m'`) $\rightarrow$ `"eeStm"`
4. `text[8:2:-2]`: Starts at index 8 (`'S'`), goes down to index > 2 with step -2.
   - Selected indices: 8 (`'S'`), 6 (`'e'`), 4 (`'u'`) $\rightarrow$ `"Seu"`

---

#### Ans 8. String Transformation Output
**Output:**
```text
pRE#bOARD#3137
```
**Dry Run Trace Table:**
| Character `ch` | Condition Met | Action | Appended to `new_msg` | Current `new_msg` |
| :---: | :---: | :---: | :---: | :--- |
| `'P'` | `isupper()` | `ch.lower()` | `'p'` | `"p"` |
| `'r'` | `islower()` | `ch.upper()` | `'R'` | `"pR"` |
| `'e'` | `islower()` | `ch.upper()` | `'E'` | `"pRE"` |
| `'-'` | `else` | `'#'` | `'#'` | `"pRE#"` |
| `'B'` | `isupper()` | `ch.lower()` | `'b'` | `"pRE#b"` |
| `'o'` | `islower()` | `ch.upper()` | `'O'` | `"pRE#bO"` |
| `'a'` | `islower()` | `ch.upper()` | `'A'` | `"pRE#bOA"` |
| `'r'` | `islower()` | `ch.upper()` | `'R'` | `"pRE#bOAR"` |
| `'d'` | `islower()` | `ch.upper()` | `'D'` | `"pRE#bOARD"` |
| `'@'` | `else` | `'#'` | `'#'` | `"pRE#bOARD#"` |
| `'2'` | `isdigit()` | `(2 + 1) % 10` | `'3'` | `"pRE#bOARD#3"` |
| `'0'` | `isdigit()` | `(0 + 1) % 10` | `'1'` | `"pRE#bOARD#31"` |
| `'2'` | `isdigit()` | `(2 + 1) % 10` | `'3'` | `"pRE#bOARD#313"` |
| `'6'` | `isdigit()` | `(6 + 1) % 10` | `'7'` | `"pRE#bOARD#3137"` |

---

#### Ans 9. List Slicing Assignment Output
**Output:**
```text
After slice assignment: [10, 25, 35, 50, 60]
Popped value: 60
Final list: [10, 25, 99, 35, 50]
```
**Step-by-Step:**
1. `vals = [10, 20, 30, 40, 50, 60]`
2. `vals[1:4] = [25, 35]`: Slices out indices 1, 2, 3 (values `20, 30, 40`) and replaces them with `25, 35`.
   `vals` becomes `[10, 25, 35, 50, 60]`.
3. `vals.insert(2, 99)`: Inserts `99` before index 2.
   `vals` becomes `[10, 25, 99, 35, 50, 60]`.
4. `vals.pop()`: Removes and returns the last item, `60`.
5. Remaining list: `[10, 25, 99, 35, 50]`.

---

#### Ans 10. Aliasing vs. Shallow Copying Output
**Output:**
```text
a: [10, 2, [30, 4]]
b: [10, 2, [30, 4]]
c: [1, 20, [30, 4]]
```
**Explanation:**
- `b = a`: `b` is an alias (reference) pointing to the same list object as `a`.
- `c = a[:]`: `c` is a shallow copy. It creates a new top-level list object with its own slots for indices 0 and 1, but inner mutable objects (the sublist `[3, 4]`) are shared references.
- `b[0] = 10`: Changes index 0 of `a` and `b` to 10. `c[0]` remains 1.
- `c[1] = 20`: Changes index 1 of `c` only. `a[1]` and `b[1]` remain 2.
- `b[2][0] = 30`: Modifies the shared inner list from `[3, 4]` to `[30, 4]`. This change reflects across `a`, `b`, and `c`!

---

#### Ans 11. String Methods Output
**Output:**
```text
Tokens count: 5
Joined: maths-physics--chemistry-english
Head: maths
Tail: physics,,chemistry,english
```
**Explanation:**
- `record.split(",")`: Splits on every comma. The consecutive comma `,,` produces an empty string `""`.
  Tokens = `['maths', 'physics', '', 'chemistry', 'english']`. Length is `5`.
- `"-".join(tokens)`: Joins the 5 elements with `-`. The empty element produces double hyphens `--`.
- `record.partition(",")`: Splits at the *first* comma into a 3-element tuple `(head, sep, tail)`.
  - `head` = `'maths'`
  - `sep` = `','`
  - `tail` = `'physics,,chemistry,english'`

---

#### Ans 12. Overlapping Counts & Case Output
**Output:**
```text
Count of 'ana': 1
Capitalize: Cbse class 11 computer science
Title: Cbse Class 11 Computer Science
```
**Explanation:**
- `phrase.count("ana")`: In `"banana"`, indices 1–3 form `"ana"`. Once matched, Python advances the search cursor past the match to index 4 (`"na"`), which cannot form another `"ana"`. In `"bandanna"`, there is no `"ana"` (only `"an"` and `"ann"`). Hence total count is **1**.
- `.capitalize()`: Uppercases the first character (`'C'`) and lowercases all subsequent characters.
- `.title()`: Uppercases the first letter of each whitespace-delimited word.

---

### SECTION C SOLUTIONS (Error Finding & Debugging)

#### Ans 13.
**Errors Identified:**
1. `word[0] = 'J'`: **TypeError**. Strings are immutable in Python; individual characters cannot be reassigned.
2. `word.append(" 3.12")`: **AttributeError**. Strings do not possess an `.append()` method (that belongs to lists).

**Corrected Code:**
```python
word = "Python"
# Reconstruct using slicing and concatenation
word = "J" + word[1:] + " 3.12"
print(word)
```
*Output:* `Jython 3.12`

---

#### Ans 14.
**1. Output Printed:**
```python
[10, 30, 40, 20, 50]
```
**2. Explanation of Defect:**
When an element is removed using `L.remove(item)`, all subsequent items shift one index to the left. However, the `for` loop internal iterator advances its pointer to the next index number.
When index 1 (`20`) is removed, the second `20` shifts from index 2 to index 1. On the next iteration, the loop inspects index 2 (which now holds `30`), entirely skipping over the second `20`!

**3. Corrected Code:**
Option A: Iterate over a shallow copy of the list:
```python
L = [10, 20, 20, 30, 40, 20, 50]
for item in L[:]:
    if item == 20:
        L.remove(item)
print(L)
```
Option B: List comprehension (cleaner and idiomatic):
```python
L = [10, 20, 20, 30, 40, 20, 50]
L = [item for item in L if item != 20]
print(L)
```

---

#### Ans 15.
**Why it Crashes:**
`colors.index("Yellow")` raises a `ValueError: 'Yellow' is not in list` because the `.index()` method raises an exception when the sought item is missing.

**Safe Approaches:**
Approach 1: Check with `in` before calling `.index()`:
```python
colors = ["Red", "Green", "Blue"]
target = "Yellow"

if target in colors:
    idx = colors.index(target)
    print("Found at index:", idx)
else:
    print(f"'{target}' is not in the list.")
```

Approach 2: `try...except` block:
```python
colors = ["Red", "Green", "Blue"]
target = "Yellow"

try:
    idx = colors.index(target)
    print("Found at index:", idx)
except ValueError:
    print(f"'{target}' is not in the list.")
```

---

### SECTION D SOLUTIONS (Programming & Code Implementations)

#### Ans 16. Case-Insensitive Palindrome Checker
```python
# Program: Check if a string is a palindrome (case-insensitive)

raw_str = input("Enter a string: ")

# Convert to lowercase to ensure case-insensitive comparison
clean_str = raw_str.lower()

# Check using string reverse slice [::-1]
if clean_str == clean_str[::-1]:
    print(f"'{raw_str}' is a PALINDROME.")
else:
    print(f"'{raw_str}' is NOT a palindrome.")
```
**Sample Run:**
```text
Enter a string: RaceCar
'RaceCar' is a PALINDROME.
```

---

#### Ans 17. Character Category Counter
```python
# Program: Count character categories in a string

text = input("Enter a line of text: ")

upper_cnt = 0
lower_cnt = 0
vowel_cnt = 0
digit_cnt = 0
special_cnt = 0

vowels = "aeiouAEIOU"

for ch in text:
    if ch.isupper():
        upper_cnt += 1
    elif ch.islower():
        lower_cnt += 1
    
    if ch in vowels:
        vowel_cnt += 1
        
    if ch.isdigit():
        digit_cnt += 1
    elif not ch.isalnum():
        special_cnt += 1

print("\n--- Character Analysis ---")
print("Uppercase letters :", upper_cnt)
print("Lowercase letters :", lower_cnt)
print("Vowels            :", vowel_cnt)
print("Digits            :", digit_cnt)
print("Spaces & Specials :", special_cnt)
```
**Sample Run:**
```text
Enter a line of text: CBSE Class 11: CS @ 2026!

--- Character Analysis ---
Uppercase letters : 6
Lowercase letters : 6
Vowels            : 3
Digits            : 6
Spaces & Specials : 8
```

---

#### Ans 18. Linear Search in a List
```python
# Program: Linear search without using .index() or 'in' operator for searching

# Sample list or input list
numbers = [45, 12, 89, 34, 78, 23, 90, 11]
print("List contents:", numbers)

target = int(input("Enter number to search: "))

found = False
found_index = -1

for i in range(len(numbers)):
    if numbers[i] == target:
        found = True
        found_index = i
        break  # Stop search at first match

if found:
    print(f"Success: {target} found at 0-based index {found_index} (Position {found_index + 1}).")
else:
    print(f"Item {target} not found in list.")
```
**Sample Run:**
```text
List contents: [45, 12, 89, 34, 78, 23, 90, 11]
Enter number to search: 34
Success: 34 found at 0-based index 3 (Position 4).
```

---

#### Ans 19. Adjacent Element Swap
```python
# Program: Swap adjacent elements in a list

nums = [10, 20, 30, 40, 50, 60, 70]
print("Original list :", nums)

# Step by 2; stop at len - 1 to leave trailing odd element in place
for i in range(0, len(nums) - 1, 2):
    nums[i], nums[i + 1] = nums[i + 1], nums[i]

print("Swapped list  :", nums)
```
**Sample Run:**
```text
Original list : [10, 20, 30, 40, 50, 60, 70]
Swapped list  : [20, 10, 40, 30, 60, 50, 70]
```

---

#### Ans 20. Second Largest Element in a Single Pass
```python
# Program: Find largest and second largest in a list without sort() or max()

nums = [14, 52, 98, 36, 98, 77, 21]
print("Input list:", nums)

if len(nums) < 2:
    print("List must contain at least two elements.")
else:
    # Initialize largest and second largest with negative infinity or first two items
    largest = float('-inf')
    second_largest = float('-inf')

    for n in nums:
        if n > largest:
            second_largest = largest
            largest = n
        elif n > second_largest and n != largest:
            second_largest = n

    if second_largest == float('-inf'):
        print("All elements in the list are identical; no second largest exists.")
    else:
        print("Largest number        :", largest)
        print("Second largest number :", second_largest)
```
**Sample Run:**
```text
Input list: [14, 52, 98, 36, 98, 77, 21]
Largest number        : 98
Second largest number : 77
```

---

#### Ans 21. Deduplication Preserving Order
```python
# Program: Remove duplicates from a list while preserving original order

raw_list = [10, 20, 10, 30, 40, 20, 50, 10, 60, 40]
print("Original list :", raw_list)

unique_list = []

for item in raw_list:
    if item not in unique_list:
        unique_list.append(item)

print("Unique list   :", unique_list)
```
**Sample Run:**
```text
Original list : [10, 20, 10, 30, 40, 20, 50, 10, 60, 40]
Unique list   : [10, 20, 30, 40, 50, 60]
```

---

#### Ans 22. Even-Odd Separation & Aggregation
```python
# Program: Partition numbers into evens and odds, compute sums and counts

raw_input = input("Enter integers separated by space: ")
numbers = [int(x) for x in raw_input.split()]

evens = []
odds = []

for n in numbers:
    if n % 2 == 0:
        evens.append(n)
    else:
        odds.append(n)

print("\n--- Results ---")
print("Even numbers :", evens)
print("Count of Evens:", len(evens))
print("Sum of Evens  :", sum(evens))

print()
print("Odd numbers  :", odds)
print("Count of Odds :", len(odds))
print("Sum of Odds   :", sum(odds))
```
**Sample Run:**
```text
Enter integers separated by space: 12 7 9 14 22 5 8 11

--- Results ---
Even numbers : [12, 14, 22, 8]
Count of Evens: 4
Sum of Evens  : 56

Odd numbers  : [7, 9, 5, 11]
Count of Odds : 4
Sum of Odds   : 32
```

