# CBSE Class 11 Computer Science (083)
## Viva Voce Master Question Bank (Examiner & Mentor Guide)

> **Purpose:** This question bank is designed for the mentor to conduct rigorous, interactive Viva Voce examinations with the younger brother (yb). It covers all core theoretical traps, viva examiner favorite questions, and code tracing puzzles across the official CBSE Class 11 Computer Science syllabus.

---

### Legend & Marking Guide
* **Core Question:** The direct prompt to ask the student aloud.
* **Target Answer:** The exact technical keywords and concepts the student must articulate to get full marks.
* **Examiner Follow-up / Trap:** The curveball question to ask if the student gives a textbook definition or hesitates.
* **Common Student Misconception:** What students typically get wrong.

---

## Section 1: Python Basics, Tokens & Data Types

#### Q1.1: What are tokens in Python? Name all five categories of tokens.
* **Target Answer:** A token is the smallest individual lexical unit in a Python program. Python has 5 types of tokens:
  1. **Keywords:** Reserved words with special meaning (e.g., `if`, `while`, `def`, `class`).
  2. **Identifiers:** User-defined names for variables, functions, and objects.
  3. **Literals:** Constant raw data values (e.g., `10`, `3.14`, `"hello"`, `True`).
  4. **Operators:** Symbols that perform computations (e.g., `+`, `==`, `and`).
  5. **Punctuators / Delimiters:** Symbols used for structure and syntax (e.g., `(`, `)`, `:`, `,`, `[`).
* **Examiner Follow-up:** "Name three keywords in Python that start with an uppercase letter."
  * *Answer:* `True`, `False`, and `None`. All other Python keywords are strictly lowercase.

#### Q1.2: What are the naming rules for an identifier? Is `2nd_number` or `my-var` valid?
* **Target Answer:**
  1. Must start with an alphabet letter (`a-z`, `A-Z`) or an underscore (`_`).
  2. Cannot start with a digit.
  3. Can only contain letters, digits, and underscores. No hyphens, spaces, or special characters (`$`, `@`, `%`) are allowed.
  4. Case-sensitive (`num` and `Num` are different).
  5. Cannot be a Python keyword.
  * `2nd_number` is **invalid** (starts with a digit).
  * `my-var` is **invalid** (contains a hyphen `-`, which Python interprets as the subtraction operator).

#### Q1.3: What is the core difference between Mutable and Immutable data types?
* **Target Answer:**
  * **Immutable:** The value or content stored at a memory address **cannot** be changed in-place after creation. Any modification creates a new object at a new memory location. Examples: `int`, `float`, `complex`, `bool`, `str`, `tuple`.
  * **Mutable:** The content of the object can be modified in-place without changing its memory identity (`id()`). Examples: `list`, `dict`, `set`.
* **Examiner Follow-up:** "If I write `x = 10` and then `x = 20`, didn't I just mutate `x`?"
  * *Target Answer:* No! `x` is a variable name (reference). The integer object `10` was not modified; rather, the name `x` was rebound to a completely new integer object `20`. The original integer `10` remains unchanged in memory.

#### Q1.4: What is the difference between `(10)` and `(10,)` in Python?
* **Target Answer:**
  * `(10)` is evaluated as an integer enclosed in arithmetic grouping parentheses. Its type is `<class 'int'>`.
  * `(10,)` is a **single-element tuple**. The comma `,` is what defines a tuple in Python, not the parentheses!
* **Examiner Follow-up:** "What is the type of `x = 10, 20` without parentheses?"
  * *Target Answer:* `<class 'tuple'>` (Tuple packing).

---

## Section 2: Operators, Precedence & Type Conversions

#### Q2.1: What is the difference between `/` and `//` in Python?
* **Target Answer:**
  * `/` is **true division** (floating-point division). It *always* returns a float, even if the division is exact (e.g., `4 / 2` evaluates to `2.0`).
  * `//` is **floor division**. It divides and rounds down to the nearest lower integer (mathematical floor).
* **Examiner Follow-up (Classic CBSE Trap):** "What does `-7 // 2` evaluate to?"
  * *Target Answer:* **`-4`**! (Students usually answer `-3`). In math, $-7 / 2 = -3.5$. Rounding down towards negative infinity gives $-4$.

#### Q2.2: Differentiate between the `==` operator and the `is` operator.
* **Target Answer:**
  * `==` is the **equality operator**. It checks if the **values** of the operands are equal (`x == y`).
  * `is` is the **identity operator**. It checks if both operands reference the **exact same memory location** (`id(x) == id(y)`).
* **Examiner Follow-up:**
  ```python
  a = [1, 2]
  b = [1, 2]
  print(a == b)
  print(a is b)
  ```
  * *Target Answer:* `True` (same contents) and `False` (two distinct list objects in memory).

#### Q2.3: Why does `int("3.5")` crash, but `int(float("3.5"))` works?
* **Target Answer:** `int(str)` expects a string literal containing a valid base-10 integer representation (digits only). When it encounters a decimal point `.` in a string, it raises `ValueError: invalid literal for int() with base 10: '3.5'`. `float("3.5")` parses the decimal string into float `3.5`, and `int(3.5)` truncates the float to `3`.

#### Q2.4: What does `bool("False")` evaluate to?
* **Target Answer:** **`True`**! In Python, any non-empty string evaluates to `True` in a boolean context. Only the empty string `""` is falsy.

---

## Section 3: Control Flow, Loops & Scope

#### Q3.1: Differentiate between `break` and `continue`.
* **Target Answer:**
  * `break`: Immediately terminates the innermost active loop and transfers execution to the statement immediately following the loop.
  * `continue`: Skips the remainder of the *current iteration* only, jumping straight to the loop condition evaluation or the next item in the sequence.

#### Q3.2: Explain the `else` clause in Python loops (`for...else` / `while...else`).
* **Target Answer:** The `else` block of a loop executes **only if the loop terminates normally** (i.e. reaches the end of the iterable or the while condition becomes False). If the loop is exited prematurely via a `break` statement, the `else` block is **skipped**.
* **Examiner Follow-up:** "How is this used in checking for prime numbers?"
  * *Target Answer:* If a divisor is found, we call `break`. The `else` clause attached to the loop prints "Prime", which runs only if no `break` was ever triggered!

#### Q3.3: How does `range()` work with 1, 2, and 3 arguments?
* **Target Answer:**
  * `range(stop)`: Starts at `0`, increments by `1`, goes up to `stop - 1`.
  * `range(start, stop)`: Starts at `start`, increments by `1`, goes up to `stop - 1`.
  * `range(start, stop, step)`: Starts at `start`, increments by `step`, stops before reaching `stop`.
  * In all cases, the `stop` boundary is **excluded** (half-open interval $[start, stop)$).
* **Examiner Follow-up:** "What is `list(range(5, 1, -1))`?"
  * *Target Answer:* `[5, 4, 3, 2]`. (Stops before 1).

---

## Section 4: Strings & String Methods

#### Q4.1: Contrast `s.find("x")` and `s.index("x")`.
* **Target Answer:** Both return the lowest 0-based index where substring `"x"` begins.
  * If `"x"` is **absent**: `find()` returns **`-1`**, whereas `index()` raises a **`ValueError: substring not found`**.

#### Q4.2: What does `"hello-world-python".partition("-")` return? Contrast with `split("-")`.
* **Target Answer:**
  * `partition("-")` always returns a **3-tuple**: `(head, separator, tail)`. Here: `('hello', '-', 'world-python')`. It stops at the *first* occurrence of the separator.
  * `split("-")` returns a **list** of all separated substrings: `['hello', 'world', 'python']`.

#### Q4.3: What is the difference between `s.split()` and `s.split(" ")`?
* **Target Answer:**
  * `s.split()` (no argument / `None`): Treats consecutive whitespace characters (spaces, tabs, newlines) as a single delimiter and strips leading/trailing whitespaces.
  * `s.split(" ")`: Strictly splits by single space characters. Consecutive spaces produce empty strings `""` in the output list.
  * Example: `"a  b".split()` $\rightarrow$ `['a', 'b']`, whereas `"a  b".split(" ")` $\rightarrow$ `['a', '', 'b']`.

---

## Section 5: Lists & Tuples

#### Q5.1: Differentiate between `list.append(x)` and `list.extend(x)`.
* **Target Answer:**
  * `append(x)` adds `x` as a **single element** at the end of the list. If `x` is a list `[1, 2]`, it adds the entire sublist as one element.
  * `extend(iterable)` iterates over the provided iterable and appends **each of its items individually** to the end of the list.
  * Trace:
    * `lst = [10]; lst.append([1, 2])` $\implies$ `[10, [1, 2]]` (length 2).
    * `lst = [10]; lst.extend([1, 2])` $\implies$ `[10, 1, 2]` (length 3).

#### Q5.2: Differentiate between `list.sort()` and `sorted(iterable)`.
* **Target Answer:**
  * `list.sort()`: A list method that sorts the list **in-place**, permanently modifying the original list. It returns **`None`**.
  * `sorted(iterable)`: A built-in function that takes any iterable and returns a **new sorted list**, leaving the original iterable completely unchanged.

#### Q5.3: Contrast `remove()`, `pop()`, and `del`.
* **Target Answer:**
  * `list.remove(value)`: Searches for the *first occurrence* of `value` and deletes it. Raises `ValueError` if `value` is not present. Returns `None`.
  * `list.pop([index])`: Removes and **returns** the element at the specified index (defaults to the last element `-1`). Raises `IndexError` if out of bounds or list is empty.
  * `del list[index]`: Python statement that deletes the item at `index` (or a slice `del list[a:b]`). Does not return anything.

#### Q5.4: Can a tuple contain a list? Can that list be modified? Does it contradict tuple immutability?
* **Target Answer:**
  * Yes, e.g., `t = (1, [10, 20], 3)`.
  * Yes, executing `t[1].append(30)` succeeds and modifies the list to `(1, [10, 20, 30], 3)`.
  * It does **not** contradict tuple immutability! Immutability means the tuple's *references* cannot change. The tuple stores a reference (memory address) to the list object. The list object itself was modified in-place, but the tuple still references the exact same list at the exact same memory address.
  * However, executing `t[1] = [50]` raises `TypeError` because that attempts to reassign a tuple element.

---

## Section 6: Dictionaries

#### Q6.1: What are the restrictions on dictionary keys in Python? Why can't a list be a key?
* **Target Answer:**
  1. Dictionary keys must be **unique** (duplicate keys overwrite earlier values).
  2. Dictionary keys must be **immutable / hashable** (e.g. `int`, `float`, `str`, `tuple` containing only immutables).
  * A list cannot be a key because lists are mutable; their contents and therefore their hash value can change during execution, which would break the underlying hash table lookup. Python raises `TypeError: unhashable type: 'list'`.

#### Q6.2: Differentiate between `d["key"]` and `d.get("key")`.
* **Target Answer:**
  * If `"key"` exists, both return its associated value.
  * If `"key"` is **missing**:
    * `d["key"]` raises a **`KeyError`**.
    * `d.get("key")` safely returns **`None`** (or a specified default value `d.get("key", default)`), without raising an error.

#### Q6.3: What does `d.setdefault(key, default)` do?
* **Target Answer:**
  * If `key` is present in `d`, it returns its existing value.
  * If `key` is missing, it inserts `key: default` into the dictionary and returns `default`.

#### Q6.4: What is the trap with `dict.fromkeys(["a", "b"], [])`?
* **Target Answer:** Both keys `"a"` and `"b"` will point to the **exact same list instance** in memory. Modifying `d["a"].append(1)` will also mutate `d["b"]` to `[1]`!

---

## Section 7: Python Standard Modules (`math`, `random`, `statistics`)

#### Q7.1: What is the difference between `random.randint(1, 6)` and `random.randrange(1, 6)`?
* **Target Answer:**
  * `random.randint(1, 6)` generates random integers in the **closed interval $[1, 6]$**. Both endpoints `1` and `6` can be generated.
  * `random.randrange(1, 6)` generates random integers in the **half-open interval $[1, 6)$**. It generates numbers from `1` to `5`; the upper bound `6` is **strictly excluded**.

#### Q7.2: What is the range of values generated by `random.random()`? Can it ever return `1.0`?
* **Target Answer:** It generates a floating-point number in the range $[0.0, 1.0)$. It can return `0.0`, but it can **never** return `1.0`.

#### Q7.3: Predict the outputs:
* `math.floor(-3.2)` $\implies$ **`-4`** (rounds down).
* `math.ceil(-3.2)` $\implies$ **`-3`** (rounds up).
* `math.fabs(-5)` $\implies$ **`5.0`** (always returns a float).
* `math.pow(2, 3)` $\implies$ **`8.0`** (always returns a float).

#### Q7.4: In the `statistics` module, how does `mode()` handle ties in modern Python (3.8+)?
* **Target Answer:** In Python 3.8+, if there are multiple modes with equal frequency, `statistics.mode()` returns the **first-encountered mode** in the input sequence. Can `mode()` accept non-numeric data like strings? **Yes**, it operates on nominal data (e.g. `mode(["red", "blue", "red"])` returns `"red"`).

---

## Section 8: Lab Practical Defense (Grilling on the 20 Programs)

* **Linear Search:** "What is the worst-case time complexity of linear search on a list of $n$ elements?" $\implies$ $O(n)$, when the element is at the end or absent.
* **Euclidean Algorithm (GCD):** "Why is Euclidean algorithm faster than checking every number from 1 to $\min(a, b)$?" $\implies$ Because it uses modulo division (`a, b = b, a % b`), reducing the numbers logarithmically.
* **Armstrong Numbers:** "Why do we raise each digit to the power of the total number of digits $k$?" $\implies$ Because that is the true definition of an $n$-digit narcissistic number ($153 = 1^3 + 5^3 + 3^3$, but $9474 = 9^4 + 4^4 + 7^4 + 4^4$).
* **Second Largest in One Pass:** "Can you find the second largest in a list without sorting? How do you handle duplicate values of the maximum?" $\implies$ Keep two variables `largest` and `second_largest`. Update `second_largest` only when an element is strictly smaller than `largest` but greater than `second_largest`.

