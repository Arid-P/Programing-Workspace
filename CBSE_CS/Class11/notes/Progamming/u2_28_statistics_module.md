# Unit 2: Computational Thinking and Programming-I (Topic 28)

---

## 28. The `statistics` Module: Measures of Central Tendency and Edge Cases

- **Mental model:**
  Think of evaluating a classroom of students who took a test:
  - **`mean` (The Fair Equalizer):** Gather all test marks into a giant bucket, melt them down, and pour out an exactly equal puddle to every student. If Bill Gates walks into the room, the puddle gets artificially huge (heavily skewed by extreme outliers).
  - **`median` (The Middle Human):** Line all students up in a straight physical line from shortest score to highest score. Walk directly to the student standing at the exact halfway mark. It does not care if the highest student scored 100 or 1,000,000 (immune to extreme outliers).
  - **`mode` (The Popularity Contest):** The score that was handed out to the greatest number of desks. Because it's just counting identical ballots, it works equally well on numbers ($95, 95$) or non-numeric words (*"Passed", "Passed", "Failed"*).

---

### The Three Prescribed Central Tendency Functions (Exhaustive Reference)

To use: `import statistics` or `from statistics import mean, median, mode`.

```
                    ┌────────────────────────────┐
                    │    statistics Module       │
                    └─────────────┬──────────────┘
              ┌───────────────────┼───────────────────┐
              ▼                   ▼                   ▼
      [ mean(data) ]      [ median(data) ]     [ mode(data) ]
      Arithmetic Average   Middle Value        Most Frequent Value
      (Numeric only)      (Numeric only)      (Numeric or Categorical)
```

---

#### 1. `statistics.mean(data) -> float`
* **Mathematical Definition:**
  $$\bar{x} = \frac{\sum_{i=1}^n x_i}{n} = \frac{x_1 + x_2 + \dots + x_n}{n}$$
* **Supported Data Types:**
  - Sequence or iterable of numbers: `int`, `float`, `Fraction`, `Decimal`.
  - Non-numeric types (e.g. strings) raise **`TypeError: unsupported operand type(s) for +`**.
* **Failure Modes & Edge Cases:**
  - **Empty Sequence:** If `data` is empty, raises **`statistics.StatisticsError: mean requires at least one data point`**!
  - `statistics.mean([10, 20, 30]) \implies 20` (or `20.0`).
  - `statistics.mean([1.5, 2.5, 5.0]) \implies 3.0`.

---

#### 2. `statistics.median(data) -> float | int`
* **Mathematical Definition:** The median is the middle value separating the higher half from the lower half of a data sample.
* **Automatic Sorting Rule:**
  - You do **NOT** need to pre-sort the list; Python automatically sorts the data internally before selecting the median.
* **Odd vs. Even Number of Elements:**
  1. **Odd Count ($n$ is odd):**
     - Returns the exact single middle element:
       $$\text{Index} = \frac{n - 1}{2}$$
     - Example: `statistics.median([7, 1, 4])` $\implies$ Sorted internally to `[1, 4, 7]` $\implies$ returns **`4`** (preserves integer type).
  2. **Even Count ($n$ is even):**
     - Calculates the **arithmetic mean of the two middle elements**:
       $$\text{Median} = \frac{x_{n/2 - 1} + x_{n/2}}{2}$$
     - **Always returns a `float`**!
     - Example: `statistics.median([10, 20, 30, 40])` $\implies \frac{20 + 30}{2} = \mathbf{25.0}$.
* **Failure Modes & Edge Cases:**
  - **Empty Sequence:** Raises **`statistics.StatisticsError: no median for empty data`**!

---

#### 3. `statistics.mode(data) -> Any` (Diagnostic Statement #20)
* **Mathematical Definition:** The mode is the single most common data point that occurs with the greatest frequency.
* **Categorical / String Data Capability (Crucial CBSE Distinction):**
  - Unlike `mean` and `median` which perform arithmetic, `mode()` performs frequency counting.
  - Therefore, `mode()` **can process strings, words, and discrete non-numeric items**:
    ```python
    grades = ["A", "B", "B", "A", "B", "C"]
    print(statistics.mode(grades))  # "B"
    ```
* **The Multimodal Tie Rule (Python 3.8+ Standard):**
  - What happens if two or more values share the highest frequency (a tie / multimodal dataset)?
  - In modern Python (3.8+), `statistics.mode()` **returns the first mode encountered in the input data**:
    ```python
    statistics.mode([4, 4, 9, 9, 1])  # Returns 4 (4 appeared before 9)
    statistics.mode([9, 9, 4, 4, 1])  # Returns 9 (9 appeared before 4)
    statistics.mode([1, 2, 3, 4])     # Returns 1 (all frequency 1; returns first)
    ```
* **Failure Modes & Edge Cases:**
  - **Empty Sequence:** Raises **`statistics.StatisticsError: no mode for empty data`**!

---

### Auxiliary Functions (CBSE & Python 3.8+ Reference)

1. **`statistics.multimode(data) -> list`:**
   - Returns a **list of all modes** with the highest frequency.
   - $`statistics.multimode([4, 4, 9, 9, 1]) \implies [4, 9]`.$
   - $`statistics.multimode([1, 2, 3]) \implies [1, 2, 3]`$.
2. **`statistics.median_low(data) -> int | float`:**
   - For an even number of data points, returns the **smaller** of the two middle elements without averaging them:
     $`statistics.median_low([1, 2, 3, 4]) \implies 2`$.
3. **`statistics.median_high(data) -> int | float`:**
   - For an even number of data points, returns the **larger** of the two middle elements without averaging them:
     $`statistics.median_high([1, 2, 3, 4]) \implies 3`$.

---

## Direct Comparison of Measures of Central Tendency

| Feature | `mean(data)` | `median(data)` | `mode(data)` |
|---|---|---|---|
| **Measures** | Center of gravity / average | Spatial midpoint | Peak frequency / popularity |
| **Data Types** | **Numeric only** | **Numeric only** | **Numeric AND Categorical (Strings)** |
| **Requires Sorting?**| No | Automatically sorts internally | No |
| **Sensitivity to Outliers**| **High** (skewed by extreme values) | **None** (robust against outliers) | **None** |
| **Even $n$ Output**| Standard float | Float average of 2 centers | Most frequent value |
| **Empty Data Error**| `StatisticsError` | `StatisticsError` | `StatisticsError` |

---

## Worked Examples Covering Board Scenarios

```python
import statistics

# 1. Handling Outliers: Mean vs Median
salaries = [30000, 32000, 35000, 31000, 1000000] # CEO salary is outlier
print("Mean:", statistics.mean(salaries))       # 225600.0 (misleadingly high!)
print("Median:", statistics.median(salaries))   # 32000 (accurately reflects typical salary)

# 2. String Mode in Survey Data
colors = ["red", "blue", "green", "blue", "blue", "red"]
print("Most popular color:", statistics.mode(colors)) # "blue"

# 3. Multimodal Ties
scores = [10, 10, 20, 20, 5]
print("Primary mode:", statistics.mode(scores))       # 10 (first encountered)
print("All modes:", statistics.multimode(scores))     # [10, 20]
```

---

## Common Exam Mistakes
1. Assuming `median([5, 1, 9])` returns 1 because 1 is at index 1 in the unsorted list (Python automatically sorts it to `[1, 5, 9]` and returns 5).
2. Expecting `statistics.mean([])` to return `0` or `0.0` (it raises `StatisticsError`).
3. Believing `mode()` only accepts numbers (it fully supports strings and categorical tokens).
4. Forgetting that `median()` on an even number of elements **always returns a float**.
5. Conflating `mode()` with `multimode()`: `mode()` returns a single scalar; `multimode()` returns a list.
