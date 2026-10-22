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
