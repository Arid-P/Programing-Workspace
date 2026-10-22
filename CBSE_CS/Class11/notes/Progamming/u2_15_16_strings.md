# Unit 2: Computational Thinking and Programming-I (Topics 15–16)

---

## 15. Strings: Structure, Operations, and Slicing Mechanics

- **Mental model:**
  Think of a Python string as a **frozen, read-only measuring tape**:
  - Each character occupies a numbered slot on the tape.
  - You can look at any slot from the front ($0, 1, 2, \dots$) or from the back ($-1, -2, -3, \dots$).
  - Because it is frozen in ice (immutable), you **cannot** chisel out a character and replace it with another. To change anything, you must create an entirely new tape.
  - Slicing is like taking a pair of scissors to cut out a window between two tick marks: if you ask for scissor cuts beyond the physical tape ends, Python doesn't break; it simply cuts along the physical tape boundaries (clamping).

---

### Core Syntax & Indexing Rules

1. **Immutability:**
   - In-place item modification is forbidden:
     ```python
     s = "Python"
     s[0] = "J"  # TypeError: 'str' object does not support item assignment
     del s[0]    # TypeError: 'str' object doesn't support item deletion
     ```
2. **Two-Way Direct Indexing:**
   - Given string `s` of length $N = \text{len}(s)$:
     - **Forward Indices:** $0, 1, 2, \dots, N-1$
     - **Backward Indices:** $-N, \dots, -2, -1$
   - **Direct Indexing Out of Bounds:** Raises an immediate runtime error:
     ```python
     s = "CAT"  # len = 3
     print(s[3])   # IndexError: string index out of range
     print(s[-4])  # IndexError: string index out of range
     ```

---

### String Operations & Edge Cases

| Operation | Syntax | Description & Full Parameter Rules | Edge Cases & Failure Modes |
|---|---|---|---|
| **Concatenation** | `s1 + s2` | Joins two strings into a new string object. | Both operands **must be `str`**. `'Age: ' + 18` raises `TypeError`. Concatenating with empty string `s + ""` returns `s`. |
| **Repetition** | `s * n` or `n * s` | Repeats string `s` sequentially $n$ times. | $n$ must be an integer. If $n \le 0$, evaluates to empty string `""` (`"abc" * -2 \implies ""`). Float multiplier (`"a" * 2.0`) raises `TypeError`. |
| **Membership** | `sub in s`, `sub not in s` | Checks if substring `sub` is present anywhere in `s`. | **Empty string is ALWAYS a member of any string**: `"" in "hello"` evaluates to **`True`**! `"" in ""` is **`True`**! |
| **Comparison** | `<`, `<=`, `>`, `>=`, `==`, `!=` | Lexicographical order character-by-character using Unicode code points (`ord(ch)`). | Uppercase letters are strictly smaller than lowercase letters (`'Z' < 'a'` because $90 < 97$). Shorter prefix is smaller (`'bat' < 'batch'`). |

---

### Slicing Mechanics & Edge Cases: `s[start:stop:step]`

Syntax: `s[start:stop:step]`

```
  Index:     0   1   2   3   4   5
  String:    P   Y   T   H   O   N
 -Index:    -6  -5  -4  -3  -2  -1
```

#### 1. Default Values Based on Step Direction
The step direction completely determines what `start` and `stop` default to when omitted (`None`):

* **When `step > 0` (Forward Slicing, default `step = +1`):**
  - `start` defaults to `0` (the beginning of the string).
  - `stop` defaults to `len(s)` (the end of the string).
  - Traversal moves **Left $\rightarrow$ Right**.
* **When `step < 0` (Backward / Reverse Slicing):**
  - `start` defaults to `len(s) - 1` (the last character, index `-1`).
  - `stop` defaults to `-(len(s) + 1)` (one position before the first character, capturing index `0`).
  - Traversal moves **Right $\rightarrow$ Left**.

#### 2. The Clamping Rule (No IndexErrors in Slices!)
Unlike direct indexing, **slicing NEVER raises an `IndexError`**. Python clamps indices to the valid string boundaries:
```python
s = "PYTHON"
print(s[2:100])    # "THON" (clamped at len=6)
print(s[-50:3])    # "PYT" (clamped at start=0)
print(s[20:50])    # "" (both beyond end; empty string returned)
```

#### 3. Critical Slicing Edge Cases
1. **Contradictory Direction (Start/Stop Mismatch):**
   - If `step > 0` and `start >= stop`: returns empty string `""`.
     ```python
     "PYTHON"[4:2]      # "" (cannot move forward from index 4 to 2 with step +1)
     ```
   - If `step < 0` and `start <= stop`: returns empty string `""`.
     ```python
     "PYTHON"[2:4:-1]   # "" (cannot move backward from index 2 to 4 with step -1)
     ```
2. **Reversing a String:**
   ```python
   "PYTHON"[::-1]       # "NOHTYP"
   ```
3. **Negative Indices with Positive Step:**
   ```python
   # "PYTHON": -6='P', -5='Y', -4='T', -3='H', -2='O', -1='N'
   "PYTHON"[-4:-1]      # "THO" (starts at -4 'T', stops before -1 'N')
   ```
4. **Negative Indices with Negative Step:**
   ```python
   "PYTHON"[-1:-5:-1]   # "NOHT" (starts at -1 'N', stops before -5 'Y', stepping backwards)
   ```
5. **Zero Step Exception:**
   ```python
   "PYTHON"[::0]        # ValueError: slice step cannot be zero
   ```
6. **Slicing on Empty String:**
   ```python
   ""[1:5]              # ""
   ""[::-1]             # ""
   ```

---

## 16. The 23 CBSE Prescribed String Methods (Exhaustive Reference)

> **Universal Rule:** Strings are immutable. **No string method ever mutates the original string.** Every method that modifies text returns a **brand-new string**.

---

### Cluster 1: Case Modification

#### 1. `s.lower() -> str`
* **Parameters:** None.
* **Function:** Converts all cased characters to lowercase. Non-cased characters (digits, punctuation) remain unchanged.
* **Edge Cases:** Empty string returns `""`. `"123#$".lower()` returns `"123#$"`.

#### 2. `s.upper() -> str`
* **Parameters:** None.
* **Function:** Converts all cased characters to uppercase.
* **Edge Cases:** Empty string returns `""`.

#### 3. `s.capitalize() -> str`
* **Parameters:** None.
* **Function:** Converts the **very first character** of the string to uppercase, and converts **all remaining characters to lowercase**.
* **Edge Cases:**
  ```python
  "hello world".capitalize()   # "Hello world" (only first letter capitalized!)
  "hELLO wORLD".capitalize()   # "Hello world" (all other letters forced to lower!)
  "123 hello".capitalize()     # "123 hello" (first char is digit; rest forced lower)
  "".capitalize()              # ""
  ```

#### 4. `s.title() -> str`
* **Parameters:** None.
* **Function:** Converts the first letter of **every word** to uppercase, and all remaining letters in each word to lowercase.
* **Edge Cases:**
  ```python
  "hello world".title()        # "Hello World"
  "they're here".title()       # "They'Re Here" (apostrophe treated as word boundary!)
  "2b or not 2b".title()       # "2B Or Not 2B" (letter following digit capitalized)
  ```

---

### Cluster 2: Character Classification (Boolean Predicates)

> **Universal Edge Case for all `is*` methods:** On an empty string `""`, **every single one of these methods returns `False`**!

#### 5. `s.isalnum() -> bool`
* **Parameters:** None.
* **Function:** Returns `True` if $\text{len}(s) \ge 1$ and all characters are alphanumeric (alphabetic letters or decimal digits).
* **Edge Cases:** Spaces, punctuation, symbols (`@`, `-`, `_`) return `False`. `"abc12" \implies True`, `"abc 12" \implies False`.

#### 6. `s.isalpha() -> bool`
* **Parameters:** None.
* **Function:** Returns `True` if $\text{len}(s) \ge 1$ and all characters are alphabetic letters (`a–z`, `A–Z`).
* **Edge Cases:** `"Hello" \implies True`, `"Hello2" \implies False`, `"Hello World" \implies False` (contains space).

#### 7. `s.isdigit() -> bool`
* **Parameters:** None.
* **Function:** Returns `True` if $\text{len}(s) \ge 1$ and all characters are digits (`0–9`).
* **Edge Cases:** Negative numbers (`"-5"`) return `False` (contains `-`). Decimal numbers (`"3.14"`) return `False` (contains `.`). Superscript digits (`"²"`) return `True`.

#### 8. `s.islower() -> bool`
* **Parameters:** None.
* **Function:** Returns `True` if all cased characters in the string are lowercase, **and there is at least one cased character**.
* **Edge Cases:**
  ```python
  "hello".islower()      # True
  "hello 123!".islower() # True (digits/symbols ignored; all cased letters are lower)
  "123!".islower()       # False (NO cased characters present!)
  "".islower()           # False
  ```

#### 9. `s.isupper() -> bool`
* **Parameters:** None.
* **Function:** Returns `True` if all cased characters are uppercase, **and there is at least one cased character**.
* **Edge Cases:** `"HELLO 123!".isupper() \implies True`, `"123!".isupper() \implies False`, `"".isupper() \implies False`.

#### 10. `s.isspace() -> bool`
* **Parameters:** None.
* **Function:** Returns `True` if $\text{len}(s) \ge 1$ and every character is a whitespace character (`' '`, `'\t'`, `'\n'`, `'\r'`, `'\v'`, `'\f'`).
* **Edge Cases:** `"".isspace() \implies False`, `"   \t\n  ".isspace() \implies True`, `"   a   ".isspace() \implies False`.

---

### Cluster 3: Search, Count, Prefix & Suffix

#### 11. `len(s) -> int`
* Built-in function returning total number of characters (Unicode code points). `len("") == 0`.

#### 12. `s.count(sub, [start], [end]) -> int`
* **Parameters:**
  - `sub`: Substring to search for (must be `str`, else `TypeError`).
  - `start` (optional): Slice start index (default: `0`).
  - `end` (optional): Slice end index (default: `len(s)`).
* **Function:** Returns the number of **non-overlapping** occurrences of `sub` in `s[start:end]`.
* **Edge Cases:**
  ```python
  "aaaa".count("aa")        # 2 (non-overlapping: indices [0:2] and [2:4])
  "banana".count("a", 2, 4) # 1 (searches within "na")
  "hello".count("z")        # 0 (absent substring returns 0, never errors)
  "cat".count("")           # 4 (empty string occurs len(s) + 1 times: before/between/after!)
  ```

#### 13. `s.find(sub, [start], [end]) -> int`
* **Parameters:**
  - `sub`: Substring to search for.
  - `start`, `end` (optional): Search window slice boundaries.
* **Function:** Returns the **lowest index** where `sub` is found in `s[start:end]`.
* **Failure Mode:** Returns **`-1`** if not found. **Never raises an exception.**
* **Edge Cases:**
  ```python
  "hello".find("l")         # 2 (first occurrence)
  "hello".find("z")         # -1 (NOT FOUND -> returns -1)
  "hello".find("l", 3)      # 3 (search starts at index 3)
  "hello".find("", 2)       # 2 (empty string found immediately at start index)
  ```

#### 14. `s.index(sub, [start], [end]) -> int`
* **Parameters:** Identical to `find()`.
* **Function:** Returns the lowest index where `sub` is found.
* **Failure Mode:** **RAISES `ValueError: substring not found`** if absent!
* **Edge Cases:**
  ```python
  "hello".index("l")        # 2
  "hello".index("z")        # ValueError: substring not found
  ```
* **When to use `find()` vs `index()`:**
  - Use `find()` when testing for presence where absence is a normal condition to check via `if s.find("x") != -1:`.
  - Use `index()` when absence indicates an exceptional error or when working polymorphically with lists/tuples (lists and tuples only have `.index()`, they do NOT have `.find()`).

#### 15. `s.startswith(prefix, [start], [end]) -> bool`
* **Parameters:**
  - `prefix`: A string **OR a tuple of strings** `(str1, str2, ...)`!
  - `start`, `end` (optional): Search window.
* **Function:** Returns `True` if `s[start:end]` starts with `prefix`.
* **Edge Cases:**
  ```python
  "report.pdf".startswith("rep")                    # True
  "https://cbse.gov.in".startswith(("http://", "https://")) # True (accepts a tuple of candidate prefixes!)
  "hello".startswith("")                            # True (every string starts with empty string)
  ```

#### 16. `s.endswith(suffix, [start], [end]) -> bool`
* **Parameters:** `suffix` (string or tuple of strings), `start`, `end` (optional).
* **Function:** Returns `True` if `s[start:end]` ends with `suffix`.
* **Edge Cases:**
  ```python
  "photo.jpg".endswith((".png", ".jpg", ".jpeg"))   # True (tuple of candidate suffixes)
  "hello".endswith("")                              # True
  ```

---

### Cluster 4: Whitespace Stripping

#### 17. `s.lstrip([chars]) -> str`
* **Parameters:** `chars` (optional string): Set of characters to remove. Defaults to whitespace.
* **Function:** Strips leading characters matching **any character in `chars`** from the left.
* **CRITICAL TRAP:** `chars` is treated as a **bag of characters**, NOT a single prefix word!
  ```python
  "   hello".lstrip()            # "hello"
  "www.example.com".lstrip("w.") # "example.com" (strips all 'w' and '.' characters)
  "apple".lstrip("ap")           # "le" (strips 'a' and 'p')
  ```

#### 18. `s.rstrip([chars]) -> str`
* **Parameters:** `chars` (optional). Defaults to whitespace.
* **Function:** Strips trailing characters matching any character in `chars` from the right.
  ```python
  "hello   ".rstrip()            # "hello"
  "test.py".rstrip(".py")        # "test"
  "banana".rstrip("an")          # "b" (strips 'a' and 'n' from right until 'b')
  ```

#### 19. `s.strip([chars]) -> str`
* **Parameters:** `chars` (optional). Defaults to whitespace.
* **Function:** Strips matching characters from **both** left and right ends.
* **Edge Cases:** **Never strips internal characters!**
  ```python
  "   a   b   ".strip()          # "a   b" (internal spaces untouched!)
  "###hello###".strip("#")       # "hello"
  "123hello321".strip("123")     # "hello"
  ```

---

### Cluster 5: Splitting, Partitioning, Replacing, and Joining

#### 20. `s.split(sep=None, maxsplit=-1) -> list[str]`
* **Parameters:**
  - `sep`: Delimiter string.
  - `maxsplit`: Maximum number of splits to perform. Default `-1` means no limit ($N$ splits yield $N+1$ items).
* **Behavior Mode 1: Default (`sep=None` or omitted):**
  - Uses the **whitespace algorithm**: runs of consecutive whitespace characters (`' '`, `'\t'`, `'\n'`) are grouped into a single separator.
  - Leading and trailing whitespace are automatically discarded.
  - Empty strings are **never** returned in the resulting list.
    ```python
    "   Delhi   Mumbai    Chennai   ".split()  # ['Delhi', 'Mumbai', 'Chennai']
    "   ".split()                              # [] (empty list!)
    ```
* **Behavior Mode 2: Explicit Delimiter (e.g. `sep=","`):**
  - Consecutive delimiters are **not** grouped; empty strings between them are preserved!
  - Leading/trailing delimiters produce empty strings at list boundaries!
    ```python
    ",a,,b,".split(",")                        # ['', 'a', '', 'b', '']
    "a b c".split(" ")                         # ['a', 'b', 'c']
    "a  b".split(" ")                          # ['a', '', 'b'] (2 spaces = 1 empty string in middle!)
    ```
* **Behavior Mode 3: With `maxsplit`:**
  ```python
  "apple,banana,orange,grape".split(",", 2)    # ['apple', 'banana', 'orange,grape'] (2 splits = 3 parts)
  ```
* **Failure Modes:**
  - Passing empty string `s.split("")` raises **`ValueError: empty separator`**!

#### 21. `s.partition(sep) -> tuple[str, str, str]`
* **Parameters:** `sep`: Delimiter string to partition around (must be non-empty string).
* **Function:** Searches for the **first occurrence** of `sep` and splits into exactly three parts:
  $$\mathbf{(head,\ sep,\ tail)}$$
* **Found Behavior:**
  ```python
  "user@cbse.nic.in".partition("@")            # ('user', '@', 'cbse.nic.in')
  "a-b-c-d".partition("-")                     # ('a', '-', 'b-c-d') (splits at FIRST occurrence only!)
  ```
* **Missing Delimiter Behavior (CRITICAL EXAM QUESTION):**
  - If `sep` is NOT found in `s`, it returns a 3-tuple containing:
    $$\mathbf{(s,\ "",\ "")}$$
  - The original string followed by two empty strings!
    ```python
    "helloworld".partition(":")                # ('helloworld', '', '')
    ```
* **Failure Modes:**
  - If `sep == ""`: raises **`ValueError: empty separator`**.
* **`partition()` vs `split()` Comparison:**
  - `partition()` **always returns a 3-element tuple**; `split()` returns a **list of arbitrary length**.
  - `partition()` retains the delimiter in the middle slot; `split()` discards the delimiter.

#### 22. `sep.join(iterable) -> str`
* **Parameters:**
  - `sep`: The string placed between joined items.
  - `iterable`: An iterable collection of strings (list, tuple, set, etc.).
* **Function:** Concatenates string elements of `iterable`, interspersed with `sep`.
* **Edge Cases & Failure Modes:**
  - **Every element inside `iterable` MUST be a `str`**:
    ```python
    "-".join([1, 2, 3])       # TypeError: sequence item 0: expected str instance, int found
    "-".join(["1", "2", "3"]) # "1-2-3"
    "-".join(["hello"])       # "hello" (single item: no separator appended)
    "-".join([])              # "" (empty iterable returns empty string)
    "".join(["a", "b", "c"])  # "abc" (clean concatenation)
    ```

#### 23. `s.replace(old, new, [count]) -> str`
* **Parameters:**
  - `old`: Substring to be replaced.
  - `new`: Replacement string.
  - `count` (optional integer): Maximum number of occurrences to replace. Defaults to all.
* **Function:** Returns a copy with occurrences of `old` replaced by `new`.
* **Edge Cases:**
  ```python
  "mississippi".replace("ss", "ZZ")       # "miZZiZZippi"
  "mississippi".replace("ss", "ZZ", 1)    # "miZZissippi" (only first occurrence replaced)
  "hello".replace("z", "a")               # "hello" (if old not found, returns original copy without error)
  "cat".replace("", "-")                  # "-c-a-t-" (empty string replaced at every boundary!)
  ```

---

## Worked Examples Covering All Traps

```python
# Trap 1: The Whitespace split() vs delimiter split()
s = "  x   y  "
print(s.split())        # ['x', 'y']
print(s.split(" "))     # ['', '', 'x', '', '', 'y', '', '']

# Trap 2: String Slicing Step Direction
word = "KNOWLEDGE"
print(word[6:2])        # "" (start > stop with positive step +1)
print(word[6:2:-1])     # "EGDL" (starts at index 6 'E', stops before index 2 'O', stepping backward)

# Trap 3: count() Overlapping
print("abababa".count("aba"))  # 2 (indices 0..2 and 4..6; index 2..4 overlaps and is skipped)

# Trap 4: join() Non-string Elements
data = [10, 20, 30]
# print(":".join(data))        # Crashes with TypeError!
print(":".join(map(str, data)))# "10:20:30" (Correct pattern)
```

---

## Common Exam Mistakes
1. Assuming `s.split("")` splits string into individual characters (it crashes with `ValueError: empty separator`; use `list(s)` instead).
2. Forgetting that `s.partition(sep)` returns a **tuple of 3 elements**, and when `sep` is absent, it returns `(s, '', '')`.
3. Expecting `s.find()` to raise an error when a substring is missing (it returns `-1`; only `s.index()` raises `ValueError`).
4. Expecting `s.strip("ab")` to only strip the exact word `"ab"` (it strips any combination of `'a'` and `'b'` characters from either end).
5. Forgetting that `"".islower()`, `"".isupper()`, and `"".isdigit()` all return `False`.
