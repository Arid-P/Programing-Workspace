# Unit 2: Computational Thinking and Programming-I (Topic 26)

---

## 26. The `math` Module: Constants, Functions, and Domain Edge Cases

- **Mental model:**
  Think of Python's standard library as a modular workshop:
  - Built-in operations (`+`, `-`, `*`, `abs()`, `**`) are tools built directly into the workbench table.
  - The **`math` module** is a specialized precision cabinet mounted on the wall. To use its scientific instruments, you must unlock and open it (`import math`).
  - Unlike general Python which is forgiving with mixed types, the `math` module is backed directly by the C standard mathematical library (`libm`). It strictly operates on **floating-point numbers** and strictly enforces **real-number domain boundaries** (it refuses to invent complex numbers if you ask for $\sqrt{-1}$, throwing a `ValueError` instead).

---

### Mathematical Constants

1. **`math.pi -> float`:**
   - Numerical value: $\pi \approx 3.141592653589793$.
   - Represents the ratio of a circle's circumference to its diameter.
2. **`math.e -> float`:**
   - Numerical value: $e \approx 2.718281828459045$.
   - The base of natural logarithms (Euler's number).

---

### The 8 Prescribed CBSE Mathematical Functions (Exhaustive Reference)

---

#### 1. `math.ceil(x) -> int`
* **Mathematical Definition:** Ceiling function $\lceil x \rceil$. Smallest integer greater than or equal to $x$.
* **Return Type:** **Always an `int`**.
* **Edge Cases & Negative Number Rounding:**
  - Rounding moves towards positive infinity ($+\infty$):
    ```python
    math.ceil(3.2)    # 4
    math.ceil(3.0)    # 3
    math.ceil(-3.7)   # -3 (because -3 > -3.7!)
    math.ceil(-3.0)   # -3
    ```

#### 2. `math.floor(x) -> int`
* **Mathematical Definition:** Floor function $\lfloor x \rfloor$. Largest integer less than or equal to $x$.
* **Return Type:** **Always an `int`**.
* **Edge Cases & Negative Number Rounding:**
  - Rounding moves towards negative infinity ($-\infty$):
    ```python
    math.floor(3.8)   # 3
    math.floor(3.0)   # 3
    math.floor(-3.2)  # -4 (because -4 < -3.2!)
    math.floor(-3.0)  # -3
    ```

#### 3. `math.sqrt(x) -> float`
* **Mathematical Definition:** Principal square root $\sqrt{x}$.
* **Return Type:** **Always a `float`** (`math.sqrt(4) \implies \mathbf{2.0}$, not `2`).
* **Domain Failure Mode:**
  - If $x < 0$: **RAISES `ValueError: math domain error`**!
  - It does **not** return a complex number (for complex roots, you must import the `cmath` module).

#### 4. `math.pow(x, y) -> float`
* **Mathematical Definition:** $x^y$ ($x$ raised to power $y$).
* **Return Type:** **Always a `float`**!
  ```python
  math.pow(2, 3)    # 8.0 (float)
  2 ** 3            # 8   (int)
  ```
* **Edge Cases & Failure Modes:**
  - `math.pow(0, 0) \implies 1.0`.
  - Negative base with fractional exponent (`math.pow(-4, 0.5)`) raises **`ValueError: math domain error`**!

#### 5. `math.fabs(x) -> float`
* **Mathematical Definition:** Absolute value $|x|$.
* **Return Type:** **Always a `float`**!
* **Contrast with Built-in `abs()`:**

| Feature | `math.fabs(x)` | Built-in `abs(x)` |
|---|---|---|
| **Import Required?** | Yes (`import math`) | No (Built-in) |
| **Return on Integer** | `math.fabs(-5) \implies \mathbf{5.0}$ (`float`) | `abs(-5) \implies \mathbf{5}$ (`int`) |
| **Return on Float** | `math.fabs(-5.5) \implies 5.5` | `abs(-5.5) \implies 5.5` |
| **Complex Numbers** | Raises `TypeError` | Returns magnitude $\sqrt{a^2 + b^2}$ |

#### 6. `math.sin(x) -> float`
* **Parameters:** $x$: Angle in **RADIANS** (must not be in degrees!).
* **Conversion Formula:** $\text{radians} = \text{degrees} \times \frac{\pi}{180}$ or `math.radians(degrees)`.
* **Common Exam Pitfall:**
  ```python
  # INCORRECT:
  math.sin(30)                    # -0.98803... (Treats 30 as 30 radians!)
  
  # CORRECT:
  math.sin(math.radians(30))      # 0.49999999999999994 (~ 0.5)
  math.sin(30 * math.pi / 180)    # 0.49999999999999994
  ```

#### 7. `math.cos(x) -> float`
* **Parameters:** $x$: Angle in **radians**.
* Returns $\cos(x)$. `math.cos(0) \implies 1.0`, `math.cos(math.pi) \implies -1.0`.

#### 8. `math.tan(x) -> float`
* **Parameters:** $x$: Angle in **radians**.
* Returns $\tan(x)$.
* **Precision Note:** For $\pi/2$ ($90^\circ$), where $\tan$ is mathematically undefined ($\infty$), floating-point IEEE 754 precision returns a massive finite number ($\approx 1.63 \times 10^{16}$), rather than an error.

---

### Auxiliary Angle Converters (Prescribed in NCERT)
* **`math.radians(deg) -> float`:** Converts angle from degrees to radians.
* **`math.degrees(rad) -> float`:** Converts angle from radians to degrees (`math.degrees(math.pi) \implies 180.0`).

---

## Worked Examples Covering Real Problems

```python
import math

# 1. Quadratic Formula Roots: (-b ± sqrt(b^2 - 4ac)) / (2a)
a, b, c = 1, -5, 6
discriminant = b**2 - 4*a*c
if discriminant >= 0:
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print("Roots:", root1, root2)  # 3.0, 2.0

# 2. Euclidean Distance Between Two Points: sqrt((x2 - x1)^2 + (y2 - y1)^2)
x1, y1 = 0, 0
x2, y2 = 3, 4
distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
print("Distance:", distance)       # 5.0

# 3. Negative Ceiling & Floor
print(math.ceil(-15.3))            # -15
print(math.floor(-15.3))           # -16
```

---

## Common Exam Mistakes
1. Forgetting that `math.sqrt()`, `math.pow()`, and `math.fabs()` **always return floats**.
2. Expecting `math.ceil()` or `math.floor()` to return floats (they strictly return **`int`**).
3. Feeding raw degrees into `sin()`, `cos()`, `tan()` without converting to radians via `math.radians()`.
4. Believing `math.sqrt(-9)` returns `3j` (it crashes with `ValueError: math domain error`).
5. Confusing negative ceiling and floor values: $\text{ceil}(-2.3) = -2$, $\text{floor}(-2.3) = -3$.

