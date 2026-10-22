# Unit 2: Computational Thinking and Programming-I (Topics 06–09)

---

## 06. Data Types in Python

- **Mental model:**
  Think of data types as specific storage classifications in a warehouse:
  - **Numbers (`int`, `float`, `complex`, `bool`):** Scalar quantities. Integers are whole counts with infinite capacity; floats are decimal measurements; complex numbers represent 2D vector coordinates ($a + bj$); booleans are single binary flags.
  - **Sequences (`str`, `list`, `tuple`):** Numbered conveyor belts where items sit in ordered numbered slots (indices $0, 1, 2, \dots$).
  - **Mappings (`dict`):** An office cubicle system where each room has a unique engraved nameplate (the key) and holds a specific object (the value).
  - **NoneType (`None`):** An empty pedestal indicating the deliberate absence of any object.

- **Key facts / definitions (CBSE Standard):**
  - **Data Type Classification Hierarchy:**
    1. **Numeric Types:**
       - **`int` (Integer):** Represents whole numbers. In Python 3, integers have **arbitrary precision** (limited only by available system RAM, preventing integer overflow).
       - **`bool` (Boolean):** Subtype of `int`. Has exactly two values: `True` (evaluates to integer `1`) and `False` (`0`).
       - **`float` (Floating Point):** 64-bit double-precision numbers using IEEE 754 standard. Includes fractional notation (`3.14`) and scientific exponent notation (`1.5e-3` $= 0.0015$).
       - **`complex` (Complex Numbers):** Numbers written as $a + bj$, where $a$ is the real part, $b$ is the imaginary part, and $j = \sqrt{-1}$.
         - Attributes: For `z = 2 + 5j`, `z.real` returns `2.0` and `z.imag` returns `5.0` (**always floats**).
    2. **Sequence Types (Ordered & 0-indexed):**
       - **`str` (String):** An ordered, immutable sequence of Unicode characters enclosed in quotes (`'...'`, `"..."`, `'''...'''`).
       - **`list`:** An ordered, mutable, heterogeneous collection enclosed in square brackets `[10, "apple", 3.14]`.
       - **`tuple`:** An ordered, immutable, heterogeneous collection enclosed in parentheses `(10, "apple", 3.14)`. Single-element tuples require a comma: `(5,)`.
    3. **Mapping Type:**
       - **`dict` (Dictionary):** An unordered (insertion-ordered in Python 3.7+) collection of key-value pairs `{k1: v1, k2: v2}`. Keys **must be immutable/hashable** (strings, numbers, tuples); values can be of any arbitrary type.
    4. **Set Types:**
       - **`set`:** Mutable, unordered collection of unique, immutable elements enclosed in `{1, 2, 3}`.
    5. **NoneType:**
       - Special data type having only one possible value: `None`. Represents void/null, unassigned states, or the default return value of functions that do not return explicitly.

- **Worked example:**
  ```python
  z = 3 + 4j
  print(type(z))         # <class 'complex'>
  print(z.real, z.imag)  # 3.0 4.0 (Both are floats!)
  
  t1 = (5)               # Just an integer inside parentheses!
  t2 = (5,)              # A single-element tuple!
  print(type(t1))        # <class 'int'>
  print(type(t2))        # <class 'tuple'>
  ```

- **Common exam mistakes:**
  - Writing `(5)` as a tuple (without a trailing comma, Python treats parentheses as grouping an integer expression).
  - Expecting `z.real` or `z.imag` to return an integer when whole numbers are used in complex literals (they are strictly `float`).
  - Using mutable objects (like lists or dictionaries) as dictionary keys (raises `TypeError: unhashable type: 'list'`).

---

## 07. Mutability vs Immutability

- **Mental model:**
  - **Immutable Objects (Carved in Stone):** Once created, the physical stone cannot be reshaped. If you want to change its value, you must discard that stone and carve an entirely new stone with a new address (`id()`).
  - **Mutable Objects (Dry-Erase Whiteboards):** The whiteboard retains its physical identity and memory location (`id()`), but you can erase, append, or rewrite items on it in place.

- **Key facts / definitions (CBSE Standard):**
  - **Immutable Data Types:**
    - Types whose values **cannot be changed in place** once allocated in memory.
    - Prescribed List: **`int`, `float`, `complex`, `bool`, `str`, `tuple`**.
    - Attempting in-place item assignment (e.g., `s = "hello"; s[0] = 'H'` or `t = (1, 2); t[0] = 99`) triggers:
      `TypeError: 'str'/'tuple' object does not support item assignment`.
  - **Mutable Data Types:**
    - Types whose contents **can be altered in place** without modifying the object's identity (`id()`).
    - Prescribed List: **`list`, `dict`, `set`**.
    - Operations like `list.append()`, `list.sort()`, `dict[key] = val` mutate the object in place and typically return `None`.
  - **Variable Aliasing & Memory Sharing:**
    - Multiple variable names can point to the same object in the heap.
    - If the object is mutable, modifying it via one alias reflects across all other aliases:
      ```python
      list_a = [1, 2, 3]
      list_b = list_a          # Aliasing: id(list_a) == id(list_b)
      list_b.append(4)
      print(list_a)            # [1, 2, 3, 4] -> list_a is modified!
      ```

- **Worked example:**
  - Memory Tracing of Immutable vs Mutable Variables:
    ```python
    # 1. Immutable integer re-binding:
    x = 10
    old_id = id(x)
    x = x + 1                # A new integer object 11 is created
    print(id(x) == old_id)   # False (New memory address!)

    # 2. Mutable list in-place mutation:
    nums = [1, 2]
    old_id = id(nums)
    nums.append(3)           # Mutated in place
    print(id(nums) == old_id)# True (Same memory address!)
    ```

- **Common exam mistakes:**
  - Believing that `x = x + 1` modifies the integer object `10` in place (integers are immutable; `x` is simply rebound to a newly created `11`).
  - Believing that a tuple containing a list cannot have the list modified (the tuple's references are immutable, but the nested list itself remains mutable).

---

## 08. Operators & Expressions

- **Mental model:**
  Operators are active mathematical engines processing inputs:
  - **Division `/` vs `//`:** True division `/` always produces a precise float. Floor division `//` acts like gravity, pulling the result down to the nearest integer floor towards $-\infty$.
  - **Modulo `%`:** Measures the leftover distance from the lower floor.
  - **Identity `is` vs Equality `==`:** `==` asks *"Do these two people look identical and weigh the same?"* (content check). `is` asks *"Are these two names referring to the exact same human being?"* (memory identity check).

- **Key facts / definitions (CBSE Standard):**
  - **Arithmetic Operators:**
    - `+`, `-`, `*`
    - `/` (True Division): Always returns a `float` in Python 3 (`4 / 2 \implies 2.0`).
    - `//` (Floor Division): Truncates to the largest integer less than or equal to the quotient ($\lfloor a/b \rfloor$).
      - Positive: `7 // 2 = 3`
      - Negative: `-7 // 2 = -4` (since $-3.5$ rounded towards $-\infty$ is $-4$).
    - `%` (Modulo / Remainder):
      - **Mathematical Formula:** $r = a - (b \times (a // b))$
      - **Sign Rule:** In Python, the sign of the remainder $r$ **always matches the sign of the divisor $b$**.
        - `-13 % 4 = 3` (Divisor is $+4 \implies$ result is $+3$)
        - `13 % -4 = -3` (Divisor is $-4 \implies$ result is $-3$)
    - `**` (Exponentiation): $x^y$.
  - **Relational Operators:** `<`, `>`, `<=`, `>=`, `==`, `!=`. Always produce a Boolean (`True` or `False`).
  - **Logical Operators (Short-Circuit Evaluation):**
    - `and`: If the first operand is falsy, returns it immediately without evaluating the second; otherwise returns the second operand.
    - `or`: If the first operand is truthy, returns it immediately without evaluating the second; otherwise returns the second operand.
    - `not`: Inverts truth value (`not True \implies False`).
  - **Identity Operators:**
    - `is`: Returns `True` if two variables reference the exact same object in memory (`id(a) == id(b)`).
    - `is not`: Returns `True` if two variables reference different memory locations.
  - **Membership Operators:**
    - `in`: Returns `True` if a value is found inside a sequence/collection. (In dictionaries, checks **keys**, not values!).
    - `not in`: Returns `True` if a value is absent from a sequence.
  - **Bitwise Operators:** `&` (AND), `|` (OR), `^` (XOR), `~` (NOT / Inversion: `~x = -x - 1`), `<<` (Left Shift), `>>` (Right Shift).

- **Worked example:**
  - Tracing Python's Modulo formula:
    - Compute `17 % -5`:
      1. $a // b = 17 // -5 = \lfloor -3.4 \rfloor = -4$.
      2. $r = a - (b \times (a // b)) = 17 - ((-5) \times (-4)) = 17 - 20 = -3$.
      3. (Matches divisor sign: $-5 < 0 \implies -3 < 0$).

- **Common exam mistakes:**
  - Expecting `-5 // 2` to return `-2` (it returns `-3` because floor rounds towards $-\infty$).
  - Forgetting that `5 == 5.0` is `True` (equality of values), but `5 is 5.0` is `False` (different data types and memory objects).

---

## 09. Operator Precedence & Type Conversion

- **Mental model:**
  - **Precedence Hierarchy:** Think of gravitational pull. Higher precedence operators pull their operands together first.
  - **Associativity:** When two operators have the same gravitational pull:
    - Almost all operators run **Left-to-Right** (like reading a sentence).
    - **Exponentiation `**` runs Right-to-Left** (like an exponent tower $2^{3^2}$).
  - **Type Conversion:**
    - *Implicit (Coercion):* Water flowing downhill naturally into a larger basin (no data lost, e.g. int to float).
    - *Explicit (Casting):* Pouring liquid forcefully into a specific mold (can spill/truncate data, or shatter if incompatible).

- **Key facts / definitions (CBSE Standard):**
  - **Operator Precedence Table (Highest to Lowest):**

| Priority | Operator Symbol | Description | Associativity |
|---|---|---|---|
| **1** | `()` | Parentheses (Grouping) | Left-to-Right |
| **2** | `**` | Exponentiation | **Right-to-Left** |
| **3** | `+x`, `-x`, `~x` | Unary Plus, Unary Minus, Bitwise NOT | Right-to-Left |
| **4** | `*`, `/`, `//`, `%` | Multiplication, Division, Floor Div, Modulo | Left-to-Right |
| **5** | `+`, `-` | Addition, Subtraction | Left-to-Right |
| **6** | `<<`, `>>` | Bitwise Shifts | Left-to-Right |
| **7** | `&` | Bitwise AND | Left-to-Right |
| **8** | `^` | Bitwise XOR | Left-to-Right |
| **9** | `\|` | Bitwise OR | Left-to-Right |
| **10** | `==`, `!=`, `<`, `>`, `<=`, `>=`, `is`, `is not`, `in`, `not in` | Comparison, Identity, Membership | Left-to-Right |
| **11** | `not` | Logical NOT | Right-to-Left |
| **12** | `and` | Logical AND | Left-to-Right |
| **13** | `or` | Logical OR | Left-to-Right |
| **14** | `=`, `+=`, `-=`, etc. | Assignment Operators | **Right-to-Left** |

  - **Chained Comparisons:**
    - Python evaluates `A op1 B op2 C` as `(A op1 B) and (B op2 C)` with short-circuit evaluation.
    - Example: `10 > 5 == True` $\implies$ `(10 > 5) and (5 == True)` $\implies$ `True and False` $\implies$ `False`.
  - **Implicit Type Conversion (Coercion):**
    - Done automatically by Python during runtime when mixed types are used in an expression.
    - Operands are promoted to the type with wider range (e.g., `int + float \implies float`).
  - **Explicit Type Conversion (Type Casting):**
    - Done manually by programmer using type constructors: `int()`, `float()`, `str()`, `bool()`, `list()`, `tuple()`.
    - **The 2 Critical Exam Traps:**
      1. `int("3.5")`: Passing a string with decimal characters to `int()` raises `ValueError`. Must use: `int(float("3.5"))`.
      2. **Truthiness & `bool()`:**
         - Falsy values: `0`, `0.0`, `0j`, `None`, `False`, `""`, `[]`, `()`, `{}`.
         - Any non-empty string or collection is **Truthy**: `bool("False") == True`, `bool("0") == True`, `bool(" ") == True`.

- **Worked example:**
  - Tracing Precedence:
    ```python
    res = 100 - 2 ** 2 ** 3 // 4 * 2
    # Step 1: Exponentiation (Right-to-Left): 2 ** 3 = 8 -> 2 ** 8 = 256
    # Expression becomes: 100 - 256 // 4 * 2
    # Step 2: Floor Division & Multiplication (Left-to-Right):
    # 256 // 4 = 64
    # 64 * 2 = 128
    # Step 3: Subtraction: 100 - 128 = -28
    ```

- **Common exam mistakes:**
  - Calculating `2 ** 3 ** 2` as $(2^3)^2 = 8^2 = 64$ (it evaluates right-to-left: $2^{(3^2)} = 2^9 = 512$).
  - Assuming `bool("False")` returns `False` (any non-empty string evaluates to `True`).
  - Assuming `int("12.3")` converts to `12` (it crashes with `ValueError`).
