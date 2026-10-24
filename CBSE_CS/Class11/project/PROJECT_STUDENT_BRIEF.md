# CBSE Class 11 Computer Science (083)
## Capstone Project Specification: Number Base Converter & Arithmetic System

> **Student Guide & Project Brief**  
> **Target Audience:** Class 11 Student (Independent Project Work — 8 Marks)  
> **Philosophy:** This document explains the **logic, rules, and mathematical behavior** in plain English. Your task is to design, write, test, and debug the program yourself using what you have learned in programming.

---

### 1. Project Overview & Motivation
Computers communicate and store data in electrical switches that are either ON or OFF, creating the **Binary (Base-2)** system. Humans, however, naturally think in the **Decimal (Base-10)** system because we have ten fingers. Programmers and computer engineers often use the **Hexadecimal (Base-16)** system as a convenient shorthand for long strings of binary numbers (such as memory addresses and color codes).

Your mission is to build a terminal-based **Number Base Conversion System** that can seamlessly convert positive numbers between:
1. **Binary (Base-2)** $\longleftrightarrow$ **Decimal (Base-10)**
2. **Decimal (Base-10)** $\longleftrightarrow$ **Hexadecimal (Base-16)**
3. **Hexadecimal (Base-16)** $\longleftrightarrow$ **Binary (Base-2)**

---

### 2. How the User Experiences the Program (Program Flow)

1. **Welcome & Main Menu:**  
   When the program starts, it presents a clear, numbered list of conversion choices:
   * Choice 1: Binary to Decimal
   * Choice 2: Binary to Hexadecimal
   * Choice 3: Decimal to Binary
   * Choice 4: Decimal to Hexadecimal
   * Choice 5: Hexadecimal to Binary
   * Choice 6: Hexadecimal to Decimal
   * Choice 7: Exit Program
2. **Menu Selection:**  
   The user enters their choice number. If they enter anything outside 1 to 7 or non-numeric text, the program should reject it and politely ask again.
3. **Number Entry:**  
   The user enters the number they wish to convert.
4. **Input Verification:**  
   Before attempting any math, the program verifies that the entered number is actually valid for that base (see Section 4). If invalid, it tells the user what was wrong and asks them to re-enter.
5. **Displaying the Result:**  
   The program prints a clear, human-readable summary, e.g.:  
   `Binary: 1101  -->  Decimal: 13`
6. **Continuation Loop:**  
   After showing the result, the program should ask if the user wants to convert another number or return to the menu, rather than abruptly quitting.

---

### 3. The Core Mathematical Logic (How to Compute the Conversions)

#### A. Converting from Any Base to Decimal (Positional Weighting)
Every number system uses positional notation. Each digit's actual value depends on its face value and its place value:
$$\text{Value} = \sum (\text{digit} \times \text{Base}^{\text{position}})$$

* **Position numbering:** Starts at **0** for the rightmost digit and increases by 1 as you move leftward.
* **Binary to Decimal:**
  * Take each digit from right to left (positions 0, 1, 2, ...).
  * Multiply each bit (0 or 1) by $2^{\text{position}}$.
  * Add all products together to get the final decimal number.
  * *Example:* $1101_2 = (1 \times 2^3) + (1 \times 2^2) + (0 \times 2^1) + (1 \times 2^0) = 8 + 4 + 0 + 1 = 13_{10}$.
* **Hexadecimal to Decimal:**
  * In hexadecimal, single digits can represent values up to 15:
    * `A` = 10, `B` = 11, `C` = 12, `D` = 13, `E` = 14, `F` = 15.
  * For each character from right to left:
    * If it is a digit `0`–`9`, use its numerical value.
    * If it is a letter `A`–`F`, use its mapped value from 10 to 15.
    * Multiply that value by $16^{\text{position}}$.
  * Add all products together to get the decimal total.
  * *Example:* $2F_{16} = (2 \times 16^1) + (15 \times 16^0) = 32 + 15 = 47_{10}$.

---

#### B. Converting from Decimal to Any Base (Successive Division)
To convert a decimal integer into another base, you reverse the process by repeatedly dividing:
1. Divide the decimal number by the target base (e.g. 2 for binary, 16 for hexadecimal).
2. Record the **remainder** of the division.
3. Replace the decimal number with the **integer quotient** (discarding the remainder).
4. Repeat steps 1–3 until the quotient becomes zero.
5. **Crucial Step:** Read all the collected remainders in **reverse order** (from the last remainder calculated to the first).

* **Decimal to Binary:**
  * Repeatedly divide by 2, collect remainders (which will only ever be 0 or 1), and reverse them.
  * *Example:* Convert 13 to binary:
    * $13 \div 2 = 6$ remainder **1**
    * $6 \div 2 = 3$ remainder **0**
    * $3 \div 2 = 1$ remainder **1**
    * $1 \div 2 = 0$ remainder **1**
    * Reading remainders backwards: **1101**.
* **Decimal to Hexadecimal:**
  * Repeatedly divide by 16 and collect remainders (0 through 15).
  * If a remainder is between 10 and 15, convert it to its letter counterpart (`10` $\rightarrow$ `A`, `11` $\rightarrow$ `B`, ..., `15` $\rightarrow$ `F`).
  * Reverse the final collection of symbols.
  * *Example:* Convert 47 to hexadecimal:
    * $47 \div 16 = 2$ remainder **15** (`F`)
    * $2 \div 16 = 0$ remainder **2**
    * Reading backwards: **2F**.

---

#### C. Converting Between Binary and Hexadecimal
You have two smart logical options here:
* **Option 1 (The Bridge Approach):**  
  Convert the source base to Decimal first using positional weighting, then convert that Decimal to the target base using successive division.
  * $\text{Binary} \longrightarrow \text{Decimal} \longrightarrow \text{Hexadecimal}$
  * $\text{Hexadecimal} \longrightarrow \text{Decimal} \longrightarrow \text{Binary}$
* **Option 2 (The 4-Bit Nibble Grouping Approach):**  
  Each hexadecimal digit directly corresponds to exactly 4 binary bits (e.g. `F` = `1111`, `A` = `1010`, `1` = `0001`). You can group binary digits in sets of four from right to left.

---

### 4. Input Validation & Error Handling (What Makes It Grade 'A')

A great program never crashes when a user makes a typing mistake. Your program must enforce these strict validation rules:

1. **Zero Handling:**  
   If the user enters `0`, `00`, or `000`, the result in every base is always simply `0`. Make sure your division loops don't produce an empty result for zero!
2. **Binary Validation:**  
   The input string must only contain characters `'0'` and `'1'`. If the user enters `1021` or `abc`, notify them that binary numbers only allow digits 0 and 1, and prompt them to try again.
3. **Decimal Validation:**  
   The input string must only contain digits `'0'` through `'9'` and must represent a positive integer.
4. **Hexadecimal Validation:**  
   The input string must only contain digits `'0'` through `'9'` and letters `'A'`, `'B'`, `'C'`, `'D'`, `'E'`, `'F'` (case-insensitive: lowercase `'a'` through `'f'` should be accepted and treated as uppercase).

---

### 5. Recommended Building Milestones for the Student

Don't try to build the whole program in one sitting. Follow this step-by-step developer roadmap:

* **Step 1 — The Menu Skeleton:**  
  Write a clean loop that displays the 6 options + exit. Read the user's choice and verify it's valid.
* **Step 2 — Binary $\longleftrightarrow$ Decimal:**  
  Write and test the logic to convert binary to decimal and decimal to binary. Test with known numbers like 0, 1, 5, 10, 15, 255.
* **Step 3 — Decimal $\longleftrightarrow$ Hexadecimal:**  
  Write the mapping logic for letters A–F. Test with numbers like 10, 15, 16, 255 (FF), 4096.
* **Step 4 — Direct Binary $\longleftrightarrow$ Hexadecimal:**  
  Combine your existing logic to allow converting binary directly to hex and vice versa.
* **Step 5 — Input Validation & Polish:**  
  Add the checks that catch letters in binary numbers or invalid characters in hex. Add borders, formatting, and pleasant terminal output.

---

### 6. Sample Test Cases to Verify Your Program

| Conversion Type | Input Value | Expected Output |
|---|---|---|
| Binary to Decimal | `1101` | `13` |
| Binary to Decimal | `10000000` | `128` |
| Decimal to Binary | `45` | `101101` |
| Decimal to Hexadecimal | `255` | `FF` |
| Decimal to Hexadecimal | `1000` | `3E8` |
| Hexadecimal to Decimal | `1A` | `26` |
| Hexadecimal to Decimal | `FF` | `255` |
| Binary to Hexadecimal | `11111111` | `FF` |
| Hexadecimal to Binary | `A5` | `10100101` |
| Zero in any base | `0` | `0` |

