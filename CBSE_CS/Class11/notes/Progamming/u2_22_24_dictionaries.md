# Unit 2: Computational Thinking and Programming-I (Topics 22–24)

---

## 22. Dictionaries: Architecture, Mutability, and Keys Access

- **Mental model:**
  - **Dictionary as a Hotel Key-Card System:**
    - Think of a dictionary as a modern hotel with individual guest rooms.
    - Each room contains arbitrary luggage (the **values**: can be clothes, electronics, nested bags, or even empty).
    - To open a room, you need an exact, engraved, physical metal key-card (the **key**).
    - **The Hashability Rule:** The key-card must be rigid and unchanging (**immutable**). If a key-card were made of soft melting wax (a **mutable object like a list**), its shape would deform while sitting in your pocket, and the lock mechanism would never recognize it again (`TypeError: unhashable type: 'list'`).
    - Every room number is unique; you cannot have two Room 101s. If you assign a new guest to Room 101, the old guest is moved out (overwritten).

---

### Core Syntax & The Hashability Rule

1. **Definition:** A **mutable, unordered (insertion-ordered in Python 3.7+), heterogeneous mapping** of unique immutable keys to arbitrary values enclosed in curly braces `{key: value}`.
2. **The Hashability Rule (The #1 CBSE Question on Dictionaries):**
   - **Keys MUST be immutable (hashable):** `int`, `float`, `str`, `tuple` (containing only immutable items), `bool`.
   - **Keys CANNOT be mutable:** Attempting to use a `list`, `dict`, or `set` as a key raises **`TypeError: unhashable type: 'list'`**!
   - **The Nested Tuple Trap:** A tuple containing a mutable object (like `(1, [2, 3])`) is **unhashable**!
     ```python
     d = {(1, [2, 3]): "data"}  # TypeError: cannot use 'tuple' as a dict key (unhashable type: 'list')
     ```
   - **Values can be ANYTHING:** Values can be mutable, duplicate, `None`, or nested collections.
3. **Key Uniqueness & The Boolean/Integer Overwrite:**
   - Keys must be unique. If duplicate keys appear in a dictionary literal, the **last value overwrites earlier values**:
     ```python
     d = {"a": 10, "b": 20, "a": 99}
     print(d)  # {'a': 99, 'b': 20}
     ```
   - Because `True == 1` and `hash(True) == hash(1)`:
     ```python
     d = {True: "yes", 1: "one"}
     print(d)       # {True: 'one'}
     print(len(d))  # 1 (Key 'True' retained; value overwritten by 'one'!)
     ```

---

### Key Access, Updating, and Deletion

1. **Direct Access (`d[key]`):**
   - Returns the associated value if `key` exists.
   - **Failure Mode:** Raises **`KeyError: key`** if `key` is missing.
2. **Assignment & Updates (`d[key] = value`):**
   - If `key` is present: updates its value.
   - If `key` is absent: inserts the new key-value pair.
3. **The `del` Statement (Diagnostic Statement #18):**
   - `del d[key]`: Deletes the key and its value from `d`.
   - **Failure Mode:** If `key` does not exist, raises **`KeyError`**!
   - `del d`: Deletes the entire dictionary variable reference.
4. **Membership Operator (`in`, `not in`):**
   - **CRITICAL FACT:** `key in d` strictly checks dictionary **keys** (`d.keys()`), NOT values!
     ```python
     grades = {"Aman": 95, "Rohit": 88}
     print("Aman" in grades)  # True (checks keys)
     print(95 in grades)      # False (does NOT check values!)
     print(95 in grades.values()) # True (explicit check on values)
     ```

---

## 23. The 17 Dictionary Functions & Methods (Exhaustive Reference)

---

### 1. `len(d) -> int`
* Returns total number of key-value pairs. `len({}) == 0`.

### 2. `dict([iterable/mapping], **kwargs) -> dict`
* Constructor function.
  - `dict()` $\implies `{}`$.
  - `dict([('a', 1), ('b', 2)]) \implies {'a': 1, 'b': 2}`.
  - `dict(name="Aman", age=17) \implies {'name': 'Aman', 'age': 17}`.

### 3. `d.keys() -> dict_keys`
* Returns a dynamic view object of all keys.
* `for k in d:` defaults to iterating over `d.keys()`.

### 4. `d.values() -> dict_values`
* Returns a dynamic view object of all values.

### 5. `d.items() -> dict_items`
* Returns a dynamic view object of `(key, value)` tuples.
* Standard traversal: `for key, val in d.items(): ...`

### 6. `d.get(key, [default=None]) -> Any`
* **Safe Key Access:**
  - If `key` is in `d`: returns `d[key]`.
  - If `key` is NOT in `d`: returns `default` (defaults to `None`).
  - **NEVER raises `KeyError`!**
  ```python
  d = {"score": 90}
  print(d.get("score"))     # 90
  print(d.get("bonus"))     # None
  print(d.get("bonus", 0))  # 0
  ```

### 7. `d.setdefault(key, [default=None]) -> Any` (Diagnostic Statement #9)
* **Parameters:** `key`, optional `default` value (defaults to `None`).
* **Behavior:**
  - If `key` **is present**: returns its existing value. The dictionary is **unchanged**.
  - If `key` **is absent**: inserts `key: default` into the dictionary and returns `default`!
  ```python
  d = {"user": "admin"}
  v1 = d.setdefault("user", "guest")   # 'user' exists -> returns 'admin' (no change)
  v2 = d.setdefault("role", "manager") # 'role' missing -> inserts 'role': 'manager' and returns 'manager'
  print(v1)  # "admin"
  print(v2)  # "manager"
  print(d)   # {'user': 'admin', 'role': 'manager'}
  ```

### 8. `d.update([other]) -> None`
* Merges key-value pairs from `other` (another dict or iterable of pairs) into `d`.
* Overwrites overlapping keys; adds new keys. Mutates in place; returns `None`.
  ```python
  d = {"a": 1, "b": 2}
  d.update({"b": 20, "c": 30})
  print(d)  # {'a': 1, 'b': 20, 'c': 30}
  ```

### 9. `d.clear() -> None`
* Empties the dictionary in place. Leaves `d = {}` (`id()` remains unchanged).

### 10. `d.fromkeys(iterable, [value=None]) -> dict`
* **Class Method:** Creates a brand-new dictionary with keys from `iterable` and all values initialized to `value`.
  ```python
  new_d = dict.fromkeys(["math", "cs", "physics"], 0)
  print(new_d)  # {'math': 0, 'cs': 0, 'physics': 0}
  ```
* **The Mutable Default Trap:** If `value` is a mutable object like `[]`, **all keys point to the exact same list instance**!
  ```python
  d = dict.fromkeys(["a", "b"], [])
  d["a"].append(1)
  print(d)  # {'a': [1], 'b': [1]} -> BOTH KEYS MUTATED!
  ```

### 11. `d.copy() -> dict`
* Returns a **shallow copy** of dictionary `d`.

### 12. `d.pop(key, [default]) -> Any`
* Removes `key` and returns its associated value.
* **Failure Modes:**
  - If `key` is absent and `default` is provided: returns `default`.
  - If `key` is absent and `default` is NOT provided: raises **`KeyError: key`**!
  ```python
  d = {"a": 10}
  print(d.pop("a"))        # 10
  print(d.pop("b", "N/A")) # "N/A"
  print(d.pop("b"))        # KeyError: 'b'
  ```

### 13. `d.popitem() -> tuple[key, value]`
* Removes and returns the **last inserted `(key, value)` pair** (LIFO order).
* **Failure Mode:** Raises **`KeyError: 'popitem(): dictionary is empty'`** on an empty dictionary!

### 14. `del d[key]`
* Keyword statement. Deletes `key` and its value. Raises **`KeyError`** if `key` is missing.

### 15. `min(d)` & `max(d)`
* Operates strictly on **keys**, not values!
  `max({'b': 1, 'a': 100}) \implies \mathbf{'b'}`.

### 16. `sorted(d, key=None, reverse=False) -> list`
* Returns a sorted **list of dictionary keys**:
  `sorted({"c": 100, "a": 500, "b": 200}) \implies \mathbf{['a',\ 'b',\ 'c']}`.

---

## 24. Essential Dictionary Programs (CBSE Prescribed)

### 1. Character Frequency Counting in a String
```python
def char_frequency(text: str) -> dict[str, int]:
    freq = {}
    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1
    return freq
```

### 2. Student Records (Roll Number $\rightarrow$ Name & Marks)
```python
def student_records():
    # Record structure: {roll: {"name": str, "marks": float}}
    students = {
        101: {"name": "Aman", "marks": 88.5},
        102: {"name": "Rohit", "marks": 72.0},
        103: {"name": "Priya", "marks": 94.0}
    }
    
    print("Students scoring above 75%:")
    for roll, data in students.items():
        if data["marks"] > 75.0:
            print(f"Roll: {roll}, Name: {data['name']}, Marks: {data['marks']}%")
```

---

## Common Exam Mistakes
1. Using a list or an unhashable tuple as a dictionary key (raises `TypeError: unhashable type`).
2. Expecting `d.get("missing")` to raise a `KeyError` (it returns `None` or default).
3. Confusing `d.pop(key)` with `d.popitem()`: `pop(key)` removes by key; `popitem()` removes the last inserted pair without taking arguments.
4. Assuming `x in d` checks values (it checks **keys**).
5. Forgetting that `sorted(d)` returns a **list of keys** in ascending order.

