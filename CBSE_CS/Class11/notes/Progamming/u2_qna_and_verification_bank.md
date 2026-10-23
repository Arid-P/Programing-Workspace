# CBSE Class 11 Computer Science (083)
## Unit 2: Raw QnA & Verification Archive

This file records the **exact, raw questions** presented during the sessions, the **exact, verbatim answers** submitted by the student (unedited), and the **CBSE model solutions / corrections**.

---

### Topic 01 & 02: Problem Solving Steps, Flowcharting, Pseudocode, and Decomposition

#### Raw Questions Given:
##### Conceptual QnA
1. In CBSE marking schemes, what is the precise difference between **Testing** and **Debugging**? Explain why testing can succeed in finding bugs while debugging might still fail.
2. If an algorithm is given to compute $1 / (x - 5)$, which essential characteristic of an algorithm is violated when $x = 5$ if no conditional check is included?
3. What is the geometric difference in a flowchart between reading an integer from the keyboard (`n = int(input())`) versus assigning a computed value to a variable (`count = count + 1`)? Name both shapes.
4. Explain the principle of **Decomposition** in problem-solving and name two concrete software engineering benefits it provides.

##### True / False Statements
* Statement 1: A connector symbol in a flowchart is represented by a small triangle.
* Statement 2: Pseudocode must follow the exact indentation and syntax rules of the target programming language to be considered valid.
* Statement 3: An algorithm must produce at least one output, but can accept zero inputs.
* Statement 4: The Decision box (Diamond) can have only one incoming path and must have at least two exiting alternative flow lines.
* Statement 5: Testing is carried out before the coding phase is initiated.

#### Raw Student Answer (Verbatim):
> Testing is the process of finding if the program has any error by running it with known test datasets. While debugging is the process of diagnosis and correcting a known error by finding it in the source code.
> 
> The definiteness of the algorithm is violated here, as for x equals to 5, the algorithm is not clearly defined.
> 
> The main geometric difference in a flowchart between reading an integer would be that it is present in a parallel diagram to show that it is either an input or an output, while assigning a computed value to a variable is present in a rectangular box to show that it is a process that is present.
> 
> The principle of decomposition is breaking a large problem into smaller sub-problems which are independent of each other, hence can be solved alone and after solving each one of them We can combine them both and we get the solution to the meal.
> 2 main and concrete benefits that software engineer see through it that large problems or problems he has to ask. Now there is a small problem that needs to be solved and each one of them or each one of the problems are loosely solved about it. Hence there is not much hassle within solving each one of them and then combining back. Second, it saves the opponent time or kicking time that now we have to do this and all that new. After breaking down, each shoon of the dungeon independently sorts these without heading to plan.
> 
> f, t, f, t, f

#### CBSE Evaluation & Model Answers:
*   **Q1:** **Correct.** Testing is executing a program with known inputs to detect anomalies, failures, or incorrect outputs. Debugging is the subsequent diagnostic phase of identifying the root cause in the source code and removing the defect.
*   **Q2:** **Correct.** **Definiteness** (and **Effectiveness**) is violated. At $x = 5$, $1/(5 - 5) = 1/0$ is mathematically undefined. Every instruction of an algorithm must have a single, definite meaning and must be computationally feasible.
*   **Q3:** **Correct.** Reading an input is placed in a **Parallelogram** (Input/Output symbol). Variable assignments and arithmetic computations are placed in a **Rectangle** (Process symbol).
*   **Q4:** **Correct.** Decomposition is top-down modularization: breaking a complex problem into independent, smaller sub-problems. Key benefits:
    1. *Reduced Complexity / Cognitive Load:* Sub-problems are easier to implement, test, and maintain in isolation.
    2. *Reusability & Team Parallelism:* Modules can be reused across different programs or developed concurrently by multiple developers.
*   **True/False Statements:** `f, t, f, t, f` (3/5 Correct)
    *   *Correction on Statement 2:* Statement 2 is **FALSE**. Pseudocode is intentionally informal, language-agnostic, and relaxed; it does not follow strict syntax, keywords, or punctuation of any specific compiler/interpreter.
    *   *Correction on Statement 3:* Statement 3 is **TRUE**. An algorithm can take zero inputs (e.g., an algorithm that prints the first 50 Fibonacci numbers or current time requires no external input), but it **must** produce at least one output to be meaningful.



---

### Topic 03, 04 & 05: Python Basics, Execution Modes, Tokens, and Variables

#### Raw Questions Given:
##### Conceptual QnA
1. In Python, what is the exact operational difference between typing `2 + 5` into the Interactive Mode prompt versus saving `2 + 5` inside a `.py` file and running it in Script Mode?
2. Examine the following list of proposed variable names. Classify each as **Valid** or **Invalid**, and for every invalid one, state the exact syntactic rule violated:
   - `_3rd_record`
   - `total-sum`
   - `True`
   - `2nd_player`
   - `while_count`
3. Classify every individual token in the following Python statement into one of the 5 CBSE token categories:
   ```python
   score = (points * 2) + 10
   ```
4. Define **L-value** and **R-value** in the context of Python assignment statements. Using those definitions, explain precisely why the Python statement `x + y = 100` generates a `SyntaxError`.

##### True / False Statements
* Statement 1: In Python, an identifier can begin with an underscore (`_`) but cannot begin with a number.
* Statement 2: The keywords `def`, `return`, and `import` can be written as `Def`, `Return`, and `Import` interchangeably.
* Statement 3: The scientific literal `2.5e3` represents the float value $2500.0$.
* Statement 4: An unassigned triple-quoted string literal (`""" ... """`) placed inside a Python file is treated as a comment and ignored during execution.
* Statement 5: The statement `a, b = b, a` is syntactically invalid because multiple L-values cannot appear on the left of an assignment operator.

#### Raw Student Answer (Verbatim):
> If you type 2 plus 5 into the interactive mode, of, Python, then it will give the output of 7 directly on the screen. But if you type 2 plus 5 inside .py file, it will give you nothing even on running it. Moreover, if you close the session, the 2 plus five does have to vanish. while the 2 plus five, will exists in the .py  file unless the file itself is deleted
> Invalid: True (keyword), 2nd+player (starts with number)
> identifier: score, points
> literals: numeric (2, 10)
> operators: *, +, =
> delimitors: (,)  
> The L-value and R-value in the context of Python-side menstruation means the left-hand value and the right-hand value respectively. Or the expression of the value on the left-hand side of the equal sign and the right-hand side of the equal sign respectively. The L values are half constraints. They can only be values which are assigned equal, which can be assigned to a person. While R values do not have any specific distribution, they are with some rules. like they can get any expression and value available without any such things, but not a keyword. For the Python statement x plus y equals 100, it is invalid because the left value or the l value practice x plus y is an expression, but a left value can never be an expression.
> t, f, t, t, f

#### CBSE Evaluation & Model Answers:
*   **Q1:** **Correct.** Interactive Mode (REPL) automatically evaluates expressions and echoes the result (`7`) immediately to stdout; however, the command is non-persistent (vanishes when the session terminates). Script mode files (`.py`) execute batch commands and do not display unevaluated expression statements unless wrapped in `print()`; scripts are stored persistently on secondary storage.
*   **Q2:** **Mostly Correct (1 missing case):**
    *   `_3rd_record`: **Valid** (can start with an underscore and contain alphanumeric characters).
    *   `total-sum`: **Invalid** (contains hyphen `-`, which is an arithmetic operator, not an identifier character).
    *   `True`: **Invalid** (cannot use a reserved Python keyword).
    *   `2nd_player`: **Invalid** (identifiers cannot begin with a digit).
    *   `while_count`: **Valid** (begins with a letter; `while` is a keyword, but `while_count` is a unique compound name and thus valid).
*   **Q3:** **Correct.** 
    *   Identifiers: `score`, `points`
    *   Literals: `2`, `10` (integer numeric literals)
    *   Operators: `*`, `+`, `=` (arithmetic and assignment operators)
    *   Punctuators / Delimiters: `(`, `)`
*   **Q4:** **Correct.** An **L-value** represents a locator or reference to an assignable memory location appearing on the LHS of `=`. An **R-value** is any expression or literal that evaluates to a value on the RHS. The expression `x + y` computes a temporary value in an accumulator register rather than referencing an assignable memory target; thus `x + y = 100` triggers `SyntaxError: cannot assign to expression`.
*   **True/False Statements:** `t, f, t, t, f` (5/5 Correct).


---

### Topic 06, 07, 08 & 09: Data Types, Mutability, Operators, Precedence, and Type Conversion

#### Raw Questions Given:
##### Conceptual QnA
1. Trace the step-by-step evaluation order and final values for the following two Python expressions, explaining which associativity rule applies:
   - Expression A: `2 ** 3 ** 2`
   - Expression B: `5 + 3 * 2 // 4 - 1`
2. Using Python's floor division and modulo definition $r = a - (b \times (a // b))$, determine the exact evaluated output of:
   - `-13 // 4`
   - `-13 % 4`
   - `13 % -4`
3. Explain why `int(4.8)` evaluates cleanly to `4`, whereas `int("4.8")` crashes with a `ValueError`. How must a programmer properly convert `"4.8"` to an integer?
4. What do each of the following expressions evaluate to, and why?
   - `bool("False")`
   - `bool("")`
   - `"Python" or "CBSE"`
   - `"" and "CBSE"`

##### True / False Statements
* Statement 1: Tuples and strings are categorized as immutable sequences because their individual elements cannot be modified in place.
* Statement 2: In the complex number literal `z = 4 + 7j`, both `z.real` and `z.imag` return floating-point numbers.
* Statement 3: The chained comparison `10 > 5 == True` evaluates to `True` in Python.
* Statement 4: If `a = [10, 20]` and `b = a`, then `b += [30]` mutates `a` in place so that `a` becomes `[10, 20, 30]`.
* Statement 5: The identity operator `is` evaluates to `True` if two variables have the same values, even if they reside at different memory addresses.

#### Raw Student Answer (Verbatim):
> 1. 2**3**2 = 2**(3**2) = 2**9 = 512
> 5 + 3 * 2 // 4 - 1 = 5 + (3 * 2) // 4 - 1  = 5 + (6 // 4) - 1 = 5 + 1 -1 = 5
> 2. -13 // 4 = floor(-3.25) = -4
> -13 % 4 = 3
> 13 % -4 = 13 - (13 * (-4)) = 13 + 52= 65
> 3. If you provide an float value within the integer function, then it turns the integer part of the float. But if you provide a string which contains any characters other than a base 10 integer value, the integer function returns or crashes with a value error. So the programmer must first convert the string of 4.8 to using float to a float value of 4.8 and just as in the first statement we can use the int function to convert the 4.8 float value into a clean integer of 4.
> 4. True, False, "Python", ""
> t, t, false, t, false

#### CBSE Evaluation & Model Answers:
*   **Q1:** **Correct.** 
    *   `**` has right-to-left associativity: $3^2 = 9 \implies 2^9 = 512$.
    *   In `5 + 3 * 2 // 4 - 1`, `*` and `//` have higher precedence than `+` and `-` and evaluate left-to-right: $3 \times 2 = 6 \implies 6 // 4 = 1 \implies 5 + 1 - 1 = 5$.
*   **Q2:** **Mostly Correct (arithmetic slip on part 3):**
    *   `-13 // 4 = -4` (Correct: $\lfloor -3.25 \rfloor = -4$).
    *   `-13 % 4 = 3` (Correct: $-13 - (4 \times -4) = -13 - (-16) = 3$).
    *   `13 % -4 = -3`: The formula is $r = a - (b \times (a // b))$.
        *   $a // b = 13 // -4 = -4$.
        *   $r = 13 - ((-4) \times (-4)) = 13 - 16 = -3$.
        *   *(Rule of Thumb: In Python, the sign of the modulo result always takes the sign of the divisor $b$. Since $b = -4$, the remainder must be negative).*
*   **Q3:** **Correct.** `int(float_val)` performs truncation towards zero. `int(str_val)` strictly expects a string representing a base-10 integer; non-integer characters like the decimal dot `.` trigger `ValueError`. The fix is double casting: `int(float("4.8"))`.
*   **Q4:** **Correct.**
    *   `bool("False")` $\rightarrow$ `True` (any non-empty string is truthy).
    *   `bool("")` $\rightarrow$ `False` (empty string is falsy).
    *   `"Python" or "CBSE"` $\rightarrow$ `"Python"` (short-circuit returns the first truthy operand).
    *   `"" and "CBSE"` $\rightarrow$ `""` (short-circuit returns the first falsy operand).
*   **True/False Statements:** `t, t, false, t, false` (5/5 Correct).


---

### Topic 10, 11 & 25: Console I/O, Error Classification, and Module Imports

#### Raw Questions Given:
##### Conceptual QnA
1. Predict the exact, character-for-character console output produced by the following two Python lines:
   ```python
   print("Delhi", "Mumbai", "Chennai", sep=" -> ", end=" ## ")
   print("Kolkata", "Bengaluru", sep=" & ")
   ```
2. A beginner student writes the following bill calculator script:
   ```python
   item_price = input("Enter item price: ")
   tax_rate = 0.18
   total_bill = item_price + (item_price * tax_rate)
   print("Total:", total_bill)
   ```
   What exact error does Python generate when this script is run, on which line does it fail, and why? Show the corrected assignment line for `item_price`.
3. Classify each of the following three scenarios into **Syntax Error**, **Run-time Error**, or **Logical Error**, and state whether the error is caught *before* or *during* program execution:
   - **Scenario A:** A script has `def calc_area(r)` without a trailing colon `:` on line 12.
   - **Scenario B:** A function attempts to compute `percentage = marks / total_subjects` where `total_subjects` is `0`.
   - **Scenario C:** A programmer computes simple interest using `si = p * r * t / 100` but types `si = p * r + t / 100`.
4. Contrast `import math` with `from math import sqrt` in terms of namespace isolation. If a script executes `import math as m`, can the programmer still call `math.sqrt(9)`? Explain why or why not.

##### True / False Statements
* Statement 1: If a Python script contains a Syntax Error on line 40, lines 1 through 39 will execute and print their outputs before the error is reported.
* Statement 2: The `input()` function can return an integer object if the user enters only digits without spaces or decimal points.
* Statement 3: An `IndentationError` in Python is a subclass of `SyntaxError` and is detected during the parsing phase before runtime.
* Statement 4: Calling `print("Hello", end="")` ensures that the subsequent `print()` statement will output on the same line immediately following `"Hello"`.
* Statement 5: The wildcard statement `from math import *` requires all math functions to be accessed using the `math.` prefix.

#### Raw Student Answer (Verbatim):
> 1. Delhi -> Mumbai -> Chennai ## 
> 2. It fails on line 3 when the operation "item_price * tax_price" is prformed as itemprice is a string data type variable while tax raet is a float, and string and float cannot be multiplied together (I think it will give ValueError). To fix it, make the first line to item_price = float(input("Enter item price: "))
> 3. A. Syntax Error, before execution
> B. Run-time Error, during
> c. Logical Error, never caught by python.
> DOUBT: What is a namespace?
> 4. import math imports the whole module into the local namespace and to acess a func of it we need to do like math.sqrt(25) . But in from math import sqrt only the sqrt function is imported into the local namespace. 
> No, bcz now the refrence to the module is m not math in the namespace
> f, f, t, t, f

#### CBSE Evaluation & Model Answers:
*   **Q1:** **Partially Complete.** The user provided the output of the first line, but missed the second line. Because `end=" ## "` replaces the default newline, the second `print()` outputs on the **exact same line**:
    `Delhi -> Mumbai -> Chennai ## Kolkata & Bengaluru`
*   **Q2:** **Correct.** Line 3 fails with `TypeError: can't multiply sequence by non-int of type 'float'`. Because `input()` always returns a `str`, multiplying a string by a float is illegal. Correct line 1: `item_price = float(input("Enter item price: "))`.
*   **Q3:** **100% Correct.**
    *   A: **Syntax Error** (caught before execution during parsing).
    *   B: **Run-time Error** (`ZeroDivisionError`, raised during execution).
    *   C: **Logical Error** (program runs cleanly but produces incorrect answers; never detected by Python).
*   **Q4:** **Correct.** `import math` binds the module object to the name `math` in the current namespace; functions must be accessed via dot notation `math.sqrt()`. `from math import sqrt` binds the identifier `sqrt` directly in the local namespace. When aliased (`import math as m`), the identifier `math` is **not** bound, so calling `math.sqrt(9)` raises a `NameError: name 'math' is not defined`.
*   **Doubt Addressed (Namespace):** A **namespace** is a mapping from names (identifiers) to objects (like variables, functions, modules). Internally in Python, it is implemented as a dictionary (`name: object_reference`). It ensures that names in different scopes do not collide (e.g., `math.sqrt` lives in module `math`'s namespace, separate from a local variable `sqrt`).
*   **True/False Statements:** `f, f, t, t, f` (5/5 Correct).


---

### Topic 12, 13 & 14: Control Flow, Conditionals, and Loops

#### Raw Questions Given:
##### Conceptual QnA
1. Trace the exact console output of the following Python program, line by line:
   ```python
   for n in range(1, 6):
       if n == 3:
           continue
       if n == 5:
           break
       print("Item:", n)
   else:
       print("Loop Completed Successfully")
   print("End")
   ```
2. Write the exact list of integers generated by each of the following three `range()` expressions:
   - `list(range(4))`
   - `list(range(3, 15, 4))`
   - `list(range(12, 2, -3))`
3. Consider the nested loop:
   ```python
   count = 0
   for i in range(1, 5):
       for j in range(i):
           count += 1
   print("Total count:", count)
   ```
   Show how `count` increments on each outer loop pass ($i=1, 2, 3, 4$), and state the final printed value of `count`.
4. State the complete conditional logic (using `and`, `or`, `%`) required to determine if a given year `Y` is a **Leap Year** according to the Gregorian calendar standard taught in CBSE.

##### True / False Statements
* Statement 1: In Python, the `else` block of a `for` loop executes only if the loop is terminated by a `break` statement.
* Statement 2: The statement `list(range(5, 5))` evaluates to an empty list `[]`.
* Statement 3: Inconsistent mixing of tabs and spaces for indentation in Python 3 generates a compile-time `TabError`.
* Statement 4: An `if-elif-else` ladder will evaluate every `elif` condition even after finding a condition that is `True`.
* Statement 5: The condition `if 0:` evaluates to `False` in Python.

#### Raw Student Answer (Verbatim):
> 1. Item: 1
> Item: 2
> Item: 4
> End
> 2. 0, 1, 2, 3
> 3, 7, 11
> 12, 9, 6, 3
> (DOUBT: What if only two args are passed to range?)
> 3. when i = 1 ends count = 1
> i = 2 ends count = 3
> i = 3 ends count = 6
> i = 4 ends count = 10
> 4. y = int(input("Enter year: "))
> if y%400 == 0 or (y%4 == 0 and y %100 != 0):
>     print("It is a leap year")
> f, t, t, f, t

#### CBSE Evaluation & Model Answers:
*   **Q1:** **100% Correct.** Accurate line-by-line trace. `continue` skips 3, `break` terminates at 5 and bypasses the loop `else` suite, followed by `"End"`.
*   **Q2:** **100% Correct.** Outputs are `[0, 1, 2, 3]`, `[3, 7, 11]`, and `[12, 9, 6, 3]`.
    *   *Doubt Addressed (`range` with 2 arguments):* When two arguments are provided `range(start, stop)`, the first is `start` and the second is `stop`. The step defaults to `+1`. E.g., `range(2, 6)` produces `2, 3, 4, 5`.
*   **Q3:** **100% Correct.** The triangular number summation $1 + 2 + 3 + 4 = 10$. Passes: $i=1 \implies 1$; $i=2 \implies 3$; $i=3 \implies 6$; $i=4 \implies 10$.
*   **Q4:** **100% Correct.** A year is a leap year if `(y % 400 == 0) or (y % 4 == 0 and y % 100 != 0)`.
*   **True/False Statements:** `f, t, t, f, t` (5/5 Correct).


---

### Topic 15 & 16: Strings, Operations, Slicing Mechanics, and the 23 CBSE Methods

#### Raw Questions Given:
##### Conceptual QnA
1. Contrast `s.find("z")` and `s.index("z")` on the string `s = "cbse"`. State the exact output or behavior of each. When would a programmer prefer `find()` over `index()`?
2. Predict the exact 3-element tuple returned by each of the following calls to `partition()`:
   - Call A: `"user@mail.com".partition("@")`
   - Call B: `"data.structure.notes".partition(".")`
   - Call C: `"computer".partition("#")`
3. Predict the exact `list` output of each of the following three `split()` statements:
   - `"  Sun   Moon    Earth  ".split()`
   - `"red,,green,blue".split(",")`
   - `"red,,green,blue".split()`.
4. Predict the exact string slice result for each:
   - `"COMPUTATION"[2:8:2]`
   - `"PYTHON"[::-1]`
   - `"HELLO"[-1:-5:-1]`
   - `"CBSE"[1:50]`

##### True / False Statements
* Statement 1: If the delimiter passed to `s.partition(sep)` is not found in `s`, Python raises a `ValueError`.
* Statement 2: The expression `"-".join([10, 20, 30])` evaluates to `"10-20-30"`.
* Statement 3: The string method call `"pYTHON pROGRAM".capitalize()` evaluates to `"Python program"`.
* Statement 4: An out-of-range string slice expression such as `"CODE"[10:20]` generates an `IndexError`.
* Statement 5: The method call `"aaaa".count("aa")` returns `2` because Python counts only non-overlapping occurrences.

#### Raw Student Answer (Verbatim):
> 1. Both find and index are almost exactly the same, the difference arises ony when the provided substring doesnt exist in the string. For such a cae find returns 1 but index raises a ValueError.
> 2.A. ("user", "@", "mail.com")
> B. ("data", ".", "structure.notes")
> C. ("computer", "", "")
> 3. ["Sun", "Moon", "Earth"]
> ['red','','green','blue']
> ["red,,green,blue"]
> 4. "MUA"
> "NOHTYP"
> "OLLE"
> "BSE"
> f, f (gives TypeError), f, f, t

#### CBSE Evaluation & Model Answers:
*   **Q1:** **Correct (with minor typo note).** On failure, `find()` returns **`-1`** (negative one, not 1), while `index()` raises `ValueError: substring not found`. `find()` is preferred when absence is a normal condition to check via `if s.find("x") != -1:`. `index()` is preferred when absence is an exceptional error or in generic sequence code (since lists/tuples only have `.index()`, not `.find()`).
*   **Q2:** **100% Correct.**
    *   A: `('user', '@', 'mail.com')`
    *   B: `('data', '.', 'structure.notes')` (splits at first delimiter only)
    *   C: `('computer', '', '')` (missing delimiter returns original string and two empty strings).
*   **Q3:** **100% Correct.**
    *   Default `split()` groups whitespace: `['Sun', 'Moon', 'Earth']`.
    *   `split(",")` preserves empty items: `['red', '', 'green', 'blue']`.
    *   `split()` without commas or spaces finds no whitespace: `['red,,green,blue']`.
*   **Q4:** **100% Correct.**
    *   `"COMPUTATION"[2:8:2]` $\implies$ `"MUA"` (indices 2, 4, 6).
    *   `"PYTHON"[::-1]` $\implies$ `"NOHTYP"` (reversal).
    *   `"HELLO"[-1:-5:-1]` $\implies$ `"OLLE"` (negative indices stepping backward).
    *   `"CBSE"[1:50]` $\implies$ `"BSE"` (safe clamping).
*   **True/False Statements:** `f, f, f, f, t` (4/5 Correct).
    *   *Correction on Statement 3:* Statement 3 is **TRUE**. `s.capitalize()` capitalizes **only the first character** (index 0) and forces **all remaining characters in the entire string to lowercase**. Hence `"pYTHON pROGRAM".capitalize()` produces `"Python program"`. (Contrast with `.title()` which produces `"Python Program"`).


---

### Topic 17, 18 & 19: Lists, Operations, Methods, and Algorithms

#### Raw Questions Given:
##### Conceptual QnA
1. Contrast `lst.append([1, 2])` with `lst.extend([1, 2])` when called on `lst = [10, 20]`. Show the resulting list and its length for each. What happens if you call `lst.extend(50)`?
2. A programmer executes the following sequence of commands on list `a = [10, 20, 30]`:
   ```python
   a.insert(100, 40)
   a.insert(-100, 5)
   ```
   Does either call raise an `IndexError`? What is the exact resulting list?
3. What is the exact output or exception raised by each of the following?
   - Call A: `[1, 2, 3].remove(5)`
   - Call B: `[].pop()`
   - Call C: `[1, True, 0, False].count(True)`
   - Call D: `sum(["a", "b", "c"])`
4. Explain the difference between `my_list.sort()` and `sorted(my_list)` in terms of return value, in-place mutation, and memory identity (`id()`). What exception is raised if `my_list = [5, "apple"]` is sorted?

##### True / False Statements
* Statement 1: Slicing a list beyond its bounds, such as `[1, 2, 3][10:20]`, raises an `IndexError`.
* Statement 2: Lists in Python support a `.find()` method that returns `-1` when an element is not present.
* Statement 3: The assignment `grid = [[0] * 3] * 3` creates a $3 \times 3$ grid where modifying `grid[0][0] = 5` inadvertently modifies index 0 of all three rows.
* Statement 4: `lst.pop(0)` removes and returns the first element of `lst`.
* Statement 5: The built-in `sum([10, 20, 30], 5)` evaluates to `65` because the optional `start` parameter defaults to 0 and adds to the total sum.

#### Raw Student Answer (Verbatim):
> 1. append add a element at the end of the list, irrspective of the type of the added element. If element is intger it adds a integer but if it is a list or some other tuple it adds the whole iterable as a single element. lst.append([1, 2]) => [10, 20, [1, 2]]
> While xtends the list by adding the elements of the iterable provide as individual elements within the list. lst.extend([1, 2]) => [10, 20, 1, 2]
> 2. No, after the two commands the list is [5, 10, 20, 30, 40]
> 3. A. Index eror as 5 isnt present in the list
> B. IndexError as the list is empty
> C. 2
> D. TypeError as addition isnt possible between int and str
> 4. sort function sorts the list by changing the object directly and returns None, ie, the original list is changed. sorted function sorts the list and returns a new list object, ie, the original one is preserved and you get a new sorted list. 
> f, f, t, f, t

#### CBSE Evaluation & Model Answers:
*   **Q1:** **Mostly Correct (1 omission).** Accurate distinction between appending as a single object vs extending by iterating. If `lst.extend(50)` is called, Python raises **`TypeError: 'int' object is not iterable`** because `extend` demands an iterable argument.
*   **Q2:** **100% Correct.** Neither raises an error. `insert` clamps index $\ge \text{len}$ to the end and index $\le -\text{len}$ to the beginning: `[5, 10, 20, 30, 40]`.
*   **Q3:** **Mostly Correct (1 exception correction):**
    *   Call A: Raises **`ValueError: list.remove(x): x not in list`** (NOT IndexError! `remove()` searches by *value*, and missing values trigger `ValueError`).
    *   Call B: Raises `IndexError: pop from empty list` (Correct).
    *   Call C: Returns `2` (Correct: `True == 1`).
    *   Call D: Raises `TypeError: unsupported operand type(s) for +: 'int' and 'str'` (Correct).
*   **Q4:** **Correct.** `sort()` mutates in place, keeps `id()` unchanged, and returns `None`. `sorted()` returns a new list with a different `id()`. Sorting `[5, "apple"]` raises `TypeError: '<' not supported between instances of 'str' and 'int'`.
*   **True/False Statements:** `f, f, t, t, t` (4/5 Correct).
    *   *Correction on Statement 4:* Statement 4 is **TRUE**. `lst.pop([index])` accepts an optional index parameter. Calling `lst.pop(0)` removes and returns the element at index 0 (the first element).


---

### Topic 20 & 21: Tuples, Immutability, Operations, and Built-ins

#### Raw Questions Given:
##### Conceptual QnA
1. What is the data type and value of each of the following four variables?
   - `a = (10)`
   - `b = (10,)`
   - `c = 10, 20, 30`
   - `d = ()`
2. Consider the tuple `t = (1, [10, 20], 3)`.
   - What happens if a programmer executes `t[1].append(30)`?
   - What happens if a programmer executes `t[1] = [10, 20, 30]`?
   Explain the difference in terms of object references and tuple immutability.
3. Predict the exact output and data type for each of the following expressions:
   - `sorted((4, 1, 3, 2))`
   - `(1, 2) + (3, 4)`
   - `(1, 2) * 0`
   - `(1, 2) * -3`
4. If `t = (10, 20, 30)`, what exact exception is raised by each of the following erroneous statements?
   - `x, y = t`
   - `t.index(99)`
   - `t.append(40)`
   - `min(())`

##### True / False Statements
* Statement 1: Calling `sorted((5, 2, 8))` returns the tuple `(2, 5, 8)`.
* Statement 2: The method `t.find(10)` returns `-1` if integer 10 is missing from tuple `t`.
* Statement 3: The operation `(1, 2) + [3, 4]` produces the combined tuple `(1, 2, 3, 4)`.
* Statement 4: Tuples can be used as keys in Python dictionaries, but lists cannot.
* Statement 5: Slicing a tuple, such as `(1, 2, 3, 4)[1:3]`, returns a new tuple `(2, 3)`.

#### Raw Student Answer (Verbatim):
> 1. Except a all are tuple. a = 10; b=(10) (a tuple with single element); c = (10, 20, 30);  = () (empty tuple)
> 2. t[1].append(30) makes the tuple (1, [10, 20, 30], 3) as here we are changing the list which is mutable while the tuple remains the sasme as it stores a obj refrence for the list.
> But t[1] = [10, 20, 30] raises a TypeError as this time we are changing the tuple by assigning one of its element with something else contyradicting its immutablity
> 3. [1, 2, 3, 4]
> (1, 2, 3, 4)
> ()
> ()
> 4. ValueError
> ValueError
> AttributeError
> TypeError
> f, t, f, t, t

#### CBSE Evaluation & Model Answers:
*   **Q1:** **100% Correct.** `a` is `int` (value 10); `b` is `tuple` (`(10,)`); `c` is `tuple` (`(10, 20, 30)`); `d` is empty `tuple` (`()`).
*   **Q2:** **100% Correct.** Accurate explanation: `t[1].append(30)` mutates the inner mutable list in place without modifying the reference address stored by the tuple. `t[1] = [...]` attempts to rebind index 1 of the tuple, violating tuple immutability and raising `TypeError: 'tuple' object does not support item assignment`.
*   **Q3:** **100% Correct.** `sorted()` returns `list [1, 2, 3, 4]`. Concatenation returns `tuple (1, 2, 3, 4)`. Non-positive repetition produces empty tuples `()`.
*   **Q4:** **Mostly Correct (1 exception correction):**
    *   `x, y = t`: `ValueError: too many values to unpack (expected 2)` (Correct).
    *   `t.index(99)`: `ValueError: tuple.index(x): x not in tuple` (Correct).
    *   `t.append(40)`: `AttributeError: 'tuple' object has no attribute 'append'` (Correct).
    *   `min(())`: **`ValueError: min() iterable argument is empty`** (NOT TypeError! Empty sequences passed to `min()` or `max()` raise `ValueError`).
*   **True/False Statements:** `f, f, f, t, t` (4/5 Correct).
    *   *Correction on Statement 2:* Statement 2 is **FALSE**. Tuples do **NOT** have a `.find()` method! Calling `t.find(10)` raises **`AttributeError: 'tuple' object has no attribute 'find'`** (only strings support `.find()`; sequences like lists and tuples only have `.index()`).


---

### Topic 22, 23 & 24: Dictionaries, Mutability, Methods, and Algorithms

#### Raw Questions Given:
##### Conceptual QnA
1. Examine the following four proposed dictionary declarations. For each, state whether it is **Valid** or **Raises Exception**. If it raises an exception, name the exception and explain why:
   - `d1 = {1: "one", "pi": 3.14, (1, 2): "point"}`
   - `d2 = {[1, 2]: "numbers"}`
   - `d3 = {(1, [2, 3]): "nested"}`
   - `d4 = {True: "yes", 1: "one"}` *(What does `d4` contain and what is its length?)*
2. Trace the exact printed output of the following sequence:
   ```python
   info = {"user": "admin"}
   val1 = info.setdefault("user", "guest")
   val2 = info.setdefault("role", "manager")
   print("val1:", val1)
   print("val2:", val2)
   print("info:", info)
   ```
3. Contrast `del d["key"]`, `d.pop("key")`, and `d.pop("key", "default")` when `"key"` is **missing** from `d`. What is the exact behavior of each?
4. A student runs `sorted({"c": 100, "a": 500, "b": 200})`. What is the exact return value and data type? Does it sort by keys or by values?

##### True / False Statements
* Statement 1: In Python dictionaries, searching for a key using `key in d` checks whether `key` is in the dictionary's keys, not its values.
* Statement 2: The method `d.popitem()` on an empty dictionary returns `None`.
* Statement 3: The method `dict.fromkeys(["a", "b", "c"], 0)` creates the dictionary `{'a': 0, 'b': 0, 'c': 0}`.
* Statement 4: Executing `d.get("missing_key")` raises a `KeyError`.
* Statement 5: The keyword `del` can be used to remove an entry from a dictionary via `del d[key]`.

#### Raw Student Answer (Verbatim):
> 1. d2 raises TypeError as list is a mutable obj and hence cannot be used as keys. For rest thy are valid
> d4 is {1: "one"} length is 1 as True == 1
> 2. {"user": "guest"}
> {"user": "admin", "role": "manager"}
> {"user": "admin"}
> 3. the first 2 raise KeyError while the third one returns "default"
> 4. ["c", "b", "a"] list type. Sorted by keys
> idk, f, t, f, t

#### CBSE Evaluation & Model Answers:
*   **Q1:** **Mostly Correct (1 missed exception):**
    *   `d1`: **Valid** (all keys are immutable).
    *   `d2`: **Raises `TypeError: unhashable type: 'list'`** (Correct: lists are mutable).
    *   `d3`: **Raises `TypeError: cannot use 'tuple' as a dict key (unhashable type: 'list')`**! (A tuple is only hashable if **all** of its elements are hashable; containing a mutable list makes the tuple unhashable).
    *   `d4`: Contains `{True: 'one'}` with `len(d4) == 1` because `True == 1` and `hash(True) == hash(1)`. The value `"yes"` is overwritten by `"one"`.
*   **Q2:** **Model Trace Correction:** `setdefault(k, default)` returns the **value** of key `k`, not a dictionary:
    *   `val1 = info.setdefault("user", "guest")` $\implies$ `"user"` exists, returns existing value `"admin"`.
    *   `val2 = info.setdefault("role", "manager")` $\implies$ `"role"` missing, inserts `'role': 'manager'` and returns `"manager"`.
    *   Outputs:
        - `val1: admin`
        - `val2: manager`
        - `info: {'user': 'admin', 'role': 'manager'}`
*   **Q3:** **100% Correct.** `del d["key"]` and `d.pop("key")` both raise `KeyError: 'key'`, whereas `d.pop("key", "default")` safely catches the absence and returns `"default"`.
*   **Q4:** **Mostly Correct (ascending sort order note).** Returns **`['a', 'b', 'c']`** (data type `list`, sorted in ascending order of **keys**).
*   **True/False Statements:** `t, f, t, f, t` (4/5 Correct).
    *   *Clarification on Statement 1:* Statement 1 is **TRUE**. In Python, `x in d` strictly checks dictionary **keys** (`d.keys()`). To search values, you must explicitly write `x in d.values()`.


---

### Topic 22, 23 & 24: Dictionaries, Mutability, Methods, and Algorithms

#### Raw Questions Given:
##### Conceptual QnA
1. Examine the following four proposed dictionary declarations. For each, state whether it is **Valid** or **Raises Exception**. If it raises an exception, name the exception and explain why:
   - `d1 = {1: "one", "pi": 3.14, (1, 2): "point"}`
   - `d2 = {[1, 2]: "numbers"}`
   - `d3 = {(1, [2, 3]): "nested"}`
   - `d4 = {True: "yes", 1: "one"}` *(What does `d4` contain and what is its length?)*
2. Trace the exact printed output of the following sequence:
   ```python
   info = {"user": "admin"}
   val1 = info.setdefault("user", "guest")
   val2 = info.setdefault("role", "manager")
   print("val1:", val1)
   print("val2:", val2)
   print("info:", info)
   ```
3. Contrast `del d["key"]`, `d.pop("key")`, and `d.pop("key", "default")` when `"key"` is **missing** from `d`. What is the exact behavior of each?
4. A student runs `sorted({"c": 100, "a": 500, "b": 200})`. What is the exact return value and data type? Does it sort by keys or by values?

##### True / False Statements
* Statement 1: In Python dictionaries, searching for a key using `key in d` checks whether `key` is in the dictionary's keys, not its values.
* Statement 2: The method `d.popitem()` on an empty dictionary returns `None`.
* Statement 3: The method `dict.fromkeys(["a", "b", "c"], 0)` creates the dictionary `{'a': 0, 'b': 0, 'c': 0}`.
* Statement 4: Executing `d.get("missing_key")` raises a `KeyError`.
* Statement 5: The keyword `del` can be used to remove an entry from a dictionary via `del d[key]`.

#### Raw Student Answer (Verbatim):
> 1. d2 raises TypeError as list is a mutable obj and hence cannot be used as keys. For rest thy are valid
> d4 is {1: "one"} length is 1 as True == 1
> 2. {"user": "guest"}
> {"user": "admin", "role": "manager"}
> {"user": "admin"}
> 3. the first 2 raise KeyError while the third one returns "default"
> 4. ["c", "b", "a"] list type. Sorted by keys
> idk, f, t, f, t

#### CBSE Evaluation & Model Answers:
*   **Q1:** **Mostly Correct (1 missed exception):**
    *   `d1`: **Valid** (all keys are immutable).
    *   `d2`: **Raises `TypeError: unhashable type: 'list'`** (Correct: lists are mutable).
    *   `d3`: **Raises `TypeError: cannot use 'tuple' as a dict key (unhashable type: 'list')`**! (A tuple is only hashable if **all** of its elements are hashable; containing a mutable list makes the tuple unhashable).
    *   `d4`: Contains `{True: 'one'}` with `len(d4) == 1` because `True == 1` and `hash(True) == hash(1)`. The value `"yes"` is overwritten by `"one"`.
*   **Q2:** **Model Trace Correction:** `setdefault(k, default)` returns the **value** of key `k`, not a dictionary:
    *   `val1 = info.setdefault("user", "guest")` $\implies$ `"user"` exists, returns existing value `"admin"`.
    *   `val2 = info.setdefault("role", "manager")` $\implies$ `"role"` missing, inserts `'role': 'manager'` and returns `"manager"`.
    *   Outputs:
        - `val1: admin`
        - `val2: manager`
        - `info: {'user': 'admin', 'role': 'manager'}`
*   **Q3:** **100% Correct.** `del d["key"]` and `d.pop("key")` both raise `KeyError: 'key'`, whereas `d.pop("key", "default")` safely catches the absence and returns `"default"`.
*   **Q4:** **Mostly Correct (ascending sort order note).** Returns **`['a', 'b', 'c']`** (data type `list`, sorted in ascending order of **keys**).
*   **True/False Statements:** `t, f, t, f, t` (4/5 Correct).
    *   *Clarification on Statement 1:* Statement 1 is **TRUE**. In Python, `x in d` strictly checks dictionary **keys** (`d.keys()`). To search values, you must explicitly write `x in d.values()`.



---

### Topic 26: The `math` Module

#### Raw Questions Given:
##### Conceptual QnA
1. Predict the exact return value and data type for each of the following:
   - `math.ceil(-3.7)`
   - `math.floor(-3.7)`
   - `math.pow(3, 2)`
   - `math.fabs(-10)`
2. What exact exception is raised if a student runs `math.sqrt(-16)`? How does `math.pow(4, 0.5)` differ from `math.sqrt(4)`?
3. If a student wants to calculate the sine of $30^\circ$, why does `math.sin(30)` produce `-0.9880316...` instead of `0.5`? Show the exact Python expression required to calculate $\sin(30^\circ)$ correctly.

##### True / False Statements
* Statement 1: The function `math.floor(5.8)` returns the floating-point value `5.0`.
* Statement 2: The expression `type(math.sqrt(9))` evaluates to `<class 'float'>`.
* Statement 3: The `math` module will automatically return a `complex` number if a negative number is passed to `math.sqrt()`.
* Statement 4: `math.ceil(7.0)` returns `7`.
* Statement 5: The trigonometric functions in Python's `math` module expect angles measured in degrees.

#### Raw Student Answer (Verbatim):
> 1. -3, -4, 9.0, 10.0
> 2. ValueError. Nothing
> 3. The different answer occurs because math.sin expects t angle to be in radian instead of degree. the student should use math.sin(math.radians(30))
> f, t, f, t, f

#### CBSE Evaluation & Model Answers:
*   **Q1:** **100% Correct.** `math.ceil(-3.7)` returns `int -3`; `math.floor(-3.7)` returns `int -4`; `math.pow(3, 2)` returns `float 9.0`; `math.fabs(-10)` returns `float 10.0`.
*   **Q2:** **100% Correct.** Raises `ValueError: math domain error`. Both `math.pow(4, 0.5)` and `math.sqrt(4)` return float `2.0`.
*   **Q3:** **100% Correct.** Trigonometric functions expect angles in radians. Correct formulation: `math.sin(math.radians(30))` or `math.sin(30 * math.pi / 180)`.
*   **True/False Statements:** `f, t, f, t, f` (5/5 Correct).
