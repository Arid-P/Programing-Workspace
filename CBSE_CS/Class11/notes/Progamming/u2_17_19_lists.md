# Unit 2: Computational Thinking and Programming-I (Topics 17–19)

---

## 17. Lists: Memory Model, Operations, and Traversal

- **Mental model:**
  - **Memory Structure:** Think of a Python list not as a single wooden storage chest, but as a **ring binder with transparent plastic sleeves**.
    - Each sleeve has a sleeve number (the index: $0, 1, 2, \dots$ or $-1, -2, \dots$).
    - What is inside the sleeve is **not the actual object itself**, but an index card containing the **memory address (pointer)** of an object floating out in the warehouse (heap).
    - Because the binder is mutable, you can open the binder rings, swap out cards, insert new sleeves in the middle (`insert`), rip out sleeves (`pop`/`remove`), or replace a whole section of sleeves at once (`slice assignment`).
  - **Aliasing vs Copies:**
    - **Aliasing (`b = a`):** Two students holding the *exact same binder*. When Student B rips out page 1, Student A sees page 1 missing.
    - **Shallow Copy (`b = a.copy()` or `b = a[:]`):** You photocopy the binder pages. You now have two distinct binders. If you rip out page 1 of binder B, binder A is unaffected. **However**, if page 1 was pointing to a shared inner folder (nested list), both binders still point to that exact same inner folder!
    - **Deep Copy (`copy.deepcopy(a)`):** You photocopy the binder *and* go duplicate every single sub-folder and item referenced inside.

---

### Core Syntax & Indexing Rules

1. **Definition:** A mutable, ordered, heterogeneous sequence of arbitrary objects enclosed in square brackets `[e1, e2, ...]`.
2. **Direct Indexing vs. Out of Bounds:**
   - Indices: $0$ to $\text{len}(lst) - 1$ (forward) and $-\text{len}(lst)$ to $-1$ (backward).
   - Direct indexing out of bounds raises **`IndexError: list index out of range`**:
     ```python
     lst = [10, 20, 30]
     print(lst[3])   # IndexError: list index out of range
     ```
3. **Slicing Clamping Rule:**
   - Slicing **NEVER raises an `IndexError`**; it safely clamps to list boundaries:
     ```python
     lst = [10, 20, 30]
     print(lst[1:100])  # [20, 30] (clamped to len=3)
     print(lst[10:20])  # [] (empty list returned)
     ```

---

### Slicing Mutations & In-Place Slice Modification

Because lists are mutable, you can assign iterable values directly into slice targets:

1. **Replacing a Slice with Different Length:**
   ```python
   nums = [1, 2, 3, 4, 5]
   nums[1:4] = [20, 30]      # 3 elements (2, 3, 4) replaced by 2 elements (20, 30)
   print(nums)               # [1, 20, 30, 5]
   ```
2. **Inserting via Zero-Width Slice:**
   ```python
   nums = [10, 40]
   nums[1:1] = [20, 30]      # Inserts at index 1 without replacing anything
   print(nums)               # [10, 20, 30, 40]
   ```
3. **Deleting via Empty Slice Assignment:**
   ```python
   nums = [10, 20, 30, 40]
   nums[1:3] = []            # Deletes elements at indices 1 and 2
   print(nums)               # [10, 40]
   ```
4. **Clearing Entire List in Place:**
   ```python
   nums = [1, 2, 3]
   nums[:] = []              # Clears contents; keeps the same id(nums) object
   ```

---

### List Aliasing, Copies, and the 2D Multiplication Trap

#### The 2D Matrix Multiplication Trap (Guaranteed CBSE Exam Question)
```python
# THE FATAL BUG:
row = [0] * 3
matrix = [row] * 3        # Creates 3 references to the EXACT SAME list object in memory!
matrix[0][0] = 99         # Mutating row 0 mutates ALL THREE ROWS!
print(matrix)             # [[99, 0, 0], [99, 0, 0], [99, 0, 0]]

# THE CORRECT CBSE IDIOM:
matrix = [[0] * 3 for _ in range(3)]  # Generates 3 independent inner list instances
matrix[0][0] = 99
print(matrix)             # [[99, 0, 0], [0, 0, 0], [0, 0, 0]]
```

---

## 18. The 14 List Methods & Functions (Exhaustive Reference)

> **Universal Rule:** In-place list methods (`append`, `extend`, `insert`, `remove`, `reverse`, `sort`) mutate the list object in memory and **always return `None`**!

---

### 1. `len(lst) -> int`
* Returns number of elements. `len([]) == 0`.

### 2. `list([iterable]) -> list`
* Constructor. Converts any iterable into a new list.
* `list("cat") \implies ['c', 'a', 't']`. `list((1, 2)) \implies [1, 2]`. `list() \implies []`.

### 3. `lst.append(x) -> None`
* **Parameters:** `x`: Any single object (number, string, list, tuple, etc.).
* **Function:** Adds `x` as a single element to the end of `lst`. Mutates in place; returns `None`.
* **Edge Case:** If `x` is another list, it appends as a single nested list item:
  ```python
  lst = [1, 2]
  lst.append([3, 4])
  print(lst)        # [1, 2, [3, 4]] -> len(lst) is 3, NOT 4!
  ```

### 4. `lst.extend(iterable) -> None`
* **Parameters:** `iterable`: Must be an iterable collection (`list`, `tuple`, `str`, `dict`, `set`).
* **Function:** Unpacks `iterable` and appends each element individually to the end of `lst`. Mutates in place; returns `None`.
* **Edge Cases & Failure Modes:**
  - Passing a non-iterable (`lst.extend(50)`) raises **`TypeError: 'int' object is not iterable`**!
  - Passing a string: `[1].extend("hi") \implies [1, 'h', 'i']`.
  - Passing a dictionary: **appends dictionary keys**, not values!
    `[1].extend({"a": 10, "b": 20}) \implies [1, 'a', 'b']`.

### 5. `lst.insert(index, x) -> None`
* **Parameters:** `index` (integer target position), `x` (object to insert).
* **Function:** Inserts item `x` at position `index`, shifting existing elements to the right. Mutates in place; returns `None`.
* **The Clamping Rule:** `insert()` **NEVER raises an `IndexError`**!
  - If `index >= len(lst)`: appends to the end of the list.
  - If `index <= -len(lst)`: inserts at index 0 (the beginning).
  ```python
  lst = [10, 20]
  lst.insert(100, 30)   # [10, 20, 30] (clamped to end)
  lst.insert(-100, 5)   # [5, 10, 20, 30] (clamped to start)
  ```

### 6. `lst.count(x) -> int`
* **Parameters:** `x`: Value to count.
* **Function:** Returns the number of elements where `element == x` evaluates to True.
* **Edge Cases:**
  - Returns `0` if absent (never errors).
  - Boolean / Integer equality trap: `[1, True, 0, False].count(1) \implies \mathbf{2}` (because `1 == True`)!

### 7. `lst.index(x, [start], [stop]) -> int`
* **Parameters:** `x` (search value), optional `start` and `stop` window slice boundaries.
* **Function:** Returns zero-based index of the first occurrence of `x`.
* **CRITICAL DIFFERENCE FROM STRINGS:** Lists do **NOT** have a `.find()` method!
* **Failure Mode:** **RAISES `ValueError: x is not in list`** if absent!
  ```python
  [10, 20, 30].index(20)  # 1
  [10, 20, 30].index(99)  # ValueError: 99 is not in list
  ```

### 8. `lst.remove(x) -> None`
* **Parameters:** `x`: Target value to remove.
* **Function:** Searches for value `x` and removes its **first occurrence**. Mutates in place; returns `None`.
* **Failure Mode:** **RAISES `ValueError: list.remove(x): x not in list`** if `x` is absent!
  *(Note: It does NOT raise `IndexError`! `remove()` operates by value, not by index).*
  ```python
  lst = [10, 20, 10, 30]
  lst.remove(10)          # Removes first 10 -> [20, 10, 30]
  lst.remove(99)          # ValueError: list.remove(x): x not in list
  ```

### 9. `lst.pop([index]) -> Any`
* **Parameters:** `index` (optional integer). **Default: `-1`** (the last element).
* **Function:** Removes and **returns** the element at position `index`.
* **Failure Mode:** Raises **`IndexError: pop from empty list`** or `pop index out of range`.
* **`remove()` vs `pop()` Direct Comparison Table:**

| Feature | `lst.remove(x)` | `lst.pop([index])` |
|---|---|---|
| **Argument Taken** | Takes a **target value** `x` to search for. | Takes an **index position** (defaults to `-1`). |
| **Return Value** | Always returns **`None`**. | Returns the **popped element**. |
| **Failure Exception** | Raises **`ValueError`** if value is not in list. | Raises **`IndexError`** if index is out of bounds or list is empty. |
| **Popping First Element**| N/A | `lst.pop(0)` removes and returns the first element. |

### 10. `lst.reverse() -> None`
* Reverses elements of `lst` **in place**. Returns `None`.
* *Contrast:* `lst[::-1]` creates a new list; `reversed(lst)` returns an iterator.

### 11. `lst.sort(key=None, reverse=False) -> None`
* Sorts `lst` **in place**. Returns `None`. Modifies the existing list object (`id()` unchanged).
* `key`: Function of one argument used to extract a comparison key from each element (`key=len`, `key=abs`, `key=str.lower`).
* `reverse=True`: Sorts in descending order.
* **Heterogeneous Type Trap:** If list contains elements that cannot be compared via `<` (e.g. `[10, "apple"]`), raises **`TypeError: '<' not supported between instances of 'str' and 'int'`**.

### 12. `sorted(iterable, key=None, reverse=False) -> list`
* Built-in function. Accepts **any iterable** and **always returns a brand-new sorted list**. Leaves original iterable unchanged.

### 13. `min(lst)` & `max(lst)`
* Returns smallest/largest element using `<` comparisons.
* **Failure Mode:** Raises **`ValueError: min() arg is an empty sequence`** on an empty list!

### 14. `sum(iterable, start=0) -> number`
* Sums elements plus `start`.
* **Failure Mode:** Elements must be numeric. If list contains strings, raises **`TypeError: unsupported operand type(s) for +: 'int' and 'str'`** (Python explicitly tells you: *"use ''.join(seq) to join strings"*).
* `sum([10, 20], 5)` evaluates to $10 + 20 + 5 = \mathbf{35}$.

---

## 19. Essential List Algorithms (CBSE Prescribed)

### 1. Linear Search Algorithm
```python
def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i  # Return index of first occurrence
    return -1         # Target not found
```

### 2. Finding Minimum, Maximum, and Mean Without Built-ins
```python
def compute_stats(nums):
    if not nums:
        return None
    
    minimum = maximum = nums[0]
    total = 0
    
    for n in nums:
        if n < minimum:
            minimum = n
        if n > maximum:
            maximum = n
        total += n
        
    mean = total / len(nums)
    return minimum, maximum, mean
```

### 3. Swapping Adjacent Even and Odd Positioned Elements
```python
def swap_even_odd(lst):
    # Swaps lst[0] with lst[1], lst[2] with lst[3], etc.
    for i in range(0, len(lst) - 1, 2):
        lst[i], lst[i + 1] = lst[i + 1], lst[i]
```

### 4. Frequency Count of All Unique Elements
```python
def frequency_count(lst):
    freq = {}
    for item in lst:
        freq[item] = freq.get(item, 0) + 1
    return freq
```

---

## Common Exam Mistakes
1. Confusing `append([1, 2])` with `extend([1, 2])`: `append` creates a nested list; `extend` unpacks elements.
2. Passing an integer to `extend()`: `lst.extend(5)` raises `TypeError` because integers are not iterable.
3. Expecting `remove()` to raise `IndexError` when a value is missing (it raises **`ValueError`**).
4. Forgetting that `lst.sort()` returns **`None`**: writing `sorted_lst = my_list.sort()` results in `sorted_lst = None`!
5. Using `[[0] * 3] * 3` to build a 2D matrix (creates aliased rows).

