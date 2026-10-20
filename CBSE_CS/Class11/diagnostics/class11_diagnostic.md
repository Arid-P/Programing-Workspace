# Class 11 CBSE CS — Cold Diagnostic

> **Instructions:**
> - This is a cold diagnostic to assess your baseline knowledge.
> - Answer **True** or **False** from memory.
> - Do not use notes, code interpreters, or external references.
> - Fill in your answers in the `Answer: ` slots below.

---

1. `type(3+4j)` is `complex`.
Answer: True

2. `5 / 2` evaluates to `2`.
Answer: False, it evalutes to nothing as '5/2' is a sing. (If it is an integer expression then 2.5)

3. `-5 // 2` evaluates to `-3`.
Answer: True

4. `==` compares identity and `is` compares values.
Answer: False, its the opposite

5. Strings in Python are mutable.
Answer: False

6. `my_list.sort()` returns a new sorted list and leaves `my_list` unchanged.
Answer: False

7. `sorted((3,1,2))` returns a tuple.
Answer: false, it returns a list

8. `d.get("k")` raises `KeyError` if `"k"` is missing.
Answer:  False

9. `d.setdefault("k", 5)` inserts `"k": 5` if `"k"` is missing and returns the value for `"k"`.
Answer: IDK

10. `"abc".partition("b")` returns `('a', 'b', 'c')`.
Answer: IDK partition

11. `"hello".find("z")` returns `-1`, while `"hello".index("z")` raises `ValueError`.
Answer: 

12. `"a b  c".split()` returns `['a', 'b', 'c']`.
Answer: False

13. `list(range(2, 10, 3))` is `[2, 5, 8]`.
Answer: true

14. `break` skips only the current iteration and continues the loop.
Answer: False

15. After `a = b = []`, `a` and `b` are two independent lists.
Answer: f

16. `(5)` is a tuple with one element.
Answer: f

17. `x.extend([1,2])` and `x.append([1,2])` produce the same list.
Answer: f

18. `del d["k"]` removes the key `"k"` from dictionary `d`.
Answer:  IDK, there is a del keyword in python for dict??

19. `random.randint(1, 6)` can return `6`, and `random.randrange(1, 6)` can also return `6`.
Answer: T

20. `statistics.mode([1,2,2,3])` returns `2`.
Answer: IDK, I diont even remember mode.i only remember mean and median

21. `math.ceil(-2.5)` is `-2`.
Answer: true

22. A syntax error is detected before the program starts running.
Answer: False

23. `'a' + 1` raises `TypeError`.
Answer: True

24. `int("3.5")` returns `3`.
Answer: True

25. `bool("False")` is `True`.
Answer: False

26. Python identifiers are case-sensitive.
Answer: True

27. Binary `1011` equals decimal `11`.
Answer: True

28. Hex `1F` equals decimal `31`.
Answer: t

29. Standard ASCII represents 128 characters using 7 bits.
Answer: t 

30. UTF-8 always uses exactly 4 bytes per character.
Answer: f

31. De Morgan: NOT(A AND B) equals (NOT A) OR (NOT B).
Answer: t

32. XOR outputs 1 when its two inputs are different.
Answer: t

33. A compiler translates the whole program before execution; an interpreter translates and runs statement by statement.
Answer: t

34. Cache memory is faster and smaller than main memory.
Answer: t

35. Copyright protects ideas themselves, not just how they are expressed.
Answer: Yes i think so

36. The GPL requires derivative works to be shared under the same licence terms (copyleft).
Answer: Whats GPL

---

---

## Diagnostic Evaluation & Review

### Summary Score: 25 / 36

| Category | Questions | Score | Assessment |
|---|---|---|---|
| **Python Core Syntax & Mutability** | 1–7, 13–17, 21, 23, 26 | 14 / 14 | Excellent retention. Identity vs equality, immutability, aliasing, slicing, and operators are solid. |
| **Data Types & Type Conversion** | 24, 25 | 0 / 2 | Gaps in explicit type conversion rules (`int("3.5")`) and truthiness of non-empty strings (`bool("False")`). |
| **Execution & Error Handling** | 22 | 0 / 1 | Misunderstood parse-time / compile-time error detection vs run-time errors. |
| **String Methods** | 10, 11, 12 | 0 / 3 | Gaps in exact method specifications (`partition`, `find` vs `index`, `split()` default whitespace rules). |
| **Dictionary Methods** | 8, 9, 18 | 1 / 3 | Knows `get()` won't raise KeyError; missed `setdefault()` and was unsure about `del d[k]`. |
| **Standard Library Modules** | 19, 20 | 0 / 2 | Missed `random.randint` vs `random.randrange` endpoint rules; forgot `statistics.mode`. |
| **Unit 1 Prerequisite Check** | 27–34 | 8 / 8 | 100% verified retention of Class 11 Unit 1 (Number systems, Boolean logic, OS/Hardware). |
| **Unit 3 Society, Law & Ethics** | 35, 36 | 0 / 2 | Missed copyright scope (ideas vs expression) and open-source licenses (GPL/copyleft). |

---

### Detailed Item-by-Item Evaluation

*   **1. `type(3+4j)` is `complex`.**
    *   **Student Answer:** `True`
    *   **Verdict:** **CORRECT**
    *   **Model Note:** Python natively supports complex numbers; `j` or `J` represents $\sqrt{-1}$. The type is `complex`.

*   **2. `5 / 2` evaluates to `2`.**
    *   **Student Answer:** `False, it evalutes to nothing as '5/2' is a sing. (If it is an integer expression then 2.5)`
    *   **Verdict:** **CORRECT**
    *   **Model Note:** In Python 3, `/` performs true float division, giving `2.5`. Floor division `//` gives integer `2`.

*   **3. `-5 // 2` evaluates to `-3`.**
    *   **Student Answer:** `True`
    *   **Verdict:** **CORRECT**
    *   **Model Note:** Python's `//` operator rounds down towards negative infinity (floor). $-5 / 2 = -2.5 \implies \lfloor -2.5 \rfloor = -3$.

*   **4. `==` compares identity and `is` compares values.**
    *   **Student Answer:** `False, its the opposite`
    *   **Verdict:** **CORRECT**
    *   **Model Note:** `==` checks value equality (`__eq__`), while `is` checks object identity (memory address / `id()`).

*   **5. Strings in Python are mutable.**
    *   **Student Answer:** `False`
    *   **Verdict:** **CORRECT**
    *   **Model Note:** Strings are immutable. In-place modification like `s[0] = 'a'` raises `TypeError`.

*   **6. `my_list.sort()` returns a new sorted list and leaves `my_list` unchanged.**
    *   **Student Answer:** `False`
    *   **Verdict:** **CORRECT**
    *   **Model Note:** `list.sort()` sorts the list in place and returns `None`.

*   **7. `sorted((3,1,2))` returns a tuple.**
    *   **Student Answer:** `false, it returns a list`
    *   **Verdict:** **CORRECT**
    *   **Model Note:** The built-in `sorted()` function always returns a new `list`, regardless of the iterable input type.

*   **8. `d.get("k")` raises `KeyError` if `"k"` is missing.**
    *   **Student Answer:** `False`
    *   **Verdict:** **CORRECT**
    *   **Model Note:** `d["k"]` raises `KeyError`, but `d.get("k")` safely returns `None` (or a specified default value).

*   **9. `d.setdefault("k", 5)` inserts `"k": 5` if `"k"` is missing and returns the value for `"k"`.**
    *   **Student Answer:** `IDK`
    *   **Verdict:** **INCORRECT** *(Statement is TRUE)*
    *   **Model Correction:** `d.setdefault(key, default)` checks if `key` exists. If present, it returns the existing value. If missing, it sets `d[key] = default` and returns `default`.

*   **10. `"abc".partition("b")` returns `('a', 'b', 'c')`.**
    *   **Student Answer:** `IDK partition`
    *   **Verdict:** **INCORRECT** *(Statement is TRUE)*
    *   **Model Correction:** `str.partition(sep)` splits at the first occurrence of `sep` and returns a 3-tuple `(head, sep, tail)`. For `"abc".partition("b")`, it returns `('a', 'b', 'c')`. If `sep` is not found, it returns `(str, '', '')`.

*   **11. `"hello".find("z")` returns `-1`, while `"hello".index("z")` raises `ValueError`.**
    *   **Student Answer:** ` ` *(blank)*
    *   **Verdict:** **INCORRECT** *(Statement is TRUE)*
    *   **Model Correction:** Both search for a substring. When not found, `.find()` returns `-1` (safe search), whereas `.index()` raises `ValueError`.

*   **12. `"a b  c".split()` returns `['a', 'b', 'c']`.**
    *   **Student Answer:** `False`
    *   **Verdict:** **INCORRECT** *(Statement is TRUE)*
    *   **Model Correction:** When `str.split()` is called with no arguments (or `sep=None`), any run of consecutive whitespace characters is treated as a single delimiter, and leading/trailing whitespace is discarded. Hence `"a b  c".split()` produces `['a', 'b', 'c']`.

*   **13. `list(range(2, 10, 3))` is `[2, 5, 8]`.**
    *   **Student Answer:** `true`
    *   **Verdict:** **CORRECT**
    *   **Model Note:** Starts at 2, increments by 3 ($2, 5, 8$), stops before 10.

*   **14. `break` skips only the current iteration and continues the loop.**
    *   **Student Answer:** `False`
    *   **Verdict:** **CORRECT**
    *   **Model Note:** `break` terminates the entire loop immediately. `continue` skips the remainder of the current iteration and advances to the next.

*   **15. After `a = b = []`, `a` and `b` are two independent lists.**
    *   **Student Answer:** `f`
    *   **Verdict:** **CORRECT**
    *   **Model Note:** Chained assignment binds both names to the same mutable list object in memory (`id(a) == id(b)`).

*   **16. `(5)` is a tuple with one element.**
    *   **Student Answer:** `f`
    *   **Verdict:** **CORRECT**
    *   **Model Note:** Parentheses around a single expression without a comma are just grouping parentheses; `type((5))` is `int`. A single-element tuple requires a trailing comma: `(5,)`.

*   **17. `x.extend([1,2])` and `x.append([1,2])` produce the same list.**
    *   **Student Answer:** `f`
    *   **Verdict:** **CORRECT**
    *   **Model Note:** `extend` unpacks the iterable and adds elements individually. `append` adds the argument as a single object (resulting in a nested list).

*   **18. `del d["k"]` removes the key `"k"` from dictionary `d`.**
    *   **Student Answer:** `IDK, there is a del keyword in python for dict??`
    *   **Verdict:** **INCORRECT** *(Statement is TRUE)*
    *   **Model Correction:** `del` is a Python keyword for deleting references. `del d["k"]` deletes the key `"k"` and its associated value from dictionary `d`. (Raises `KeyError` if `"k"` does not exist).

*   **19. `random.randint(1, 6)` can return `6`, and `random.randrange(1, 6)` can also return `6`.**
    *   **Student Answer:** `T`
    *   **Verdict:** **INCORRECT** *(Statement is FALSE)*
    *   **Model Correction:** `random.randint(a, b)` generates integers in the closed range $[a, b]$ (both inclusive, so 6 is possible). `random.randrange(start, stop)` generates integers in the half-open range $[\text{start}, \text{stop})$ (stop is excluded), so `randrange(1, 6)` can only return 1, 2, 3, 4, 5 — never 6.

*   **20. `statistics.mode([1,2,2,3])` returns `2`.**
    *   **Student Answer:** `IDK, I diont even remember mode.i only remember mean and median`
    *   **Verdict:** **INCORRECT** *(Statement is TRUE)*
    *   **Model Correction:** `statistics.mode()` returns the most frequent data point in a dataset. Since 2 appears most frequently, it returns `2`.

*   **21. `math.ceil(-2.5)` is `-2`.**
    *   **Student Answer:** `true`
    *   **Verdict:** **CORRECT**
    *   **Model Note:** The ceiling function returns the smallest integer greater than or equal to $x$. Since $-2 > -2.5$, `math.ceil(-2.5) == -2`.

*   **22. A syntax error is detected before the program starts running.**
    *   **Student Answer:** `False`
    *   **Verdict:** **INCORRECT** *(Statement is TRUE)*
    *   **Model Correction:** Python parses source code into an Abstract Syntax Tree (AST) and compiles it into bytecode before execution begins. Syntax errors are caught during parsing, before a single line of code is executed. Run-time errors (like `ZeroDivisionError` or `TypeError`) occur during execution.

*   **23. `'a' + 1` raises `TypeError`.**
    *   **Student Answer:** `True`
    *   **Verdict:** **CORRECT**
    *   **Model Note:** Python does not do implicit type coercion between `str` and `int`; concatenating them raises `TypeError: can only concatenate str (not "int") to str`.

*   **24. `int("3.5")` returns `3`.**
    *   **Student Answer:** `True`
    *   **Verdict:** **INCORRECT** *(Statement is FALSE)*
    *   **Model Correction:** `int(string)` expects a string representing an integer in base 10. Passing a floating-point string literal like `"3.5"` raises `ValueError: invalid literal for int() with base 10: '3.5'`. To truncate to 3, one must convert to float first: `int(float("3.5"))`.

*   **25. `bool("False")` is `True`.**
    *   **Student Answer:** `False`
    *   **Verdict:** **INCORRECT** *(Statement is TRUE)*
    *   **Model Correction:** `bool(x)` evaluates truthiness. Any non-empty string in Python evaluates to `True`, regardless of its content (`bool("False")` is `True`, `bool("0")` is `True`). Only the empty string `""` evaluates to `False`.

*   **26. Python identifiers are case-sensitive.**
    *   **Student Answer:** `True`
    *   **Verdict:** **CORRECT**
    *   **Model Note:** `name`, `Name`, and `NAME` are three distinct identifiers in Python.

*   **27. Binary `1011` equals decimal `11`.**
    *   **Student Answer:** `True`
    *   **Verdict:** **CORRECT**
    *   **Model Note:** $1\times 8 + 0\times 4 + 1\times 2 + 1\times 1 = 11$.

*   **28. Hex `1F` equals decimal `31`.**
    *   **Student Answer:** `t`
    *   **Verdict:** **CORRECT**
    *   **Model Note:** $1\times 16 + 15\times 1 = 31$.

*   **29. Standard ASCII represents 128 characters using 7 bits.**
    *   **Student Answer:** `t`
    *   **Verdict:** **CORRECT**
    *   **Model Note:** Standard ASCII uses 7 bits ($2^7 = 128$ distinct characters, codes 0 to 127).

*   **30. UTF-8 always uses exactly 4 bytes per character.**
    *   **Student Answer:** `f`
    *   **Verdict:** **CORRECT**
    *   **Model Note:** UTF-8 is a variable-length encoding using 1 to 4 bytes per code point. UTF-32 is fixed at 4 bytes.

*   **31. De Morgan: NOT(A AND B) equals (NOT A) OR (NOT B).**
    *   **Student Answer:** `t`
    *   **Verdict:** **CORRECT**
    *   **Model Note:** First De Morgan law: $\overline{A \cdot B} = \overline{A} + \overline{B}$.

*   **32. XOR outputs 1 when its two inputs are different.**
    *   **Student Answer:** `t`
    *   **Verdict:** **CORRECT**
    *   **Model Note:** $A \oplus B = 1$ if and only if $A \neq B$.

*   **33. A compiler translates the whole program before execution; an interpreter translates and runs statement by statement.**
    *   **Student Answer:** `t`
    *   **Verdict:** **CORRECT**
    *   **Model Note:** Fundamental distinction between compilers (batch translation to object code) and interpreters (line-by-line translation and immediate execution).

*   **34. Cache memory is faster and smaller than main memory.**
    *   **Student Answer:** `t`
    *   **Verdict:** **CORRECT**
    *   **Model Note:** Cache (SRAM) is placed close to the CPU core for speed, but is significantly smaller and more expensive per byte than main memory (DRAM).

*   **35. Copyright protects ideas themselves, not just how they are expressed.**
    *   **Student Answer:** `Yes i think so`
    *   **Verdict:** **INCORRECT** *(Statement is FALSE)*
    *   **Model Correction:** Copyright protects only the original *expression* of an idea (source code, text, diagrams), not the underlying idea, concept, algorithm, or mathematical principle.

*   **36. The GPL requires derivative works to be shared under the same licence terms (copyleft).**
    *   **Student Answer:** `Whats GPL`
    *   **Verdict:** **INCORRECT** *(Statement is TRUE)*
    *   **Model Correction:** The GNU General Public License (GPL) is the canonical "copyleft" software license. Anyone distributing modified or derivative versions of GPL software must release the modified source code under the same GPL terms.

