# Unit 2: Computational Thinking and Programming-I (Topics 03–05)

---

## 03. Python Execution Modes & Core Features

- **Mental model:**
  - **Interactive Mode (REPL):** Like having a live phone conversation with a calculator. You speak a sentence (`2 + 5`), it replies immediately (`7`), but once you hang up the phone (close terminal), the conversation is gone forever without a transcript.
  - **Script Mode:** Like writing, proofreading, and mailing a letter. You type the full set of instructions into a file (`script.py`), save it to the hard drive, and hand it to the Python interpreter to read and execute from start to finish. If you want a response sent back, you must explicitly write `print()`.

- **Key facts / definitions (CBSE Standard):**
  - **Features of Python:**
    1. *High-level:* Abstraction from low-level hardware; machine-independent and human-readable.
    2. *Interpreted:* Executes source code line-by-line via bytecode compilation on the Python Virtual Machine (PVM).
    3. *Dynamically Typed:* Variable types do not need to be declared; types are bound to values (objects) at runtime, not to variable names.
    4. *Case-sensitive:* Treats uppercase and lowercase letters as distinct (`Value` $\neq$ `value`).
    5. *Extensible & Portable:* Runs without modifications across Linux, Windows, macOS; can interface with C/C++.
    6. *Batteries Included:* Vast standard library providing built-in support for math, statistics, file handling, and networking.
  - **Interactive Mode vs Script Mode Comparison:**

| Feature | Interactive Mode (REPL) | Script Mode |
|---|---|---|
| **Primary Prompt** | `>>>` (Secondary continuation prompt: `...`) | None (runs from terminal via `python file.py` or IDE Run button) |
| **Execution Style** | Immediate evaluation statement-by-statement. | Sequential batch execution of the entire file. |
| **Output Display** | Expressions automatically echo their evaluated result to stdout. | Expressions must be passed to `print()` to output to screen. |
| **Storage / Persistence** | Non-persistent; code vanishes when the window or session closes. | Persistent; saved as `.py` files on secondary storage. |
| **Typical Use** | Fast syntax prototyping, module exploration, debugging snippets. | Developing practical assignments, modules, and full programs. |

- **Worked example:**
  - In Interactive Mode:
    ```python
    >>> 10 + 20
    30
    >>> a = 5
    >>> a * 4
    20
    ```
  - In Script Mode (`calc.py`):
    ```python
    10 + 20       # Executed, but nothing displays to console!
    a = 5
    a * 4         # Executed, but nothing displays!
    print(10 + 20)  # Output: 30
    print(a * 4)    # Output: 20
    ```

- **Common exam mistakes:**
  - Expecting script mode to automatically print expression results without `print()` statements.
  - Forgetting the primary prompt symbol (`>>>`) when asked in viva or 1-mark theory questions.

---

## 04. Character Set & The 5 Python Tokens

- **Mental model:**
  Think of learning human English grammar:
  - The **Character Set** is the English alphabet (letters A–Z, punctuation marks, spaces).
  - A **Token** is a single vocabulary word constructed from that alphabet.
  - Just as English classifies words into nouns, verbs, adjectives, prepositions, and conjunctions, Python classifies every token into:
    1. *Keywords* (the language's reserved grammar words).
    2. *Identifiers* (the nouns / names you invent).
    3. *Literals* (the concrete values / data facts).
    4. *Operators* (the action verbs performing arithmetic or logic).
    5. *Punctuators* (the punctuation organizing clauses and lists).

- **Key facts / definitions (CBSE Standard):**
  - **Character Set:** The set of valid characters recognized by the Python language:
    - Letters: `A–Z`, `a–z`
    - Digits: `0–9`
    - Special symbols: `+ - * / % ** // == != < > <= >= = ( ) [ ] { } , : . ; ' " # \ @ _`
    - Whitespace: Blank space, tab (`\t`), newline (`\n`), carriage return (`\r`).
    - Other characters: Python 3 supports the complete **Unicode** character set.
  - **Token (Lexical Unit):** The smallest individual element of a program that has meaning to the compiler/interpreter.
  - **The 5 Token Classifications:**
    1. **Keywords:**
       - Reserved words that convey a predefined syntactic meaning to the interpreter.
       - Cannot be used as variable, function, or class names.
       - *Crucial Rule:* In Python 3, **only three keywords are capitalized**: `True`, `False`, and `None`. All other 32+ keywords are lowercase (`def`, `class`, `if`, `elif`, `else`, `while`, `for`, `in`, `is`, `import`, `from`, `global`, `lambda`, `pass`, `return`, `raise`, `try`, `except`, `finally`, `with`, `as`, `del`, etc.).
    2. **Identifiers:**
       - User-defined names used to label program entities (variables, functions, classes).
       - *CBSE Rules for Identifiers:*
         - Must begin with an alphabet letter (`A–Z`, `a–z`) or an underscore (`_`).
         - **Cannot begin with a digit** (`0–9`).
         - Can consist of letters, digits, and underscores only.
         - Cannot contain spaces or special punctuation (`-`, `@`, `$`, `%`, `.`, `!`).
         - Cannot be a reserved keyword.
         - Strictly case-sensitive (`Total` $\neq$ `total`).
         - Can be of arbitrary length.
    3. **Literals (Constants):**
       - Data items that have a fixed, constant value directly embedded in the program text.
       - *Numeric Literals:*
         - *Integer:* Decimal (`42`), Binary (`0b1010`), Octal (`0o77`), Hexadecimal (`0x1F`).
         - *Floating-point:* Fractional (`3.14159`) or Scientific/Exponent notation (`mEn` $\equiv m \times 10^n$, e.g., `2.5e3` $= 2500.0$, `1.2e-2` $= 0.012$). Mantissa $m$ can be integer or float; exponent $n$ must be an integer.
         - *Complex:* Consists of a real part and an imaginary part (`a + bj`), where `j` represents $\sqrt{-1}$.
       - *String Literals:* Sequence of characters enclosed in quotes.
         - Single-line: Single quotes (`'...'`) or double quotes (`"..."`).
         - Multi-line: Triple quotes (`'''...'''` or `"""..."""`) or backslash continuation (`\`).
         - Escape sequences: Non-graphic characters preceded by a backslash (`\n` newline, `\t` tab, `\\` backslash, `\'` single quote, `\"` double quote).
         - Raw strings: Prefixed with `r` or `R` (e.g., `r"C:\test\notes"` suppresses escape sequence interpretation).
       - *Boolean Literals:* `True` (equivalent to integer 1 in numeric contexts) and `False` (0).
       - *Special Literal:* `None` (indicates absence of a value or null state).
    4. **Operators:**
       - Symbols or keywords that compute a result when applied to operands (e.g., `+`, `-`, `*`, `/`, `//`, `%`, `**`, `==`, `!=`, `and`, `or`, `not`, `is`, `in`).
    5. **Punctuators (Delimiters):**
       - Symbols used to group, delimit, and format syntactic structures (`( )`, `[ ]`, `{ }`, `,`, `:`, `.`, `;`, `@`, `=`, `+=`, `-=`, etc.).

- **Worked example:**
  - Token Breakdown Table for:
    ```python
    total = (count * 1.5e2) + 25
    ```

| Lexical Item | Token Category | Specific Sub-type |
|---|---|---|
| `total` | **Identifier** | User-defined variable |
| `=` | **Operator** (or Punctuator) | Assignment operator |
| `(` | **Punctuator** | Grouping delimiter |
| `count` | **Identifier** | User-defined variable |
| `*` | **Operator** | Arithmetic multiplication |
| `1.5e2` | **Literal** | Floating-point (scientific notation: $150.0$) |
| `)` | **Punctuator** | Grouping delimiter |
| `+` | **Operator** | Arithmetic addition |
| `25` | **Literal** | Decimal integer |

  - Valid vs Invalid Identifiers Table:

| Identifier | Validity | Reason / Rule Violated |
|---|---|---|
| `_my_var` | **Valid** | Starts with underscore, contains valid characters. |
| `3rd_score` | **INVALID** | Cannot start with a digit (`3`). |
| `total-sum` | **INVALID** | Hyphen `-` is an arithmetic operator, not permitted in identifiers. |
| `my sum` | **INVALID** | Spaces are not allowed inside identifiers. |
| `def` | **INVALID** | `def` is a reserved Python keyword. |
| `Def` | **Valid** | Python is case-sensitive; `Def` is not a keyword (though poor practice). |
| `True` | **INVALID** | `True` is a reserved Boolean keyword. |
| `true` | **Valid** | Lowercase `true` is not a keyword in Python (unlike JavaScript/C++). |
| `salary$bonus` | **INVALID** | Special character `$` is not allowed. |

- **Common exam mistakes:**
  - Classifying hyphenated identifiers like `net-pay` as valid (the hyphen `-` is interpreted as subtraction).
  - Assuming `_` (underscore) is invalid at the start of a variable (leading underscores are completely legal).
  - Confusing `true` with `True` (only `True` is a keyword; `true` is treated as a regular identifier).
  - Misinterpreting scientific notation: `2e-3` is $2 \times 10^{-3} = 0.002$ (float), not an integer.

---

## 05. Variables, L-value vs R-value, and Comments

- **Mental model:**
  - **Memory in C vs Python:**
    - In C: A variable is a physical metal mailbox with a fixed label. Putting 10 in it means placing the number 10 into that metal box.
    - In Python: Objects (numbers, strings) float in a storage room (the heap). A variable is a paper sticky-tag tied by a string to an object.
    - When you write `x = 10`, you stick the tag `x` onto object `10`.
    - When you later write `x = "apple"`, you untie tag `x` from `10` and tie it onto `"apple"`.
  - **L-value vs R-value:**
    - **L-value (Left-hand side):** Must be a **sticky-tag holder** (a valid storage location or reference capable of being assigned).
    - **R-value (Right-hand side):** Must be the **actual object or value** being assigned (any valid computation or literal).
    - You can stick a tag onto a box (`x = 10`), but you cannot stick a box onto a tag (`10 = x`).

- **Key facts / definitions (CBSE Standard):**
  - **Variable:** A named reference to an object in memory. Created automatically upon first assignment.
  - **Dynamic Typing:** Python variables can refer to objects of different data types during the course of program execution.
    ```python
    val = 100       # val references an int
    val = "Hello"   # val now references a str (completely legal)
    ```
  - **L-value vs R-value:**
    - **L-value ("Locator Value" / Left-hand side):** An expression or identifier that refers to an assignable memory address or object reference. It appears on the left side of `=`.
      - Examples of valid L-values: `x`, `student_name`, `my_list[0]`, `person.age`.
    - **R-value ("Read Value" / Right-hand side):** Any valid expression, variable, or literal that evaluates to a value. It appears on the right side of `=`.
    - *The Syntax Rule:* An expression that calculates a value (like `a + b` or `5 * 2`) is an R-value only. It does not represent an assignable memory location.
      - Therefore: `a + b = 25` raises `SyntaxError: cannot assign to expression`.
  - **Multiple Assignment:**
    - Assigning one value to multiple variables: `x = y = z = 0` (all three names point to the same integer object `0`).
    - Multiple values to multiple variables (tuple unpacking): `a, b = 10, 20` (`a` gets `10`, `b` gets `20`).
    - Swapping values without a temporary variable: `a, b = b, a`.
  - **Comments in Python:**
    - Comments are non-executable text annotations meant for developers to document program logic.
    - Ignored by the Python parser/compiler.
    - *Single-line Comments:* Begin with a hash symbol (`#`) and continue to the end of the line.
    - *Multi-line Comments:*
      - Consecutive `#` symbols on each line.
      - Unassigned triple-quoted string literals (`'''...'''` or `"""..."""`). When not assigned to a variable or placed as a function/module docstring, Python evaluates the string object and immediately discards it from memory, effectively behaving as a multi-line comment.

- **Worked example:**
  - Tracing multiple assignment and value swapping:
    ```python
    x, y = 10, 25
    x, y = y, x + 5
    print("x:", x, "y:", y)
    ```
  - *Trace:*
    1. Initially, `x` references `10`, `y` references `25`.
    2. In `x, y = y, x + 5`:
       - Right-hand side (R-values) are evaluated first: `(y, x + 5) \implies (25, 10 + 5) \implies (25, 15)`.
       - Left-hand side (L-values) are bound: `x` is assigned `25`, `y` is assigned `15`.
    3. Output: `x: 25 y: 15`.

- **Common exam mistakes:**
  - Writing `x + 10 = y` and expecting Python to solve for `x` (raises `SyntaxError`).
  - Assuming Python variables are fixed-type containers like in C/Java.
  - Forgetting that in multiple assignment `a, b = b, a + b`, all RHS expressions are completely evaluated before any LHS assignments take place.

