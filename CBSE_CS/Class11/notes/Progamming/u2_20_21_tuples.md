# Unit 2: Computational Thinking and Programming-I (Topics 20–21)

---

## 20. Tuples: Structure, Immutability, and Operations

- **Mental model:**
  - **Tuple as a Locked Glass Display Case:**
    - Think of a list as a magnetic whiteboard where you can slap on, rearrange, or wipe off sticky notes whenever you want.
    - A tuple is a **sealed, locked museum glass case**. The items inside are placed in numbered slots ($0, 1, 2, \dots$).
    - Once the glass case is sealed, **you cannot add items (`no append/extend`), remove items (`no pop/remove`), or replace an item with another (`no item assignment`)**.
    - *The Nested Mutability Paradox:* If one of the items inside the locked glass case happens to be a live chameleon or a Tamagotchi (a mutable inner list), that chameleon can still change color inside the case (`t[1].append()`). The glass case itself hasn't been opened; the pointer remains intact!

---

### Core Syntax & Indexing Rules

1. **Definition:** An **immutable, ordered, heterogeneous sequence** of elements.
2. **The Mandatory Single-Element Comma Rule:**
   - In Python, parentheses `()` are overloaded: they are used for mathematical expression grouping as well as for tuple creation.
   - Without a comma, Python evaluates parentheses as mathematical grouping:
     ```python
     a = (5)     # type is INT (value 5)
     b = (5,)    # type is TUPLE (length 1)
     c = 5,      # type is TUPLE (parentheses are optional!)
     d = ()      # type is TUPLE (empty tuple)
     ```
3. **Indexing & Slicing:**
   - Positive ($0 \dots N-1$) and negative ($-N \dots -1$) indexing.
   - Direct indexing out of bounds raises **`IndexError: tuple index out of range`**.
   - Slicing **never raises an error**; it clamps safely to boundaries and **always returns a new tuple**:
     ```python
     t = (10, 20, 30, 40)
     print(t[1:3])     # (20, 30) -> type is tuple
     print(t[10:50])   # () -> empty tuple
     ```

---

### Immutability & The Nested Mutability Edge Cases

1. **Direct Mutation Prohibition:**
   ```python
   t = (10, 20, 30)
   t[0] = 99     # TypeError: 'tuple' object does not support item assignment
   del t[0]      # TypeError: 'tuple' object doesn't support item deletion
   del t         # LEGAL! Deletes the entire variable reference 't'
   ```
2. **The Nested Mutability Paradox (Classic Exam Question):**
   ```python
   t = (1, [10, 20], 3)
   
   # Action A: Mutating the inner list in place
   t[1].append(30)
   print(t)      # (1, [10, 20, 30], 3) -> COMPLETELY LEGAL!
   
   # Action B: Reassigning index 1 of the tuple
   t[1] = [10, 20, 30]  # TypeError: 'tuple' object does not support item assignment
   ```
   *Explanation:* The tuple stores fixed **memory addresses (references)**. Modifying the contents of the inner list does not change its memory address `id()`; thus, the tuple remains immutable while its mutable child evolves.
3. **Tuples as Dictionary Keys:**
   - Dictionaries require keys to be **hashable (immutable)**.
   - A tuple containing only immutable elements (e.g. `(1, 2)` or `("A", 10)`) can be a dictionary key.
   - If a tuple contains a mutable object (e.g. `(1, [2, 3])`), attempting to use it as a dictionary key raises **`TypeError: unhashable type: 'list'`**!

---

### Tuple Packing, Unpacking, and Operations

1. **Tuple Packing:**
   - Assigning comma-separated values to a single variable automatically packs them into a tuple:
     ```python
     student = "Aman", 17, 95.5   # Packs into ('Aman', 17, 95.5)
     ```
2. **Tuple Unpacking:**
   - Unpacking elements of a tuple into distinct variables:
     ```python
     name, age, marks = student
     ```
   - **Failure Modes:** The number of target variables must match tuple length exactly:
     ```python
     x, y = (1, 2, 3)     # ValueError: too many values to unpack (expected 2)
     x, y, z = (1, 2)     # ValueError: not enough values to unpack (expected 3, got 2)
     ```
3. **Extended Unpacking with Star (`*`):**
   ```python
   head, *tail = (1, 2, 3, 4)
   # head = 1, tail = [2, 3, 4] (Note: 'tail' is unpacked into a LIST!)
   ```
4. **Operations:**
   - Concatenation (`+`): `(1, 2) + (3, 4) \implies (1, 2, 3, 4)`. Both operands **must be tuples** (`(1, 2) + [3]` raises `TypeError`).
   - Repetition (`*`): `(1, 2) * 2 \implies (1, 2, 1, 2)`. If multiplier $\le 0$, returns `()`.
   - Membership (`in`, `not in`): `2 in (1, 2, 3) \implies True`.

---

## 21. Tuple Methods and Built-in Functions

> **Noticeable Fact:** Lists have 11 built-in methods. **Tuples have ONLY TWO methods: `.count()` and `.index()`!**
> Tuples do **NOT** have `.append()`, `.extend()`, `.insert()`, `.remove()`, `.pop()`, `.sort()`, `.reverse()`, or `.find()`!

---

### The 2 Tuple Methods

#### 1. `t.count(x) -> int`
* **Parameters:** `x`: Target value to count.
* **Function:** Returns number of times `element == x` evaluates to True.
* **Edge Cases:** Returns `0` if absent (never errors). Boolean equality: `(1, True, 0).count(1) \implies \mathbf{2}`.

#### 2. `t.index(x, [start], [stop]) -> int`
* **Parameters:** `x`: Target search value. Optional `start` and `stop` window slice boundaries.
* **Function:** Returns the lowest zero-based index of the first occurrence of `x`.
* **THE `.find()` MYTH (Classic Exam Trap):**
  - Tuples do **NOT** have a `.find()` method!
  - Calling `t.find(10)` raises **`AttributeError: 'tuple' object has no attribute 'find'`**!
* **Failure Mode:** **RAISES `ValueError: tuple.index(x): x not in tuple`** if `x` is absent!

---

### Built-in Functions on Tuples

#### 3. `len(t) -> int`
* Returns number of elements. `len(()) == 0`.

#### 4. `tuple([iterable]) -> tuple`
* Constructor function. Converts any iterable into a tuple:
  `tuple([1, 2, 3]) \implies (1, 2, 3)`. `tuple("cat") \implies ('c', 'a', 't')`. `tuple() \implies ()`.

#### 5. `sorted(iterable, key=None, reverse=False) -> list`
* **CRITICAL EXAM TRAP (Diagnostic Statement #7):**
  `sorted((3, 1, 2))` does **NOT** return a tuple! It **ALWAYS returns a brand-new `list`**:
  ```python
  res = sorted((3, 1, 2))
  print(res)        # [1, 2, 3] (a LIST!)
  print(type(res))  # <class 'list'>
  ```
  *To get a sorted tuple:* Must explicitly wrap in constructor: `tuple(sorted(t))`.

#### 6. `min(t)` & `max(t)`
* Returns the smallest / largest element based on `<` comparisons.
* **Failure Modes:**
  - Empty tuple: `min(())` or `max(())` raises **`ValueError: min() iterable argument is empty`**!
  - Unorderable mixed types: `min((1, "a"))` raises **`TypeError: '<' not supported between instances of 'str' and 'int'`**.

#### 7. `sum(iterable, start=0) -> number`
* Sums elements plus `start`. Elements must be numeric (`int`, `float`, `complex`).
* Non-numerics (e.g. strings) raise **`TypeError`**.

---

## Tuple Algorithms & Practical Logic

### 1. Linear Search on a Tuple
```python
def tuple_linear_search(t: tuple, target) -> int:
    for i in range(len(t)):
        if t[i] == target:
            return i
    return -1
```

### 2. Computing Min, Max, and Mean of a Tuple
```python
def tuple_stats(t: tuple[float, ...]) -> tuple[float, float, float]:
    if not t:
        raise ValueError("Cannot compute stats on an empty tuple")
    
    minimum = maximum = t[0]
    total = 0.0
    
    for val in t:
        if val < minimum:
            minimum = val
        if val > maximum:
            maximum = val
        total += val
        
    return minimum, maximum, total / len(t)
```

### 3. Frequency Count in a Tuple
```python
def tuple_frequency(t: tuple) -> dict:
    freq = {}
    for item in t:
        freq[item] = freq.get(item, 0) + 1
    return freq
```

---

## Common Exam Mistakes
1. Assuming `(5)` is a tuple (needs a comma: `(5,)`).
2. Assuming `t.find()` exists for tuples (tuples only have `.count()` and `.index()`; calling `.find()` raises `AttributeError`).
3. Believing `sorted(tuple)` returns a tuple (it strictly returns a `list`).
4. Believing that a tuple cannot contain mutable items (a tuple can contain a list, and the inner list can be mutated via `t[1].append()`).
5. Forgetting that `min(())` raises `ValueError`, not `TypeError`.

