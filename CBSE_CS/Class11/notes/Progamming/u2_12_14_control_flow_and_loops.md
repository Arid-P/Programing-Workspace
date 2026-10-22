# Unit 2: Computational Thinking and Programming-I (Topics 12–14)

---

## 12. Control Flow & Indentation in Python

- **Mental model:**
  - **Sequential Flow:** Walking down a straight single-lane hallway. Every door you pass must be entered in exact order.
  - **Selective Flow (Conditionals):** Arriving at a fork in the road with a signpost. If the sign matches your destination, you take the left path; otherwise, you take the right path.
  - **Iterative Flow (Loops):** A running track. You run laps around the oval repeatedly until the coach blows the whistle (`while condition becomes False` or `range count ends`).
  - **Indentation:** The building walls that enclose a room. In C/Java, curly braces `{ }` define rooms. In Python, the indent depth (the physical indentation from the left margin) *is* the wall. If a brick is misaligned by even one space, the structure collapses (`IndentationError`).

- **Key facts / definitions (CBSE Standard):**
  - **The Three Control Flow Structures:**
    1. *Sequential Flow:* The default execution model where statements are executed strictly one after another from top to bottom.
    2. *Selection / Conditional Flow:* Controls which statement block executes based on truth value evaluation of a Boolean expression (`if`, `if-else`, `if-elif-else`).
    3. *Iterative / Repetitive Flow:* Repeats a group of statements multiple times as long as a condition remains true (`for`, `while`).
  - **Indentation (Block / Suite Structure):**
    - A block (called a **suite** in Python) is a group of contiguous statements that belong to a single compound statement (like an `if` branch or a loop).
    - Indentation replaces curly braces `{ }` and `begin`/`end` markers.
    - All statements inside a suite **must have the identical level of indentation**.
    - Standard convention (PEP 8 & CBSE): **4 spaces per indentation level**.
    - Mixing tabs and spaces in Python 3 generates a compile-time **`TabError`** (subclass of `IndentationError`).

- **Worked example:**
  ```python
  # Indentation Demonstration
  age = 18
  if age >= 18:
      print("Eligible to vote")  # 4 spaces (inside suite)
      print("Apply for ID")     # 4 spaces (inside suite)
  print("Process complete")     # 0 spaces (outside suite, runs sequentially)
  ```

- **Common exam mistakes:**
  - Forgetting the colon `:` at the end of `if`, `elif`, `else`, `for`, `while` header lines (SyntaxError).
  - Mixing tabs and spaces inside the same source file.
  - Unaligned indentation within the same block:
    ```python
    if x > 0:
        print("Positive")
         print("Valid")  # IndentationError: unexpected indent!
    ```

---

## 13. Conditional Statements (`if`, `if-else`, `if-elif-else`)

- **Mental model:**
  - `if`: A tollbooth with a boom barrier. If you have a pass, you enter; if not, you bypass.
  - `if-else`: A two-way railway switch. The train goes down Track A or Track B, never both.
  - `if-elif-else`: A multi-tier priority ladder. Python tests each rung from top to bottom. The moment **one rung holds your weight (evaluates to True)**, you stop climbing, execute that rung's block, and jump straight to the bottom of the ladder (short-circuiting all remaining rungs).

- **Key facts / definitions (CBSE Standard):**
  - **Simple `if` Statement:**
    ```python
    if condition:
        statement(s)
    ```
  - **`if-else` Statement:**
    ```python
    if condition:
        statement(s)_if_true
    else:
        statement(s)_if_false
    ```
  - **`if-elif-else` Ladder (Chained Conditionals):**
    ```python
    if condition_1:
        block_1
    elif condition_2:
        block_2
    elif condition_3:
        block_3
    else:
        fallback_block
    ```
    - Conditions are checked sequentially from top to bottom.
    - As soon as any condition evaluates to `True`, its block executes, and Python exits the entire ladder immediately.
    - If all conditions evaluate to `False`, the `else` block executes (if present).
  - **Nested Conditionals:** An `if` or `if-else` statement placed entirely inside the body of another `if` or `else` block.
  - **Standard CBSE Logic Patterns:**
    1. *Absolute Value:*
       `abs_val = -n if n < 0 else n` (or standard `if n < 0: abs_val = -n`).
    2. *Finding Largest of Three Numbers:*
       ```python
       if a >= b and a >= c:
           largest = a
       elif b >= c:
           largest = b
       else:
           largest = c
       ```
    3. *Leap Year Gregorian Standard:*
       A year is a leap year if it is a century year divisible by 400, or a non-century year divisible by 4:
       `is_leap = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)`

- **Worked example:**
  - Flowchart & Python logic for sorting 3 numbers ($a, b, c$) in ascending order:
    ```python
    a = int(input("Enter A: "))
    b = int(input("Enter B: "))
    c = int(input("Enter C: "))
    
    if a > b:
        a, b = b, a
    if a > c:
        a, c = c, a
    if b > c:
        b, c = c, b
        
    print("Sorted order:", a, b, c)
    ```

- **Common exam mistakes:**
  - Using multiple independent `if` statements when an `if-elif-else` ladder is required (causes multiple unintended branches to execute).
  - Forgetting century leap year rules (e.g. claiming 1900 was a leap year; 1900 is divisible by 4, but divisible by 100 and NOT by 400, so it is **not** a leap year).

---

## 14. Loops (`for`, `while`, `range()`), Patterns, and Series

- **Mental model:**
  - **`for` Loop:** An inspector checking each item on a warehouse conveyor belt. The conveyor belt has an exact known length (`range`, string, list). Once the last item passes, the inspector goes home.
  - **`while` Loop:** A security guard at a gate. As long as the alarm is sounding (`condition == True`), the guard continues patrolling. You must remember to give the guard a key to disarm the alarm (`counter update`), or the guard patrols forever (infinite loop).
  - **Loop `else` Clause:** The "mission accomplished without alarms" bonus. If the loop completes all iterations naturally without tripping a wire (`break`), the `else:` suite executes. If an alarm trips (`break`), the bonus is cancelled.

- **Key facts / definitions (CBSE Standard):**
  - **The `range()` Generator:**
    - `range(stop)` $\implies 0, 1, 2, \dots, stop - 1$ (start defaults to 0, step defaults to 1).
    - `range(start, stop)` $\implies start, start + 1, \dots, stop - 1$ (step defaults to 1).
    - `range(start, stop, step)` $\implies start, start + step, start + 2\cdot step, \dots$
    - *Step constraints:*
      - If $step > 0$: $start < stop$ required; terminates when value $\ge stop$.
      - If $step < 0$: $start > stop$ required; terminates when value $\le stop$.
      - If $step == 0$: raises **`ValueError: range() arg 3 must not be zero`**.
  - **`while` Loop Syntax:**
    ```python
    initialization
    while test_condition:
        loop_body
        update_statement (increment/decrement)
    ```
  - **Loop Jump Statements:**
    - **`break`:** Terminates the innermost loop immediately. Bypasses the loop's `else:` block.
    - **`continue`:** Skips the rest of the current iteration and jumps immediately to the next iteration / condition evaluation.
  - **Loop `else` Suite:**
    - Syntactically attached directly to `for` or `while`.
    - **Executes ONLY if the loop exits normally** (i.e. condition becomes false in `while`, or `range` exhausts in `for`).
    - **Skipped if the loop is terminated prematurely via `break`**.

- **Worked example:**
  - **Prime Number Verification Algorithm (using `for...else`):**
    ```python
    num = int(input("Enter positive integer > 1: "))
    if num <= 1:
        print("Neither prime nor composite")
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                print(num, "is COMPOSITE (divisible by", i, ")")
                break
        else:
            print(num, "is PRIME")
    ```

- **Worked example 2: Nested Loops for Classic CBSE Patterns:**
  - Pattern 1: Right-Angled Triangle of Asterisks ($n=4$):
    ```text
    *
    * *
    * * *
    * * * *
    ```
    ```python
    n = 4
    for i in range(1, n + 1):
        for j in range(i):
            print("*", end=" ")
        print()  # newline
    ```
  - Pattern 2: Number Triangle:
    ```text
    1
    1 2
    1 2 3
    1 2 3 4
    ```
    ```python
    n = 4
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
    ```

- **Worked example 3: Series Summation ($x^k / k!$ with alternating signs):**
  - Series: $S = x - \frac{x^2}{2!} + \frac{x^3}{3!} - \frac{x^4}{4!} + \dots + (-1)^{n+1}\frac{x^n}{n!}$
    ```python
    x = float(input("Enter x: "))
    n = int(input("Enter number of terms n: "))
    
    total_sum = 0.0
    term = x
    sign = 1
    
    for k in range(1, n + 1):
        # Calculate factorial of k
        fact = 1
        for f in range(1, k + 1):
            fact *= f
        
        current_term = sign * (x ** k) / fact
        total_sum += current_term
        sign = -sign  # Alternate sign (+1, -1, +1, ...)
        
    print("Sum of series:", total_sum)
    ```

- **Common exam mistakes:**
  - Forgetting loop counter update inside `while` loops, causing infinite execution.
  - Off-by-one errors in `range(start, stop)` (forgetting that `stop` is non-inclusive).
  - Calling `range(1, 10, 0)` which triggers a `ValueError`.

