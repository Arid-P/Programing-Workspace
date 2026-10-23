# Unit 2: Computational Thinking and Programming-I (Topic 27)

---

## 27. The `random` Module: Pseudo-Random Number Generation and Range Analysis

- **Mental model:**
  - **Pseudo-Random Generator as a Shuffled Deck of Cards:**
    - A computer cannot generate true randomness out of thin air. Instead, it uses a deterministic mathematical algorithm (Python uses the **Mersenne Twister**, period $2^{19937}-1$) that produces a sequence of numbers so scrambled that it looks completely random.
    - If you provide the same starting seed (`random.seed(42)`), the deck is shuffled into the exact same order every time (crucial for reproducible scientific simulations and game replays).
  - **`randint` vs `randrange`:**
    - **`randint(a, b)`:** A physical board-game die with faces numbered from $a$ to $b$. When you roll it, you can land on the lowest face ($a$) or the highest face ($b$). **Both ends are included.**
    - **`randrange(start, stop)`:** A digital countdown clock. It starts counting at `start` and ticks up, but shuts down the millisecond it reaches `stop`. **`stop` is never reached.**

---

### The Three Prescribed CBSE Random Functions (Exhaustive Reference)

---

#### 1. `random.random() -> float`
* **Parameters:** None.
* **Return Type:** **`float`**.
* **Mathematical Interval:** **$[0.0, 1.0)$**
* **Endpoint Inclusions:**
  $$0.0 \le r < 1.0$$
  - $0.0$ is **INCLUDED** (can be generated).
  - $1.0$ is **STRICTLY EXCLUDED** (can never be generated).
* **Scaling to Arbitrary Real Interval $[A, B)$:**
  To generate a random float between $A$ and $B$:
  $$\text{val} = A + \text{random.random}() \times (B - A)$$
  - Example: `5 + random.random() * 10` generates a float in $[5.0, 15.0)$.

---

#### 2. `random.randint(a, b) -> int`
* **Parameters:** Two integers $a$ and $b$ such that $a \le b$.
* **Return Type:** **`int`**.
* **Mathematical Interval:** **$[a, b]$ (Closed Interval)**
* **Endpoint Inclusions:**
  $$a \le N \le b$$
  - Both endpoints $a$ and $b$ are **INCLUDED**!
  - Example: `random.randint(1, 6)` can return $1, 2, 3, 4, 5, \mathbf{6}$.
* **Edge Cases & Failure Modes:**
  - **Single Element Range:** `random.randint(5, 5)` returns integer `5` (completely legal).
  - **Inverted Range:** If $a > b$ (e.g. `random.randint(10, 5)`), **RAISES `ValueError: empty range for randint()`**! (It does not swap them).

---

#### 3. `random.randrange([start], stop, [step]) -> int`
* **Parameters:**
  - `start` (optional): Initial integer (default: `0`).
  - `stop` (**mandatory**): Upper limit (**STRICTLY EXCLUDED**).
  - `step` (optional): Integer increment step (default: `+1`).
* **Return Type:** **`int`**.
* **Mathematical Interval:** **$[start, stop)$ (Half-Open Interval)**
* **Variations:**
  1. *1 Argument (`random.randrange(N)`):*
     - Generates an integer from $0$ up to $N - 1$.
     - `random.randrange(6)` $\implies 0, 1, 2, 3, 4, 5$ ($6$ is never returned!).
  2. *2 Arguments (`random.randrange(start, stop)`):*
     - Generates integers from $start$ up to $stop - 1$.
     - `random.randrange(1, 6)` $\implies 1, 2, 3, 4, 5$ ($6$ is never returned!).
  3. *3 Arguments (`random.randrange(start, stop, step)`):*
     - Generates integers following the progression $start, start+step, start+2\cdot step, \dots < stop$.
     - Example: `random.randrange(10, 30, 4)` generates strictly from $\{10, 14, 18, 22, 26\}$ (30 is excluded).
* **Failure Modes:**
  - `step == 0`: Raises **`ValueError: zero arg for randrange()`**.
  - Non-integer arguments: Raises **`ValueError: non-integer arg 1 for randrange()`**.

---

### Direct Comparison: `randint` vs `randrange`

| Feature | `random.randint(a, b)` | `random.randrange(a, b)` |
|---|---|---|
| **Interval Type** | **Closed $[a, b]$** | **Half-Open $[a, b)$** |
| **Is Upper Bound Included?** | **YES ($b$ is included)** | **NO ($b$ is strictly excluded)** |
| **Supports Step Argument?** | No (steps are always 1) | Yes (`step` can be specified) |
| **Equivalent Expression** | `random.randrange(a, b + 1)` | `random.randint(a, b - 1)` (when step=1) |
| **Output for `(1, 6)`** | $1, 2, 3, 4, 5, \mathbf{6}$ | $1, 2, 3, 4, 5$ |

---

## Solving CBSE Board Exam Output Range Questions (The 3-Step Method)

> **Standard Board Exam Problem:**
> Given the following code, find the minimum and maximum possible values of `VAL`, and determine which of the given options can NEVER be printed.
> ```python
> import random
> CITY = ["DELHI", "MUMBAI", "CHENNAI", "KOLKATA", "BENGALURU"]
> FLY = random.randint(1, 3)
> for k in range(FLY, 4):
>     print(CITY[k], end=":")
> ```

### The 3-Step Solution Protocol:
1. **Find Extremes of the Random Variable:**
   - `FLY = random.randint(1, 3)`
   - Minimum value of `FLY` = **1**
   - Maximum value of `FLY` = **3**
2. **Trace the Loop for Minimum Case (`FLY = 1`):**
   - `range(1, 4)` iterates over $k = 1, 2, 3$:
   - Prints: `CITY[1]:CITY[2]:CITY[3]:` $\implies$ **`MUMBAI:CHENNAI:KOLKATA:`**
3. **Trace the Loop for Maximum Case (`FLY = 3`):**
   - `range(3, 4)` iterates over $k = 3$:
   - Prints: `CITY[3]:` $\implies$ **`KOLKATA:`**
4. **Intermediate Case (`FLY = 2`):**
   - `range(2, 4)` iterates over $k = 2, 3$:
   - Prints: `CITY[2]:CITY[3]:` $\implies$ **`CHENNAI:KOLKATA:`**

*Conclusion:*
- Only three possible outputs can ever be produced:
  1. `MUMBAI:CHENNAI:KOLKATA:`
  2. `CHENNAI:KOLKATA:`
  3. `KOLKATA:`
- Any option that starts with `DELHI` or includes `BENGALURU` is mathematically impossible!

---

## Common Exam Mistakes
1. Assuming `random.randrange(1, 6)` can return 6 (the upper bound in `randrange` is **always excluded**).
2. Assuming `random.random()` can return 1.0 (the interval is $[0.0, 1.0)$).
3. Writing `random.randint(10, 1)` and expecting it to count backwards (raises `ValueError: empty range for randint()`).
4. Conflating list slicing clamping with `randint()` boundaries.
5. In subtraction problems ($A - B$): forgetting that minimum of $A - B$ occurs at $\text{Min}(A) - \text{Max}(B)$.

