# Unit 1: Computer Systems and Organisation (Topics 01–03)

## 01. Basic Computer Organisation: Hardware, I/O Devices, and CPU

- **Mental model:** 
  A computer functions like a corporate office: Input devices are the mailroom clerks bringing raw material in; Output devices are the dispatch clerks printing reports; the CPU is the executive suite where the Control Unit acts as the operations manager delegating tasks, the ALU is the specialized math/analyst team crunching the numbers, Registers are sticky notes on the manager's desk for active work, and System Buses are the internal hallways connecting everyone.

- **Key facts / definitions:**
  - **Hardware vs Software:** Hardware is physical and tangible; software is an intangible set of instructions and programs directing the hardware.
  - **Input vs Output:** Input converts external data into machine-readable binary ($0/1$); output converts processed binary into human-readable format.
  - **Specialised I/O:**
    - MICR (Magnetic Ink Character Recognition): Reads characters printed in magnetic ink (iron oxide); used on bank cheques.
    - OMR (Optical Mark Recognition): Detects pencil/pen marks on fixed coordinates (evaluation sheets).
    - OCR (Optical Character Recognition): Converts images of text into editable machine-encoded text.
    - Impact vs Non-impact Printers: Impact uses mechanical strikes with ribbon (Dot Matrix); Non-impact uses toner/ink without physical striking (Laser, Inkjet).
    - Plotter: High-precision vector graphics drawing device.
  - **CPU Components:**
    - **ALU (Arithmetic Logic Unit):** Performs arithmetic ($+, -, *, /$) and logical/relational decisions ($<, >, ==, \text{AND}, \text{OR}$).
    - **CU (Control Unit):** Supervises the system; fetches and decodes instructions, issues timing/control signals. *Does not compute, execute, or store data.*
    - **Registers:** High-speed internal CPU storage. PC (holds next instruction address), IR (holds current instruction), MAR (memory address), MDR (memory data), AC (intermediate ALU results).
  - **System Bus:**
    - Address Bus: Unidirectional (CPU $\rightarrow$ Memory/IO).
    - Data Bus: Bidirectional.
    - Control Bus: Bidirectional (control & timing pulses).

- **Worked example:**
  - Task: Compute $Z = X + Y$.
  - Execution: CU fetches the ADD instruction pointed to by the Program Counter (PC) via Address Bus/MAR into Instruction Register (IR). Operands are retrieved into data registers via Data Bus. ALU performs addition. Intermediate sum lands in the Accumulator (AC) before being written back to memory.

- **Common exam mistakes:**
  - Stating that the Control Unit (CU) "executes instructions" or "stores data" (it does neither; it only fetches, decodes, and orchestrates signals).
  - Calling the Address Bus "bidirectional" (the address bus is strictly unidirectional from the CPU to memory/devices).
  - Confusing OCR (Optical Character Recognition - optical character to text conversion) with OMR (Optical Mark Recognition - optical mark presence detection).

---

## 02. Memory Hierarchy, Primary, Cache, and Secondary Storage

- **Mental model:**
  Think of a chef cooking in a commercial kitchen:
  - Registers: The ingredients currently in the chef's hands.
  - Cache: The prep cutting-board right beside the stove (very fast, holds only immediate ingredients).
  - Primary Memory (RAM): The countertop/pantry in the kitchen (holds all ingredients for the current shift; wiped clean every night = volatile).
  - Secondary Storage (SSD/HDD): The deep-freeze warehouse down the street (huge capacity, permanent, but takes time to go fetch items into the kitchen).

- **Key facts / definitions:**
  - **Memory Hierarchy Tradeoff:** Moving downward: Speed decreases (access time increases), Capacity increases, Cost-per-bit decreases.
  - **Cache Memory:** High-speed buffer between CPU and RAM to resolve the CPU-memory speed mismatch. Built from SRAM; operates on the Principle of Locality (Temporal & Spatial).
  - **RAM vs ROM:**
    - RAM: Random Access Memory; Read/Write; Volatile; stores running OS and active programs.
    - ROM: Read Only Memory; Non-volatile; stores startup firmware (BIOS/UEFI and bootstrap loader).
  - **SRAM vs DRAM:**
    - SRAM: Uses flip-flops; faster; does NOT require refreshing; less dense, expensive; used in Cache.
    - DRAM: Uses transistor + capacitor; slower; REQUIRES periodic electrical refreshing (capacitors leak charge); dense, cheaper; used in Main RAM.
  - **ROM Types:** PROM (programmed once), EPROM (erased by UV light), EEPROM (erased electrically).
  - **Secondary Storage:** Persistent/non-volatile; cannot be directly executed by CPU.
    - HDD (magnetic platters, mechanical latency).
    - SSD (NAND flash, no moving parts, fast, shock-resistant).
    - Optical: CD (700 MB), DVD (4.7 GB), Blu-ray (25–50 GB).

- **Worked example:**
  - When booting up a PC:
    1. CPU reads the bootstrap loader permanently stored in ROM (non-volatile).
    2. Bootstrap loader copies the OS kernel from Secondary Storage (SSD/HDD) into Primary Memory (DRAM).
    3. CPU executes OS instructions from DRAM, buffering active loops in SRAM Cache.

- **Common exam mistakes:**
  - Saying the CPU directly executes programs from secondary storage (CPU can only execute from primary memory/cache).
  - Confusing SRAM and DRAM roles (e.g., claiming DRAM is used in cache memory; DRAM is main memory, SRAM is cache).
  - Forgetting why DRAM requires refreshing (capacitors physically leak electric charge over milliseconds).
  - Calling ROM volatile (ROM is strictly non-volatile).
  - Conflating access time with access speed: access time *increases* as you move downward (it takes longer).

---

## 03. Units of Memory

- **Mental model:**
  Data storage works like building a skyscraper out of microscopic Lego bricks:
  - 1 bit: A single light switch (ON/OFF, 1/0).
  - 1 nibble: A cluster of 4 switches (can represent one hexadecimal digit).
  - 1 Byte: 8 switches grouped together (the standard envelope size to encode a single text character).
  - Every step up to the next metric prefix (KB, MB, GB, TB, PB) multiplies by 1024 ($2^{10}$), not 1000, because binary systems count in powers of 2.

- **Key facts / definitions:**
  - **Bit:** Smallest elementary unit of data ($0$ or $1$).
  - **Nibble:** Group of 4 bits.
  - **Byte:** Group of 8 bits ($1\text{ B} = 8\text{ bits}$).
  - **The 1024 Scaling Standard (Base-2):**
    - $1\text{ KB (Kilobyte)} = 1024\text{ Bytes} = 2^{10}\text{ Bytes}$
    - $1\text{ MB (Megabyte)} = 1024\text{ KB} = 2^{20}\text{ Bytes}$
    - $1\text{ GB (Gigabyte)} = 1024\text{ MB} = 2^{30}\text{ Bytes}$
    - $1\text{ TB (Terabyte)} = 1024\text{ GB} = 2^{40}\text{ Bytes}$
    - $1\text{ PB (Petabyte)} = 1024\text{ TB} = 2^{50}\text{ Bytes}$
    - $1\text{ EB (Exabyte)} = 1024\text{ PB} = 2^{60}\text{ Bytes}$
    - $1\text{ ZB (Zettabyte)} = 1024\text{ EB} = 2^{70}\text{ Bytes}$
    - $1\text{ YB (Yottabyte)} = 1024\text{ ZB} = 2^{80}\text{ Bytes}$
  - **Symbol Case Matters:**
    - Small 'b' = bit (used for network transfer speed / bandwidth, e.g., Mbps).
    - Capital 'B' = Byte (used for file size and storage memory capacity, e.g., MB).
    - $1\text{ Byte/s} = 8\text{ bits/s}$.

- **Worked example:**
  - How many bits are there in $2\text{ MB}$?
    $$\text{Bytes} = 2 \times 1024 \times 1024 = 2 \times 2^{20} = 2^{21}\text{ Bytes}$$
    $$\text{Bits} = 2^{21}\text{ Bytes} \times 8 = 2^{21} \times 2^3 = 2^{24}\text{ bits} = 16,777,216\text{ bits}$$

- **Common exam mistakes:**
  - Using $1000$ instead of $1024$ in numerical conversions (e.g., writing $1\text{ KB} = 1000\text{ Bytes}$).
  - Confusing bits with bytes due to casing ('b' vs 'B') when calculating network transfer times or data quotas.
  - Forgetting that a nibble is 4 bits (half a byte).

