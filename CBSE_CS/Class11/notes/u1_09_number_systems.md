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
    1. *Decimal to Any Base:* Successive division of integer part by target base (remainders read bottom-to-top / LSB to MSB). Successive multiplication of fractional part by target base (integers read top-to-bottom).
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

