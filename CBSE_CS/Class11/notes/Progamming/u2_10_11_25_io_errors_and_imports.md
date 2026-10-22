# Unit 2: Computational Thinking and Programming-I (Topics 10, 11, 25)

---

## 10. Console Input and Output

- **Mental model:**
  - **`input()`:** A receptionist sitting at the door with a clipboard. Whatever you hand the receptionist (even if it's the number 42 on a slip of paper), it is stamped and sealed in a **text envelope (`str`)**. If your computer needs to do math with it, you must open the envelope and convert it into a numeric token using `int()` or `float()`.
  - **`print()`:** A megaphone shouting items to the screen. By default, it takes a breath between words (`sep=' '`) and steps off stage onto a new line when finished (`end='\n'`). You can change the megaphone's punctuation by modifying `sep` and `end`.

- **Key facts / definitions (CBSE Standard):**
  - **The `input()` Function:**
    - Syntax: `input([prompt])`
    - Displays the optional string prompt to standard output and waits for user keyboard input followed by `Enter`.
    - **CRITICAL CBSE RULE:** The `input()` function **always returns data of type `str` (string)**, regardless of what the user types.
    - **Explicit Conversion for Numerics:**
      - Integers: `num = int(input("Enter number: "))`
      - Floats: `price = float(input("Enter price: "))`
    - If user enters characters that do not conform to the expected numeric format (e.g., typing `"ten"` or `"4.5"` into `int()`), Python crashes with a runtime **`ValueError`**.
  - **The `print()` Function:**
    - Syntax: `print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)`
    - Evaluates expressions, converts each object to a string, and outputs them to standard output.
    - **`sep` Parameter (Separator):**
      - Specifies the string placed between individual arguments.
      - **Default:** Single space (`' '`).
      - Example: `print("A", "B", "C", sep="-")` $\implies$ `A-B-C`.
      - Example: `print("A", "B", "C", sep="")` $\implies$ `ABC` (no space).
    - **`end` Parameter (Line Terminator):**
      - Specifies the string appended after the last argument has been printed.
      - **Default:** Newline character (`'\n'`).
      - Example: `print("Hello", end=" ")` keeps the cursor on the same line so the next `print()` continues immediately beside it.

- **Worked example:**
  - Multi-line `print()` output trace:
    ```python
    print("Roll", "Name", "Marks", sep="\t", end="\n" + "-"*25 + "\n")
    print(101, "Aman", 92, sep="\t")
    print(102, "Rohit", 88, sep="\t")
    ```
  - Console Output:
    ```text
    Roll    Name    Marks
    -------------------------
    101     Aman    92
    102     Rohit   88
    ```

- **Common exam mistakes:**
  - Attempting arithmetic directly on `input()` without type casting:
    `a = input(); b = input(); print(a + b)` will perform **string concatenation** (`"10" + "20" = "1020"`), not addition!
  - Assuming `print("A", "B", sep="*")` prints an asterisk at the end (the separator `sep` is placed strictly *between* arguments; `end` goes at the end).

---

## 11. Errors: Syntax, Run-Time, and Logical

- **Mental model:**
  Think of cooking a recipe from a cookbook:
  1. **Syntax Error:** The recipe is printed in gibberish with missing letters: *"bake cake at 350 for 30"* (missing word 'minutes'). You cannot even begin cooking; the instructions violate the rules of grammar.
  2. **Run-time Error (Exception):** The recipe is grammatically flawless, but step 4 tells you to *"pour 500 mL of milk"* and when you open the fridge, there is no milk (`KeyError` / `FileNotFoundError`), or step 5 tells you to *"divide the batter among 0 pans"* (`ZeroDivisionError`). You stop dead in the middle of cooking and the kitchen catches fire (crashes).
  3. **Logical Error:** You follow the recipe perfectly from start to finish, the cake bakes, but when you taste it, it is salty because the chef accidentally wrote *"2 cups of salt"* instead of *"2 cups of sugar"*. Nothing crashed, but the result is completely wrong.

- **Key facts / definitions (CBSE Standard):**

| Error Category | Formal Definition | When Detected? | Impact on Program Execution | Common Examples |
|---|---|---|---|---|
| **Syntax Error** | Violation of the formal grammatical rules and syntax of Python. | **Parse-Time / Compile-Time (Before execution begins)** | The Python parser rejects the file immediately. **Not a single line of code is executed**, even lines preceding the error. | Missing colon `:` after `if`/`for`/`def`, unclosed quotes/brackets, misspelled keywords (`whle`), invalid variable names (`1st = 5`), `IndentationError` (subclass of `SyntaxError`). |
| **Run-time Error (Exception)** | The syntax is valid, but an impossible or illegal operation is encountered during active execution. | **Execution-Time (During program run)** | The program executes normally line-by-line until the offending statement is reached, then halts abruptly and outputs a traceback. | `ZeroDivisionError` (`x / 0`), `TypeError` (`'a' + 1`), `ValueError` (`int("abc")`), `IndexError` (`arr[10]` out of bounds), `KeyError` (missing dict key), `NameError` (undefined variable). |
| **Logical Error (Bug)** | The program is syntactically sound and runs without crashing, but generates **incorrect or unintended results** due to faulty logic/algorithm. | **Never detected by Python** | Program runs to completion, but output is wrong. Detected only via human verification or **testing**. | Using wrong arithmetic formulas (`avg = a + b / 2`), wrong operators (`<` instead of `>`), wrong loop ranges. |

- **Worked example:**
  - Diagnosing error types:
    ```python
    # Example 1: Syntax Error (Compile-time)
    print("Starting")
    if 5 > 2
        print("Bigger")
    # Output: SyntaxError: expected ':'
    # NOTE: "Starting" is NEVER printed!
    
    # Example 2: Run-time Error (Execution-time)
    print("Starting")
    x = 10 / 0
    print("Done")
    # Output: "Starting" IS printed, followed by ZeroDivisionError crash. "Done" is never reached.
    
    # Example 3: Logical Error
    def get_avg(a, b):
        return a + b / 2  # Missing parentheses: evaluates as a + (b/2)
    print(get_avg(10, 20))
    # Output: 20.0 (Expected 15.0). Program ran smoothly without errors!
    ```

- **Common exam mistakes:**
  - Claiming syntax errors occur while running the code (Syntax errors are caught during the initial AST parsing phase *before* execution).
  - Believing `IndentationError` is a runtime error (it is a compile-time syntax error).
  - Expecting Python to catch logical errors (Python only checks validity of execution, not correctness of business logic).

---

## 25. Python Modules and Namespaces

- **Mental model:**
  - **Module:** A toolbox with a specific label (e.g. `math.py`, `random.py`).
  - **Namespace (The Phonebook):** A dictionary in Python memory that pairs every name (identifier) with its corresponding object.
    - Think of the name *"Aman"*. If you are in Delhi, dialing Aman reaches the Delhi Aman. If you are in Mumbai, dialing Aman reaches the Mumbai Aman. The city code is like a module namespace (`delhi.aman` vs `mumbai.aman`).
    - Without namespaces, two variables or functions with the same name would overwrite each other.

- **Key facts / definitions (CBSE Standard):**
  - **What is a Module?**
    - A Python source file with a `.py` extension containing related functions, classes, and constants meant to be reused across different programs.
  - **What is a Namespace?**
    - A mapping from names (identifiers) to objects.
    - In Python, namespaces are implemented under the hood as standard Python **dictionaries** (`{'name': object_reference}`).
    - **Types of Namespaces in Python:**
      1. *Built-in Namespace:* Contains built-in functions (`print`, `len`, `input`, `int`). Created when Python starts up.
      2. *Global (Module) Namespace:* Contains names defined at the top-level of a module/file. Created when the module is imported or file is run.
      3. *Local Namespace:* Created inside a function when the function is called; destroyed when the function returns.
  - **Import Syntax Variations:**
    1. **`import module_name`:**
       - Imports the entire module into its own namespace.
       - Items inside the module must be accessed using **dot notation**: `module_name.item`.
       - *Advantage:* Complete namespace isolation; no naming collisions with local variables.
    2. **`from module_name import func1, func2`:**
       - Imports specific identifiers directly into the current (local/global) namespace.
       - Called directly: `func1()`.
       - *Drawback:* May shadow (overwrite) an existing variable or function with the same name.
    3. **`from module_name import *` (Wildcard Import):**
       - Imports all public names from the module directly into the local namespace.
       - **CBSE Note:** Discouraged because it clutters the namespace and creates ambiguity about where names originated.
    4. **Aliasing with `as`:**
       - Renames a module reference: `import math as m`.
       - **Important Rule:** Once an alias is assigned (`m`), the original name (`math`) is **not bound** in the namespace. Calling `math.sqrt()` raises `NameError`.

- **Worked example:**
  ```python
  # Namespace Collision Demonstration:
  from math import sqrt
  
  def sqrt(x):
      return "Overwritten local function!"
      
  print(sqrt(16))  # Calls the local function, shadowing math.sqrt!
  
  # Clean namespace approach:
  import math
  print(math.sqrt(16))  # 4.0 (Protected from local name shadowing)
  ```

- **Common exam mistakes:**
  - Calling a function without its module prefix when `import module` was used (e.g. typing `sqrt(9)` instead of `math.sqrt(9)`).
  - Attempting to use the original module name after defining an alias:
    `import math as m; print(math.pi)` raises `NameError: name 'math' is not defined`.

