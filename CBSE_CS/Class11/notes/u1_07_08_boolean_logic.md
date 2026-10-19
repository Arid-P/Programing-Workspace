# Unit 1: Computer Systems and Organisation (Topics 07–08)

## 07. Boolean Logic and Logic Gates

- **Mental model:**
  Think of electrical circuits with switches in series and parallel:
  - An input is either ON ($1$ / True) or OFF ($0$ / False).
  - **AND** is switches in series (both must be closed for the bulb to light).
  - **OR** is switches in parallel (closing either switch lights the bulb).
  - **NOT** is an inverter relay (closing the switch shorts or cuts power to the bulb).
  - **NAND & NOR** are "Universal building blocks"—just like Lego bricks, you can build any gate (AND, OR, NOT) using only NANDs or only NORs.
  - **XOR** is a "difference detector" or a stair-light circuit (turns ON when switch inputs are different).

- **Key facts / definitions:**
  - **Boolean Variable:** A variable that takes only one of two values: $0$ (False) or $1$ (True).
  - **Basic Gates:**
    - **NOT (Inverter):** Unary operator. $Y = \overline{A}$. Inverts the input ($0 \rightarrow 1$, $1 \rightarrow 0$).
    - **AND (Conjunction):** $Y = A \cdot B$ (or $AB$). Output is $1$ if and only if **all** inputs are $1$.
    - **OR (Disjunction):** $Y = A + B$. Output is $1$ if **at least one** input is $1$.
  - **Universal Gates (CBSE must-know):**
    - A gate is *universal* if any Boolean function can be implemented using only that gate type.
    - **NAND (NOT-AND):** $Y = \overline{A \cdot B}$. Output is $0$ only when all inputs are $1$.
    - **NOR (NOT-OR):** $Y = \overline{A + B}$. Output is $1$ only when all inputs are $0$.
  - **Exclusive Gates:**
    - **XOR (Exclusive-OR):** $Y = A \oplus B = \overline{A}B + A\overline{B}$. Output is $1$ if inputs are **different** (odd parity detector).
    - **XNOR (Exclusive-NOR / Equivalence):** $Y = \overline{A \oplus B} = AB + \overline{A}\overline{B}$. Output is $1$ if inputs are **identical**.

- **Worked example:**
  - Truth table for XOR ($Y = A \oplus B$):
    - $A=0, B=0 \implies Y = 0$
    - $A=0, B=1 \implies Y = 1$
    - $A=1, B=0 \implies Y = 1$
    - $A=1, B=1 \implies Y = 0$

- **Common exam mistakes:**
  - Writing that XOR gives $1$ when both inputs are $1$ (conflating OR with XOR).
  - Forgetting why NAND and NOR are called "Universal" (they can independently synthesize NOT, AND, and OR circuits).
  - Misinterpreting the bubble at gate outputs (a bubble represents logical negation/NOT).

---

## 08. De Morgan's Laws and Boolean Expression Simplification

- **Mental model:**
  Think of breaking a long bar over a mathematical expression:
  "Break the line, change the sign."
  When you negate a grouped condition, AND flips to OR, and OR flips to AND, while distributing the negation to individual terms.
  - Example: "I will NOT (eat apples AND bananas)" $\equiv$ "I will NOT eat apples OR I will NOT eat bananas."

- **Key facts / definitions:**
  - **De Morgan's First Law:**
    - The complement of a product (AND) equals the sum of the individual complements.
    - Formula: $\overline{A \cdot B} = \overline{A} + \overline{B}$ (or $(AB)' = A' + B'$)
    - Gate equivalence: A **NAND** gate is functionally equivalent to a **Bubbled OR** gate (an OR gate with inverted inputs).
  - **De Morgan's Second Law:**
    - The complement of a sum (OR) equals the product of the individual complements.
    - Formula: $\overline{A + B} = \overline{A} \cdot \overline{B}$ (or $(A+B)' = A' \cdot B'$)
    - Gate equivalence: A **NOR** gate is functionally equivalent to a **Bubbled AND** gate (an AND gate with inverted inputs).
  - **Essential Boolean Postulates for Simplification:**
    - Annulment / Dominance: $A + 1 = 1$, $A \cdot 0 = 0$.
    - Identity: $A + 0 = A$, $A \cdot 1 = A$.
    - Idempotence: $A + A = A$, $A \cdot A = A$.
    - Complementarity: $A + \overline{A} = 1$, $A \cdot \overline{A} = 0$.
    - Involution: $\overline{\overline{A}} = A$.
    - Distributive: $A(B + C) = AB + AC$, and $A + BC = (A + B)(A + C)$.
    - Absorption: $A + AB = A$, $A(A + B) = A$, $A + \overline{A}B = A + B$.

- **Worked example:**
  - Simplify: $F = AB + A\overline{B}$
    1. Factor out common term $A$: $F = A(B + \overline{B})$
    2. Apply Complementarity ($B + \overline{B} = 1$): $F = A \cdot 1$
    3. Apply Identity ($A \cdot 1 = A$): $F = A$

- **Common exam mistakes:**
  - Forgetting the second distributive law: $A + BC = (A + B)(A + C)$ (students try to multiply out rather than factor).
  - Forgetting to invert the operator when applying De Morgan's laws (e.g., incorrectly writing $\overline{A \cdot B} = \overline{A} \cdot \overline{B}$).
  - Misapplying Absorption: writing $A + AB = B$ instead of $A$.

