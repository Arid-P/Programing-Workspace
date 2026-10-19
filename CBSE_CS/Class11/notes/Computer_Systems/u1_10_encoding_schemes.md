# Unit 1: Computer Systems and Organisation (Topic 10)

## 10. Character Encoding Schemes: ASCII, ISCII, and Unicode (UTF-8, UTF-32)

---

### Mental Model & Core Intuition

Imagine human communication as hundreds of different spoken dialects, while computer hardware is a strict telegraph operator who only understands electrical pulses: ON ($1$) and OFF ($0$).
- **The Problem:** The CPU cannot inherently store the letter `'A'`, the digit `'7'`, the Hindi character `'क'`, or an emoji `'🔥'`. It can only store binary numbers.
- **The Solution (Character Encoding):** An encoding scheme is an official, standardized "dictionary / codebook" that pairs every human character with a unique numerical ID (called a **Code Point**) and a specific binary sequence.
- **The Evolution:**
  - **ASCII (1960s):** A pocket-sized American codebook with only 128 entries—just enough for English letters, typewriter symbols, and control keys.
  - **ISCII (1991):** An Indian adaptation that kept ASCII in the front half of the book, and used the back half for Indian languages, ingeniously assigning the *same page number* to phonetically equivalent sounds across Hindi, Bengali, Tamil, etc.
  - **Unicode (Modern):** The monumental Library of Alexandria of computing. It assigns a permanent, unique universal code point (`U+XXXX`) to every symbol ever used by humanity.
  - **UTF-8 vs UTF-32:** Unicode gives every character an ID, but how do we pack that ID into memory bytes?
    - **UTF-8** is an *elastic suitcase*: common English letters take only 1 byte; complex European letters take 2; Indian/Asian scripts take 3; emojis take 4.
    - **UTF-32** is a *luxury 4-seat limousine* booked for every single passenger: even if it's just the letter `'A'`, it consumes a full 4 bytes (32 bits).

---

### Comprehensive Theoretical Breakdown (CBSE Exam Standard)

#### 1. ASCII (American Standard Code for Information Interchange)

*   **Origin & Purpose:** Developed by ANSI in the 1960s for teletypewriters and early computers.
*   **Standard 7-bit ASCII:**
    *   Uses **7 bits** to represent each character.
    *   Total capacity: $2^7 = \mathbf{128\text{ unique characters}}$ (numbered $0$ to $127$).
    *   *Non-Printable Control Characters ($0\text{--}31$ and $127$):* Commands originally used for teletype hardware control:
        *   `NUL` (Null) = $0$
        *   `BS` (Backspace) = $8$
        *   `HT` (Horizontal Tab) = $9$
        *   `LF` (Line Feed / Newline `\n`) = $10$
        *   `CR` (Carriage Return `\r`) = $13$
        *   `ESC` (Escape) = $27$
        *   `DEL` (Delete) = $127$
    *   *Printable Characters ($32\text{--}126$):* Punctuation, decimal digits, uppercase English letters, lowercase English letters.
*   **The 4 Essential ASCII Anchor Values (Must-Memorize for CBSE):**
    1.  **Space (`' '`):** $(32)_{10} = (00100000)_2 = (20)_{16}$
    2.  **Digits `'0'` to `'9'`:** $(48)_{10}$ to $(57)_{10}$ *(Notice: character `'0'` is code $48$, NOT $0$!)*
    3.  **Uppercase `'A'` to `'Z'`:** $(65)_{10}$ to $(90)_{10}$ *(`'A'` = $65$, `'B'` = $66\dots$)*
    4.  **Lowercase `'a'` to `'z'`:** $(97)_{10}$ to $(122)_{10}$ *(`'a'` = $97$, `'b'` = $98\dots$)*

*   **The Algebraic & Binary "Offset of 32" (Case Toggling):**
    *   Notice that $97 - 65 = \mathbf{32}$.
    *   For any English letter: $\text{Lowercase Code} = \text{Uppercase Code} + 32$.
    *   In binary, $32 = 2^5$. When written as an 8-bit byte:
        *   `'A'` = $65_{10} = \mathbf{01000001}_2$
        *   `'a'` = $97_{10} = \mathbf{01100001}_2$
        *   *Observation:* Only bit position 5 (the 6th bit from the right) changes! $0$ means Uppercase, $1$ means Lowercase. Flipping this one bit instantly converts case.

*   **Extended 8-bit ASCII:**
    *   Uses a full **8-bit byte** $\implies 2^8 = \mathbf{256\text{ unique characters}}$ ($0\text{--}255$).
    *   Codes $0\text{--}127$ remain identical to 7-bit ASCII.
    *   Codes $128\text{--}255$ contain accented Latin vowels (e.g., `é`, `ü`), mathematical symbols ($\pm, \sqrt{}$), and graphical box-drawing borders.
    *   *Major Limitation:* Cannot represent non-Latin alphabets (Hindi, Arabic, Chinese, Russian Cyrillic).

---

#### 2. ISCII (Indian Script Code for Information Interchange)

*   **Origin:** Standardized by the **Bureau of Indian Standards (BIS)** in 1991 to unify digital data processing across India.
*   **Architecture:**
    *   An **8-bit encoding** ($1\text{ Byte}$ per character $\implies 256$ code points).
    *   **Lower 128 characters ($0\text{--}127$):** Strictly identical to standard 7-bit ASCII (guaranteeing that English text, numbers, and punctuation work without any alteration).
    *   **Upper 128 characters ($128\text{--}255$):** Reserved for Indian alphabets derived from the ancient **Brahmi script**:
        *   Devanagari (Hindi, Marathi, Sanskrit)
        *   Bengali & Assamese
        *   Gurmukhi (Punjabi)
        *   Gujarati
        *   Oriya
        *   Tamil, Telugu, Kannada, Malayalam
*   **The Core Innovation: Phonetic Alignment across Indian Languages:**
    *   All Brahmic scripts share a shared phonetic structure:
        *   Vowels: *अ (a), आ (aa), इ (i), ई (ee)...*
        *   Consonants arranged by vocal articulation: Velar (*क, ख, ग, घ, ङ*), Palatal (*च, छ, ज, झ, ञ*), Retroflex (*ट, ठ, ड...*), etc.
    *   ISCII assigns the **exact same numerical code to phonetically identical characters across all Indian scripts**.
    *   *Practical Consequence:* **Instant Font-Level Transliteration.**
        *   If the byte `0xB3` represents the sound *"ka"*, a Devanagari font renders it as **'क'**.
        *   If the user simply switches the display font to a Bengali font, that exact same byte `0xB3` renders as Bengali **'ক'**.
        *   Switch to a Tamil font, and it renders as Tamil **'க'**.
        *   No computational translation or text conversion is needed; the underlying data bytes are identical.

---

#### 3. Unicode (Universal Coded Character Set)

*   **Why Unicode Was Created:**
    *   Before Unicode, every country invented incompatible regional standards (ASCII for US, ISCII for India, Shift-JIS for Japan, Big5 for Taiwan, KOI8-R for Russia).
    *   A document created in India using ISCII opened as nonsensical garbled characters (*Mojibake*) on a computer in Japan or America.
*   **What Unicode Is:**
    *   A universal standard maintained by the Unicode Consortium that assigns a unique, permanent identifier called a **Code Point** to every character across every written human language, ancient scripts (Egyptian hieroglyphs), mathematical notation, and modern Emojis.
    *   **Code Point Notation:** Written as `U+XXXX` where `XXXX` is a 4- to 6-digit hexadecimal number.
        *   Example: `'A'` is `U+0041`
        *   Example: Devanagari `'अ'` is `U+0905`
        *   Example: Fire Emoji `'🔥'` is `U+1F525`
    *   **Total Capacity:**
        *   Divided into **17 Planes**, each containing $2^{16} = 65,536$ code points.
        *   Total Code Space: $17 \times 65,536 = \mathbf{1,114,112\text{ code points}}$ (from `U+0000` to `U+10FFFF`).
*   **Crucial Conceptual Distinction: Character Set vs. Encoding Scheme:**
    *   **Unicode is a Character Set / Code Point Catalog**, NOT a byte layout on disk. It says: *"The letter 'अ' is number 2309 (`U+0905`)."*
    *   **UTF (Unicode Transformation Format) is the Encoding Scheme.** It defines how that number (`2309`) is physically converted into a stream of $1\text{s}$ and $0\text{s}$ in memory or on a storage drive.
    * Simply, Unicode itself is NOT a file storage format. Unicode only assigns the number (Code Point). How those numbers are stored as bytes on disk or transmitted across cables is defined by Unicode Transformation Formats (UTF).

---

#### 4. Unicode Transformation Formats: UTF-8, UTF-16, and UTF-32 (Bit-Level Architectures)

Unicode assigns every character a numeric ID (**Code Point**). The **UTF** standards define the exact bit-level binary rules to serialize those code points into physical bytes.

---

##### A. UTF-8 (Variable-Length: 1 to 4 Bytes)
UTF-8 is an ingenious, self-synchronizing variable-length encoding designed by Ken Thompson and Rob Pike.
*   **How does a decoder know how many bytes a character uses?**
    *   The **leading bits** of the first byte tell the computer the total length of the sequence.
    *   All **continuation bytes** start with the strict prefix `10`.

| Code Point Range | Total Bytes | Byte 1 (Lead Byte) | Byte 2 (Continuation) | Byte 3 (Continuation) | Byte 4 (Continuation) | Total Data Bits |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `U+0000` to `U+007F` | **1 Byte** | `0xxxxxxx` | - | - | - | 7 bits (ASCII) |
| `U+0080` to `U+07FF` | **2 Bytes** | `110xxxxx` | `10xxxxxx` | - | - | 11 bits |
| `U+0800` to `U+FFFF` | **3 Bytes** | `1110xxxx` | `10xxxxxx` | `10xxxxxx` | - | 16 bits |
| `U+10000` to `U+10FFFF` | **4 Bytes** | `11110xxx` | `10xxxxxx` | `10xxxxxx` | `10xxxxxx` | 21 bits |

*   **Key Bit-Level Patterns to Remember:**
    1.  **1-Byte Pattern (`0xxxxxxx`):** Starts with `0`. The remaining 7 bits are identical to 7-bit ASCII.
    2.  **2-Byte Pattern (`110xxxxx 10xxxxxx`):** Starts with two `1`s (`110`), followed by one continuation byte (`10`).
    3.  **3-Byte Pattern (`1110xxxx 10xxxxxx 10xxxxxx`):** Starts with three `1`s (`1110`), followed by two continuation bytes (`10`).
    4.  **4-Byte Pattern (`11110xxx 10xxxxxx 10xxxxxx 10xxxxxx`):** Starts with four `1`s (`11110`), followed by three continuation bytes (`10`).
    *   *Self-Synchronization Feature:* If transmission drops a byte or starts mid-stream, the CPU can instantly tell if a byte is a start byte (`0...`, `110...`, `1110...`, `11110...`) or a continuation byte (`10...`), preventing cascading data corruption.

---

##### B. UTF-16 (Variable-Length: 2 or 4 Bytes)
UTF-16 uses **16-bit code units** (groups of 2 bytes):
*   **Characters in the Basic Multilingual Plane (BMP: `U+0000` to `U+FFFF`):**
    *   Encoded in **exactly 2 bytes** (16 bits): `xxxxxxxx xxxxxxxx`.
    *   This covers all common modern languages (English, Hindi, Greek, Chinese, etc.).
*   **Characters in Supplementary Planes (`U+10000` to `U+10FFFF`, e.g., Emojis):**
    *   Cannot fit in 16 bits. Encoded as a **Surrogate Pair** (two 16-bit units = **4 bytes total**):
        *   **High Surrogate:** A 16-bit word in the reserved range `0xD800` to `0xDBFF`.
        *   **Low Surrogate:** A 16-bit word in the reserved range `0xDC00` to `0xDFFF`.
*   *Endianness & BOM:* Because UTF-16 reads in 16-bit words, byte ordering matters:
    *   **UTF-16BE (Big Endian):** Most significant byte first.
    *   **UTF-16LE (Little Endian):** Least significant byte first (used natively inside Windows OS).
    *   **BOM (Byte Order Mark):** Code point `U+FEFF` placed at the very start of a file to declare endianness.

---

##### C. UTF-32 (Fixed-Length: Strictly 4 Bytes)
*   **Mechanism:** Completely fixed-width. Every single character occupies **exactly 4 bytes (32 bits)**, regardless of where it lies in Unicode.
*   **Bit-Level Structure:**
    *   The 32-bit register is simply the numeric code point directly zero-padded to 32 bits:
        `00000000 000xxxxx xxxxxxxx xxxxxxxx`
    *   Example: ASCII `'A'` (`U+0041`) is stored as `0x00000041` (or `00 00 00 41` in hex).
*   *Trade-off:*
    *   **Advantage:** Extreme mathematical simplicity. String length equals byte length divided by 4; indexing character at index $i$ is directly at memory address $\text{base} + 4 \times i$ in $O(1)$ time.
    *   **Disadvantage:** Massive memory inflation (3 to 4 times the size of UTF-8 for typical texts).

---

##### D. Master Comparison: UTF-8 vs. UTF-16 vs. UTF-32

| Parameter | UTF-8 | UTF-16 | UTF-32 |
| :--- | :--- | :--- | :--- |
| **Unit Size** | 8-bit byte | 16-bit word | 32-bit dword |
| **Bytes per Character** | **1, 2, 3, or 4 Bytes** | **2 or 4 Bytes** | **Strictly 4 Bytes** |
| **ASCII (0–127) Size** | **1 Byte** (100% identical to ASCII) | **2 Bytes** (padded with 1 zero byte) | **4 Bytes** (padded with 3 zero bytes) |
| **Devanagari / CJK Size** | **3 Bytes** | **2 Bytes** | **4 Bytes** |
| **Emoji / Historic Size** | **4 Bytes** | **4 Bytes** (Surrogate Pair) | **4 Bytes** |
| **ASCII Backward Compatibility** | **Yes (100%)** | **No** | **No** |
| **Endianness Sensitivity** | No (reads byte-by-byte) | Yes (requires LE/BE or BOM) | Yes (requires LE/BE or BOM) |
| **Primary Domain** | The Web (>98%), Linux, Python source | Windows API, Java/JavaScript runtimes | Specialized internal array buffers |

---

### Step-by-Step Revision Worked Examples

#### Example 1: Calculating ASCII Values and Binary Representation
*   **Question:** What is the 8-bit binary representation of the character `'E'`?
*   **Step-by-step Solution:**
    1. Recall anchor $`'A' = 65_{10}`$.
    2. Count offset:
       - `'A'` = $65$
       - `'B'` = $66$
       - `'C'` = $67$
       - `'D'` = $68$
       - `'E'` = $69_{10}$
    3. Convert decimal $69$ to 8-bit binary:
       - $69 = 64 + 4 + 1 = 2^6 + 2^2 + 2^0$
       - Binary: $\mathbf{01000101_2}$

---

#### Example 2: The Critical Exam Trap — Character `'7'` vs. Integer `7`
*   **In Computer Memory:**
    *   **Integer `7`:** Stored as pure numeric binary value:
        $$7_{10} = \mathbf{00000111_2}$$
    *   **Character `'7'` (as typed text):**
        *   Anchor `'0' = 48_{10}`.
        *   Code for `'7'` $= 48 + 7 = \mathbf{55_{10}}$.
        *   Convert $55$ to binary: $55 = 32 + 16 + 4 + 2 + 1 = \mathbf{00110111_2}$.
    *   *Takeaway:* The character `'7'` has a binary representation of $55_{10}$, completely different from numeric integer $7$!

---

#### Example 3: Converting Uppercase to Lowercase
*   **Question:** If `'K'` has ASCII code $(75)_{10}$, what is the ASCII code of `'k'` in decimal, hexadecimal, and binary?
*   **Step-by-step Solution:**
    1. Add the case offset ($+32$):
       $$\text{Code for 'k'} = 75 + 32 = \mathbf{107_{10}}$$
    2. Convert $107_{10}$ to Hexadecimal:
       - $107 \div 16 = 6$, Remainder $11$ ($\text{B}$)
       - Hex: $\mathbf{6\text{B}_{16}}$
    3. Convert $107_{10}$ to Binary:
       - $107 = 64 + 32 + 8 + 2 + 1 = \mathbf{01101011_2}$
       *(Compare with `'K'`: $75_{10} = \mathbf{01001011_2}$. Again, only bit 5 flipped from $0$ to $1$).*

---

#### Example 4: Multilingual Unicode Code Points & UTF-8 Byte Lengths
Here is how Unicode and UTF-8 represent different human writing systems:

| Character | Description | Unicode Code Point | UTF-8 Byte Size | Hex Bytes in UTF-8 |
| :---: | :---: | :---: | :---: | :---: |
| `'A'` | English Uppercase Letter | `U+0041` | **1 Byte** | `41` |
| `'9'` | Decimal Digit | `U+0039` | **1 Byte** | `39` |
| `'é'` | French Accented Letter | `U+00E9` | **2 Bytes** | `C3 A9` |
| `'Ω'` | Greek Capital Omega | `U+03A9` | **2 Bytes** | `CE A9` |
| `'अ'` | Hindi Devanagari Vowel | `U+0905` | **3 Bytes** | `E0 A4 85` |
| `'க'` | Tamil Consonant "Ka" | `U+0B95` | **3 Bytes** | `E0 AE 95` |
| `'中'` | Chinese Character "Middle" | `U+4E2D` | **3 Bytes** | `E4 B8 AD` |
| `'🚀'` | Rocket Emoji | `U+1F680` | **4 Bytes** | `F0 9F 9A 80` |

---

#### Example 5: Detailed File Storage Calculation (UTF-8 vs. UTF-32)
*   **Scenario:** A student creates a project document containing:
    *   $1,000$ standard English letters and numbers
    *   $300$ Hindi Devanagari characters
    *   $50$ Emojis
*   **Calculation under UTF-8:**
    *   English: $1,000 \times 1\text{ Byte} = 1,000\text{ Bytes}$
    *   Hindi (Devanagari): $300 \times 3\text{ Bytes} = 900\text{ Bytes}$
    *   Emojis: $50 \times 4\text{ Bytes} = 200\text{ Bytes}$
    *   $$\text{Total UTF-8 Size} = 1,000 + 900 + 200 = \mathbf{2,100\text{ Bytes}}$$
*   **Calculation under UTF-32:**
    *   Total characters $= 1,000 + 300 + 50 = 1,350\text{ characters}$.
    *   Since UTF-32 assigns strictly $4\text{ Bytes}$ to *every single character*:
    *   $$\text{Total UTF-32 Size} = 1,350 \times 4\text{ Bytes} = \mathbf{5,400\text{ Bytes}}$$
    *   *Result:* UTF-32 requires more than **$2.5\times$ the storage** of UTF-8 for the same text!

---

#### Example 6: End-to-End Bit-Level Encoding (Given Code Point $\rightarrow$ UTF-8, UTF-16, UTF-32)

Let's convert three specific characters from their Unicode Code Point into their exact binary and hexadecimal byte representation across all three UTF formats:

##### Case A: Basic ASCII Character `'A'` (`U+0041`)
*   **Code Point in Binary:** $41_{16} = 65_{10} = \mathbf{01000001_2}$ (7 data bits: `1000001`).
1.  **UTF-8:**
    *   Falls in range `U+0000` to `U+007F` $\rightarrow$ **1 Byte format (`0xxxxxxx`)**.
    *   Insert the 7 data bits into `0xxxxxxx`:
        $$\text{Result} = \mathbf{01000001_2} = \mathbf{41_{16}} \quad (1\text{ Byte})$$
2.  **UTF-16:**
    *   Falls in Basic Multilingual Plane (BMP) $\rightarrow$ direct 16-bit word:
        $$\text{Result} = \mathbf{00000000\;01000001_2} = \mathbf{0041_{16}} \quad (2\text{ Bytes})$$
3.  **UTF-32:**
    *   Direct zero-padding to 32 bits:
        $$\text{Result} = \mathbf{00000000\;00000000\;00000000\;01000001_2} = \mathbf{00000041_{16}} \quad (4\text{ Bytes})$$

---

##### Case B: Devanagari Character `'अ'` (`U+0905`)
*   **Code Point in Binary:** $0905_{16} = 2309_{10} = \mathbf{0000\;1001\;0000\;0101_2}$ (16 bits: `0000 1001 0000 0101`).
1.  **UTF-8:**
    *   Falls in range `U+0800` to `U+FFFF` $\rightarrow$ **3 Byte format**:
        $$\text{Template: } \mathbf{1110xxxx} \quad \mathbf{10xxxxxx} \quad \mathbf{10xxxxxx}$$
    *   We need 16 data bits to fill the $x$'s ($4 + 6 + 6 = 16$ slots):
        - High 4 bits: `0000`
        - Middle 6 bits: `100100`
        - Low 6 bits: `000101`
    *   Slot them into the template:
        - Byte 1: `1110` + `0000` = $\mathbf{11100000_2} = \mathbf{E0_{16}}$
        - Byte 2: `10` + `100100` = $\mathbf{10100100_2} = \mathbf{A4_{16}}$
        - Byte 3: `10` + `000101` = $\mathbf{10000101_2} = \mathbf{85_{16}}$
    *   **UTF-8 Bytes:** $\mathbf{E0\;A4\;85_{16}}$ ($3\text{ Bytes}$).
2.  **UTF-16:**
    *   Falls in BMP $\rightarrow$ direct 16-bit word:
        $$\text{Result} = \mathbf{0905_{16}} \quad (2\text{ Bytes})$$
3.  **UTF-32:**
    *   Direct zero-padding to 32 bits:
        $$\text{Result} = \mathbf{00000905_{16}} \quad (4\text{ Bytes})$$

---

##### Case C: Rocket Emoji `'🚀'` (`U+1F680`)
*   **Code Point in Binary:** $1\text{F}680_{16} = 128640_{10} = \mathbf{0001\;1111\;0110\;1000\;0000_2}$ (21 bits: `00001 111101 101000 000000`).
1.  **UTF-8:**
    *   Falls in range `U+10000` to `U+10FFFF` $\rightarrow$ **4 Byte format**:
        $$\text{Template: } \mathbf{11110xxx} \quad \mathbf{10xxxxxx} \quad \mathbf{10xxxxxx} \quad \mathbf{10xxxxxx}$$
    *   Slot the 21 bits ($3 + 6 + 6 + 6$) into the template:
        - Byte 1: `11110` + `000` = $\mathbf{11110000_2} = \mathbf{F0_{16}}$
        - Byte 2: `10` + `011111` = $\mathbf{10011111_2} = \mathbf{9F_{16}}$
        - Byte 3: `10` + `011010` = $\mathbf{10011010_2} = \mathbf{9A_{16}}$
        - Byte 4: `10` + `000000` = $\mathbf{10000000_2} = \mathbf{80_{16}}$
    *   **UTF-8 Bytes:** $\mathbf{F0\;9F\;9A\;80_{16}}$ ($4\text{ Bytes}$).
2.  **UTF-16 (Surrogate Pair Calculation):**
    *   Since $1\text{F}680 > \text{FFFF}$, it requires a surrogate pair:
        1. Subtract `0x10000`:
           $$U' = 1\text{F}680_{16} - 10000_{16} = 0\text{F}680_{16} = \mathbf{0000\;1111\;0110\;1000\;0000_2}$$
        2. High 10 bits: `0000111101` ($03\text{D}_{16}$) $\implies \text{High Surrogate} = \text{D}800_{16} + 03\text{D}_{16} = \mathbf{\text{D}83\text{D}_{16}}$.
        3. Low 10 bits: `1010000000` ($280_{16}$) $\implies \text{Low Surrogate} = \text{DC}00_{16} + 280_{16} = \mathbf{\text{DE}80_{16}}$.
    *   **UTF-16 Bytes:** $\mathbf{\text{D}83\text{D}\;\text{DE}80_{16}}$ ($4\text{ Bytes}$).
3.  **UTF-32:**
    *   Direct zero-padding to 32 bits:
        $$\text{Result} = \mathbf{0001F680_{16}} \quad (4\text{ Bytes})$$

---

### Python Connection (Where This Appears in Programming)

In Python 3, strings are Unicode by default:
```python
# ord() returns the integer Unicode / ASCII code point
print(ord('A'))       # Output: 65
print(ord('a'))       # Output: 97
print(ord('a') - ord('A'))  # Output: 32 (The case offset!)
print(ord('0'))       # Output: 48 (Not 0!)
print(ord('अ'))       # Output: 2309 (U+0905 in decimal)

# chr() converts a numerical code point back into the character glyph
print(chr(65))        # Output: 'A'
print(chr(2309))      # Output: 'अ'

# UTF-8 Byte lengths in Python
print(len('A'.encode('utf-8')))    # Output: 1 byte
print(len('अ'.encode('utf-8')))    # Output: 3 bytes
print(len('🚀'.encode('utf-8')))   # Output: 4 bytes
```

---

### Common Exam Mistakes

1.  **Thinking character `'0'` equals numeric $0$:** Character `'0'` is code $48$; character `'1'` is $49$, etc.
2.  **Claiming UTF-8 is fixed at 8 bits:** UTF-8 is **variable-length (1 to 4 bytes)**. Only ASCII characters take 8 bits.
3.  **Calling Unicode an encoding scheme:** Unicode is the *character set / code space*; UTF-8, UTF-16, and UTF-32 are the *encoding schemes*.
4.  **Forgetting that ISCII is 8-bit and backward-compatible with ASCII:** The first 128 codes of ISCII are 100% identical to 7-bit ASCII.
