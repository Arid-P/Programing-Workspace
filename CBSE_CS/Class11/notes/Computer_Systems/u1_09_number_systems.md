# Unit 1: Computer Systems and Organisation (Topic 09)

## 09. Number Systems and Conversions

- **Mental model:**
  Think of number systems as different counting currencies:
  - Decimal (Base 10) is counting on 10 fingers ($0\text{--}9$).
  - Binary (Base 2) is a single switch with 2 states ($0\text{--}1$).
  - Octal (Base 8) and Hexadecimal (Base 16) are compact human shorthands for binary:
    - 3 binary switches group cleanly into 1 octal digit ($2^3 = 8$).
    - 4 binary switches (a nibble) group cleanly into 1 hex digit ($2^4 = 16$).

- **Key facts / definitions:**
  - **Base / Radix:** The number of unique digits available in that number system.
    - Binary: Base 2 ($0, 1$).
    - Octal: Base 8 ($0, 1, 2, 3, 4, 5, 6, 7$).
    - Decimal: Base 10 ($0, 1, 2, 3, 4, 5, 6, 7, 8, 9$).
    - Hexadecimal: Base 16 ($0\text{--}9$ and $\text{A}=10, \text{B}=11, \text{C}=12, \text{D}=13, \text{E}=14, \text{F}=15$).
  - **Conversion Rules:**
    1. *Decimal to Any Base:*
       - **Integer Part:** Successive division by target base (remainders read bottom-to-top / LSB to MSB).
       - **Fractional Part:** Successive multiplication by target base (integer carry read top-to-bottom).
       - *Why the carry can never exceed the base:* Since $0 \le \text{fraction} < 1$, multiplying by Base $B$ strictly guarantees $0 \le B \times \text{fraction} < B$. In binary ($\times 2$), the carry can ONLY be $0$ or $1$. In octal ($\times 8$), carries are $0\text{--}7$. In hex ($\times 16$), carries are $0\text{--}15$ ($0\text{--}\text{F}$).
       - *When to stop multiplying:*
         - Case A: Fractional part reaches $.000\dots$ (terminating, stop immediately).
         - Case B: An earlier fractional remainder repeats (infinite recurring cycle; put an overbar or stop).
         - Case C: If neither occurs, terminate at 4 to 6 fractional digits as per standard CBSE instructions.
    2. *Any Base to Decimal:* Expand positional weights: $\sum (\text{digit} \times \text{base}^{\text{position}})$. Positions are $0, 1, 2\dots$ left of radix point, and $-1, -2\dots$ right of radix point.
    3. *Binary $\leftrightarrow$ Octal:* Group bits in clusters of **3** ($2^3 = 8$). Pad with leading/trailing zeroes if needed.
    4. *Binary $\leftrightarrow$ Hexadecimal:* Group bits in clusters of **4** (nibbles, $2^4 = 16$).
    5. *Octal $\leftrightarrow$ Hexadecimal:* Use **Binary as the intermediate bridge** ($\text{Octal} \xrightarrow{3\text{-bit}} \text{Binary} \xrightarrow{\text{regroup 4-bit}} \text{Hex}$).

- **Worked example:**
  - Convert $(53.625)_{10}$ to Binary:
    - Integer: $53 \div 2 = 26$ R $1$; $26 \div 2 = 13$ R $0$; $13 \div 2 = 6$ R $1$; $6 \div 2 = 3$ R $0$; $3 \div 2 = 1$ R $1$; $1 \div 2 = 0$ R $1$. Bottom-up: $(110101)_2$.
    - Fractional: $0.625 \times 2 = 1.25$ ($1$); $0.25 \times 2 = 0.50$ ($0$); $0.50 \times 2 = 1.0$ ($1$). Top-down: $(0.101)_2$.
    - Result: $(110101.101)_2$.
  - Grouping to Hex:
    - Integer: $\underbrace{0011}_{3} \;\underbrace{0101}_{5} \implies 35_{16}$.
    - Fraction: $\underbrace{1010}_{\text{A}} \implies \text{A}_{16}$.
    - Result: $(35.\text{A})_{16}$.

- **Common exam mistakes:**
  - Forgetting that $\text{A}=10, \text{B}=11, \text{C}=12, \text{D}=13, \text{E}=14, \text{F}=15$ in hexadecimal (e.g. writing $10$ instead of $\text{A}$).
  - Grouping binary bits from the wrong direction: for integers, always group **right-to-left**; for fractional parts, always group **left-to-right**.
  - Writing the remainders top-to-bottom instead of bottom-to-top in decimal-to-base conversions.


---

### Detailed Worked Examples: Fractional Conversions & Recurring Radix Expansion

#### A. Decimal Fraction to Target Base

1. **Terminating Binary Example:** $(0.6875)_{10} \rightarrow \text{Binary}$
   - $0.6875 \times 2 = 1.375 \implies \text{carry } 1, \text{ rem } 0.375$
   - $0.375 \times 2 = 0.75 \implies \text{carry } 0, \text{ rem } 0.75$
   - $0.75 \times 2 = 1.50 \implies \text{carry } 1, \text{ rem } 0.50$
   - $0.50 \times 2 = 1.00 \implies \text{carry } 1, \text{ rem } 0.00$ (Stop)
   - Read top-down: $(0.6875)_{10} = (0.1011)_2$.

2. **Terminating Octal & Hex Examples:** $(0.6875)_{10}$
   - To Octal: $0.6875 \times 8 = 5.50$ (carry $5$, rem $0.5$); $0.5 \times 8 = 4.0$ (carry $4$, rem $0.0$). Stop $\implies (0.54)_8$.
   - To Hexadecimal: $0.6875 \times 16 = 11.0$ (carry $11 = \text{B}$, rem $0.0$). Stop $\implies (0.\text{B})_{16}$.

3. **Infinite Repeating Binary Example:** $(0.2)_{10} \rightarrow \text{Binary}$
   - $0.2 \times 2 = 0.4 \implies 0$, rem $0.4$
   - $0.4 \times 2 = 0.8 \implies 0$, rem $0.8$
   - $0.8 \times 2 = 1.6 \implies 1$, rem $0.6$
   - $0.6 \times 2 = 1.2 \implies 1$, rem $0.2$ (Cycle repeats: $0.2$ re-occurs)
   - Carries: $0011\;0011\dots \implies (0.\overline{0011})_2 \approx (0.001100)_2$.

4. **Hexadecimal Large Carries:** $(0.8125)_{10} \rightarrow \text{Hexadecimal}$
   - $0.8125 \times 16 = 13.00 \implies \text{carry } 13 = \text{D}$, rem $0.0$. Stop $\implies (0.\text{D})_{16}$.

---

#### B. Converting Recurring Radix Fractions Back to Decimal (Base 10)

General Formula for a repeating fraction $(0.\overline{d_1 d_2 \dots d_k})_B$ with period length $k$ in Base $B$:
$$x = \frac{(d_1 d_2 \dots d_k)_B \text{ in decimal}}{B^k - 1}$$

1. **Binary Recurring to Decimal:** $(0.\overline{0011})_2$
   - Let $x = (0.00110011\dots)_2$. Period $k = 4$, Base $B = 2$.
   - Multiply by $2^4 = 16$:
     $$16x = (11.00110011\dots)_2 = (0011)_2 + x = 3 + x$$
   - Subtract $x$: $15x = 3 \implies x = \frac{3}{15} = \frac{1}{5} = \mathbf{0.2_{10}}$.

2. **Octal Recurring to Decimal:** $(0.\overline{25})_8$
   - Let $x = (0.252525\dots)_8$. Period $k = 2$, Base $B = 8$.
   - Multiply by $8^2 = 64$:
     $$64x = (25.2525\dots)_8 = (25)_8 + x$$
   - Convert $(25)_8$ to decimal: $2 \times 8 + 5 = 21_{10}$.
   - Subtract $x$: $63x = 21 \implies x = \frac{21}{63} = \frac{1}{3} = \mathbf{0.3333\dots_{10}}$.

3. **Hexadecimal Recurring to Decimal:** $(0.\overline{\text{C}})_{16}$
   - Let $x = (0.\text{CCCC}\dots)_{16}$. Period $k = 1$, Base $B = 16$.
   - Multiply by $16^1 = 16$:
     $$16x = (\text{C}.\text{CCCC}\dots)_{16} = \text{C}_{16} + x = 12 + x$$
   - Subtract $x$: $15x = 12 \implies x = \frac{12}{15} = \frac{4}{5} = \mathbf{0.8_{10}}$.


---

### Detailed Worked Examples: Fractional Conversions & Recurring Radix Expansion

#### A. Decimal Fraction to Target Base

1. **Terminating Binary Example:** $(0.6875)_{10} \rightarrow \text{Binary}$
   - $0.6875 \times 2 = 1.375 \implies \text{carry } 1, \text{ rem } 0.375$
   - $0.375 \times 2 = 0.75 \implies \text{carry } 0, \text{ rem } 0.75$
   - $0.75 \times 2 = 1.50 \implies \text{carry } 1, \text{ rem } 0.50$
   - $0.50 \times 2 = 1.00 \implies \text{carry } 1, \text{ rem } 0.00$ (Stop)
   - Read top-down: $(0.6875)_{10} = (0.1011)_2$.

2. **Terminating Octal & Hex Examples:** $(0.6875)_{10}$
   - To Octal: $0.6875 \times 8 = 5.50$ (carry $5$, rem $0.5$); $0.5 \times 8 = 4.0$ (carry $4$, rem $0.0$). Stop $\implies (0.54)_8$.
   - To Hexadecimal: $0.6875 \times 16 = 11.0$ (carry $11 = \text{B}$, rem $0.0$). Stop $\implies (0.\text{B})_{16}$.

3. **Infinite Repeating Binary Example:** $(0.2)_{10} \rightarrow \text{Binary}$
   - $0.2 \times 2 = 0.4 \implies 0$, rem $0.4$
   - $0.4 \times 2 = 0.8 \implies 0$, rem $0.8$
   - $0.8 \times 2 = 1.6 \implies 1$, rem $0.6$
   - $0.6 \times 2 = 1.2 \implies 1$, rem $0.2$ (Cycle repeats: $0.2$ re-occurs)
   - Carries: $0011\;0011\dots \implies (0.\overline{0011})_2 \approx (0.001100)_2$.

4. **Hexadecimal Large Carries:** $(0.8125)_{10} \rightarrow \text{Hexadecimal}$
   - $0.8125 \times 16 = 13.00 \implies \text{carry } 13 = \text{D}$, rem $0.0$. Stop $\implies (0.\text{D})_{16}$.

---

#### B. Converting Recurring Radix Fractions Back to Decimal (Base 10)

General Formula for a repeating fraction $(0.\overline{d_1 d_2 \dots d_k})_B$ with period length $k$ in Base $B$:
$$x = \frac{(d_1 d_2 \dots d_k)_B \text{ in decimal}}{B^k - 1}$$

1. **Binary Recurring to Decimal:** $(0.\overline{0011})_2$
   - Let $x = (0.00110011\dots)_2$. Period $k = 4$, Base $B = 2$.
   - Multiply by $2^4 = 16$:
     $$16x = (11.00110011\dots)_2 = (0011)_2 + x = 3 + x$$
   - Subtract $x$: $15x = 3 \implies x = \frac{3}{15} = \frac{1}{5} = \mathbf{0.2_{10}}$.

2. **Octal Recurring to Decimal:** $(0.\overline{25})_8$
   - Let $x = (0.252525\dots)_8$. Period $k = 2$, Base $B = 8$.
   - Multiply by $8^2 = 64$:
     $$64x = (25.2525\dots)_8 = (25)_8 + x$$
   - Convert $(25)_8$ to decimal: $2 \times 8 + 5 = 21_{10}$.
   - Subtract $x$: $63x = 21 \implies x = \frac{21}{63} = \frac{1}{3} = \mathbf{0.3333\dots_{10}}$.

3. **Hexadecimal Recurring to Decimal:** $(0.\overline{\text{C}})_{16}$
   - Let $x = (0.\text{CCCC}\dots)_{16}$. Period $k = 1$, Base $B = 16$.
   - Multiply by $16^1 = 16$:
     $$16x = (\text{C}.\text{CCCC}\dots)_{16} = \text{C}_{16} + x = 12 + x$$
   - Subtract $x$: $15x = 12 \implies x = \frac{12}{15} = \frac{4}{5} = \mathbf{0.8_{10}}$.

