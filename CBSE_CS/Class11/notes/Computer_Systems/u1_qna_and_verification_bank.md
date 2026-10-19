# CBSE Class 11 Computer Science (083)
## Unit 1: Computer Systems and Organisation — QnA & Verification Bank

This document compiles all conceptual questions, numericals, and True/False verification statements covered across Unit 1, including the student's answers, technical feedback, examiner tips, and CBSE model answers.

---

### Topic 01: Hardware, Input/Output Devices, and CPU Organisation

#### Conceptual QnA
1. **Question:** A bank wants to automate the sorting and clearing of thousands of paper cheques every evening. Which input device must be used, what specific physical property allows it to work, and why isn't a standard flatbed scanner preferred?
   - **Student Answer:** MICR. It can read the magnetic ink present on the paper. A flatbed scanner isn't preferred because due to human error or random error the paper may not be correctly placed or the scan may come out blurry, but since MICR recognizes magnetic ink, whatever orientation or minor error, recognition failure is very rare.
   - **Evaluation:** **Correct.**
   - **CBSE Model Answer:** The required device is **MICR (Magnetic Ink Character Recognition)**. It detects characters printed with magnetic ink containing iron oxide. Flatbed optical scanners rely purely on optical contrast and light reflection; they easily fail due to smudges, dirt, candidate signatures, stamps, folds, or slight misorientations. MICR reads the underlying magnetic field patterns irrespective of surface dirt or markings.

2. **Question:** If an architect needs to print CAD blueprints with continuous, smooth vector curves and high dimensional precision, which output device is specified by CBSE, and why won't a standard dot matrix printer suffice?
   - **Student Answer:** A plotter. Since the blueprint must be continuous and have smooth curves, a dot matrix printer won't suffice because it cannot produce such results. Its dot matrix can never produce true smooth curves or continuous figures.
   - **Evaluation:** **Correct.**
   - **CBSE Model Answer:** A **Plotter**. Plotters utilize mechanical pens or blades to draw smooth, continuous **vector graphics** based on geometric coordinates. A Dot Matrix Printer (DMP) is an impact raster device that forms images out of a discrete grid of mechanical pins striking a ribbon, producing jagged, low-resolution dotted approximations unsuitable for precision schematics.

3. **Question:** State the exact role of the **Program Counter (PC)** register during the fetch phase of an instruction cycle. What happens to its value immediately after the fetch occurs?
   - **Student Answer:** The PC holds the next instruction to be run. During fetch the CU reads PC and fetches the data, after fetching PC is incremented to the next instruction.
   - **Evaluation:** **Correct.**
   - **CBSE Model Answer:** The **Program Counter (PC)** stores the memory address of the *next instruction* to be fetched from primary memory. During the fetch stage, the Control Unit copies this address to the Memory Address Register (MAR) and onto the Address Bus. Immediately after the instruction is retrieved from memory, the PC is automatically **incremented** to point to the subsequent sequential memory address.

4. **Question:** Differentiate between the **Address Bus** and the **Data Bus** in terms of directionality and the type of information carried.
   - **Student Answer:** AB is unidirectional as it carries the memory address from the CPU to the memory. DB is bidirectional as it needs to carry data to and from CPU.
   - **Evaluation:** **Correct.**
   - **CBSE Model Answer:**
     - **Address Bus:** *Unidirectional* (signals travel only from CPU outwards to memory and I/O devices). Carries physical memory addresses. Its width determines maximum addressable memory ($2^N$).
     - **Data Bus:** *Bidirectional* (data travels both into and out of the CPU). Transfers actual operands, program instructions, and processed data between CPU, memory, and peripherals.

#### True / False Statements
*   **Statement 1:** The Control Unit (CU) contains internal circuits for performing comparison operations like checking if $A > B$.  
    - *Answer:* **False** (Logic section of the ALU handles comparisons; CU only fetches, decodes, and routes timing signals).
*   **Statement 2:** The Address Bus is unidirectional because only the CPU generates the physical addresses for reading from or writing to memory locations.  
    - *Answer:* **True**.
*   **Statement 3:** An Inkjet printer is categorized as an impact printer because the ink droplets make physical contact with the paper surface.  
    - *Answer:* **False** (Inkjet is strictly non-impact; impact requires mechanical pins/hammers striking a ribbon).
*   **Statement 4:** The Memory Data Register (MDR) holds the instruction currently being decoded and executed by the Control Unit.  
    - *Answer:* **False** (The Instruction Register / IR holds the active instruction being decoded; MDR temporarily holds data/instructions moving over the data bus).
*   **Statement 5:** A plotter uses vector graphics rather than a raster grid of dots to produce high-precision schematics.  
    - *Answer:* **True**.

---

### Topic 02: Memory Types (Primary, Cache, Secondary) & Hierarchy Tradeoffs

#### Conceptual QnA
1. **Question:** Explain the technical reason why **Dynamic RAM (DRAM)** requires periodic electrical refreshing, whereas **Static RAM (SRAM)** does not.
   - **Student Answer:** DRAM uses capacitors which leak charges over time. So to retain those charges (data) it needs to be electrically refreshed periodically. SRAM is constructed with flip-flops or latches which don't leak any charge and hold their state until power is provided, so they don't need periodic electrical refresh.
   - **Evaluation:** **Correct.**
   - **CBSE Model Answer:** DRAM stores each bit of data in a circuit composed of a single transistor and a **capacitor**. Capacitors physically leak their stored electrical charge over milliseconds; hence, DRAM requires periodic reading and rewriting (refreshing) hundreds of times per second. SRAM stores data using multi-transistor bistable **flip-flop / latch circuits** that maintain state stably without charge dissipation as long as power is continuously supplied.

2. **Question:** In terms of CPU performance, what is the exact purpose of placing a **Cache Memory** between the CPU and primary RAM? Which principle explains why small cache memories achieve high hit rates?
   - **Student Answer:** It is to prevent memory stall of CPU. Due to the significant difference in the CPU speed and RAM memory, if the CPU directly accesses data from RAM it will need to wait a long time relatively. The principle of locality.
   - **Evaluation:** **Correct.**
   - **CBSE Model Answer:** Cache memory resolves the **speed mismatch** between the high-speed CPU (clock cycle $< 0.3\text{ ns}$) and relatively slow primary RAM ($10\text{--}50\text{ ns}$), eliminating CPU idle wait cycles (memory stalls). It achieves high hit rates via the **Principle of Locality of Reference**:
     - *Temporal Locality:* Recently referenced memory addresses are likely to be accessed again soon (e.g., loop counters).
     - *Spatial Locality:* Instructions and data stored adjacent to recently accessed addresses are likely to be accessed soon (e.g., array elements, sequential code).

3. **Question:** What is the fundamental functional difference between **RAM** and **ROM** regarding their role during the computer's bootup sequence?
   - **Student Answer:** RAM stores data that the CPU may require as well as data of currently running programs. ROM stores the most important information like boot sector, BIOS etc. which are required to even start the computer.
   - **Evaluation:** **Correct.**
   - **CBSE Model Answer:** **ROM** is *non-volatile* and stores permanent firmware: the **BIOS / UEFI** and the **Bootstrap Loader**. When power is initially switched on, the CPU immediately executes POST and the bootstrap loader directly from ROM. **RAM** is *volatile* and completely empty at power-on; its role begins only after the bootstrap loader copies the operating system kernel from secondary storage into RAM so the CPU can execute running applications.

4. **Question:** A school needs to purchase external optical media to distribute a 15 GB educational video collection on a single physical disc. Which optical media type must they choose, and why won't a standard DVD work?
   - **Student Answer:** Blu-ray. A DVD doesn't have enough capacity to hold a 15 GB file.
   - **Evaluation:** **Correct.**
   - **CBSE Model Answer:** They must select a **Blu-ray Disc (BD)** (single layer capacity is $\approx 25\text{ GB}$). A standard single-layer DVD holds only $4.7\text{ GB}$ (and dual-layer holds $8.5\text{ GB}$), neither of which can accommodate 15 GB.

#### True / False Statements
*   **Statement 1:** The CPU can directly access and execute instructions stored on a Solid State Drive (SSD) via the system bus without loading them into RAM first.  
    - *Answer:* **False** (CPU can only execute instructions residing in primary memory or cache; code on secondary storage must first be loaded into RAM).
*   **Statement 2:** Static RAM (SRAM) is constructed using flip-flop circuits and is primarily used to build cache memory.  
    - *Answer:* **True**.
*   **Statement 3:** EPROM chips are erased by applying high-voltage electrical pulses across their pins while connected to the motherboard.  
    - *Answer:* **False** (EPROM is erased by exposure to intense Ultraviolet / UV light through a quartz window; EEPROM is erased electrically).
*   **Statement 4:** As one moves downward in the memory hierarchy (from CPU registers toward secondary storage), the access time increases while the cost per bit decreases.  
    - *Answer:* **True** *(Examiner Trap: Access time is latency. Slower speed means access time increases / takes longer).*
*   **Statement 5:** Dynamic RAM offers higher storage density and lower manufacturing cost per bit compared to Static RAM.  
    - *Answer:* **True**.

---

### Topic 03: Units of Memory

#### Numerical & Conceptual QnA
1. **Question:** A solid-state drive has a capacity of **$1\text{ TB}$**. Exactly how many **Megabytes (MB)** does this drive contain according to the CBSE standard? Show your multiplication expression.
   - **Student Answer:** $\text{Memory} = 1\text{ TB} = 2^{10}\text{ GB} = 2^{20}\text{ MB}$.
   - **Evaluation:** **Correct.**
   - **CBSE Model Answer:** $1\text{ TB} = 1024\text{ GB} = 1024 \times 1024\text{ MB} = 2^{10} \times 2^{10}\text{ MB} = \mathbf{2^{20}\text{ MB}} = \mathbf{1,048,576\text{ MB}}$.

2. **Question:** A broadband connection has an advertised bandwidth of **$64\text{ Mbps}$**. What is the maximum theoretical download rate in **Megabytes per second (MB/s)**?
   - **Student Answer:** $8\text{ MBps}$.
   - **Evaluation:** **Correct.**
   - **CBSE Model Answer:** $\text{Speed in MB/s} = \frac{\text{Speed in Mbps}}{8} = \frac{64\text{ Mbps}}{8} = \mathbf{8\text{ MB/s}}$ (or $8\text{ MBps}$).

3. **Question:** How many **nibbles** are contained in **$2\text{ KB}$** of memory? Show your conversion steps.
   - **Student Answer:** $\text{Memory} = 2\text{ KB} = 2 \times 2^{10}\text{ Bytes} = 2^{11}\text{ B} = 2 \times 2^{11}\text{ Nibble} = 2^{12} = 4096\text{ Nibbles}$.
   - **Evaluation:** **Correct.**
   - **CBSE Model Answer:**
     - $1\text{ Byte} = 8\text{ bits} = 2\text{ nibbles}$.
     - $2\text{ KB} = 2 \times 1024\text{ Bytes} = 2048\text{ Bytes} = 2^{11}\text{ Bytes}$.
     - $\text{Total Nibbles} = 2048 \times 2 = \mathbf{4096\text{ nibbles}}$ ($2^{12}\text{ nibbles}$).

4. **Question:** Arrange the following 6 quantities in strictly **ascending order** of capacity:
   $A = 1024\text{ KB}$, $B = 1\text{ GB}$, $C = 2^{25}\text{ bits}$, $D = 1024\text{ Bytes}$, $E = 1\text{ PB}$, $F = 1\text{ TB}$.
   - **Student Answer:** $D < A < C < B < F < E$.
   - **Evaluation:** **Correct.**
   - **CBSE Model Answer:** Converting all to common units:
     - $D = 1024\text{ Bytes} = 1\text{ KB}$ ($2^{10}\text{ B}$)
     - $A = 1024\text{ KB} = 1\text{ MB}$ ($2^{20}\text{ B}$)
     - $C = 2^{25}\text{ bits} = \frac{2^{25}}{2^3}\text{ Bytes} = 2^{22}\text{ Bytes} = 4\text{ MB}$
     - $B = 1\text{ GB} = 1024\text{ MB}$ ($2^{30}\text{ B}$)
     - $F = 1\text{ TB} = 1024\text{ GB}$ ($2^{40}\text{ B}$)
     - $E = 1\text{ PB} = 1024\text{ TB}$ ($2^{50}\text{ B}$)
     $$\mathbf{D < A < C < B < F < E}$$

#### True / False Statements
*   **Statement 1:** In the CBSE curriculum standard, $1\text{ Petabyte (PB)}$ is equal to $2^{50}\text{ Bytes}$.  
    - *Answer:* **True** ($1\text{ PB} = 1024^5\text{ Bytes} = 2^{50}\text{ Bytes}$).
*   **Statement 2:** A 32-bit register architecture can hold exactly 8 nibbles of data simultaneously.  
    - *Answer:* **True** ($32\text{ bits} / 4\text{ bits per nibble} = 8\text{ nibbles}$).
*   **Statement 3:** If a file is $8\text{ MB}$ in size, downloading it over an ideal $8\text{ Mbps}$ network connection takes exactly 1 second.  
    - *Answer:* **False** ($8\text{ MB} = 64\text{ Mb}$. Over an $8\text{ Mbps}$ line, it takes $\frac{64}{8} = \mathbf{8\text{ seconds}}$, not 1).
*   **Statement 4:** One Terabyte (TB) contains exactly $10^{12} = 1,000,000,000,000\text{ Bytes}$ in CBSE examination marking schemes.  
    - *Answer:* **False** (CBSE strictly mandates binary base-2: $1\text{ TB} = 2^{40} = 1,099,511,627,776\text{ Bytes}$).
*   **Statement 5:** The symbol 'kbps' denotes Kilobits per second, whereas 'KBps' denotes Kilobytes per second.  
    - *Answer:* **True** (Lower-case 'b' = bits; Upper-case 'B' = Bytes).

---

### Topic 04: Software Types (System Software, Programming Tools, Application Software)

#### Conceptual QnA
1. **Question:** Differentiate between **System Utilities** and **Application Software** based on: (a) primary purpose, (b) who they serve, and (c) two specific examples of each.
   - **Student Answer:**
     - (a) SU help maintain system software/computer; AS are specialized software made for the user to perform tasks.
     - (b) SU serve system; AS serve user.
     - (c) SU: Antivirus, Disk Defragmenter; AS: Word Processor, Spreadsheet software.
   - **Evaluation:** **Correct.**
   - **CBSE Model Answer:**
     - *(a) Purpose:* System Utilities perform housekeeping, maintenance, and optimization to ensure smooth computer hardware/OS performance. Application Software solves specific real-world tasks or business problems.
     - *(b) Beneficiary:* Utilities serve the system/hardware; Application Software directly serves the end user.
     - *(c) Examples:* Utilities: Disk Defragmenter, Antivirus, 7-Zip, Backup tools. Application: MS Word, MS Excel, VLC Player, Web browsers.

2. **Question:** A user plugs a new thermal receipt printer into a computer running Linux. The printer powers on, but when a print job is sent, the OS shows an error: *"Device communication failed: Driver missing."* Explain what a **Device Driver** is, why the OS cannot print without it despite the hardware being intact, and classify it in the software hierarchy.
   - **Student Answer:** A device driver is a piece of software that tells the computer system (the OS) how to communicate with the particular device. Since the printer's device drivers are missing, the OS cannot communicate with it and hence cannot print anything.
   - **Evaluation:** **Correct.**
   - **CBSE Model Answer:** A **Device Driver** is a specialized system software program that acts as an interface/translator between the Operating System and a specific hardware peripheral. The OS issues generic, high-level I/O commands; the driver translates these commands into the unique electrical signals and proprietary control language required by that peripheral's chipset. Hierarchy: **System Software $\rightarrow$ Device Driver**.

3. **Question:** An airline commissions a software company to build an automated flight scheduling and crew roster system customized to international civil aviation norms. Classify this software under the CBSE taxonomy (down to its exact subtype), and clearly contrast it with **General Purpose Application Software**.
   - **Student Answer:** Specific Purpose software. It is designed to perform a very specific task for a particular user. General purpose software is designed to solve a mass of users' problems.
   - **Evaluation:** **Correct.**
   - **CBSE Model Answer:** Classification: **Application Software $\rightarrow$ Specific Purpose / Customized (Tailor-made / Bespoke) Software**. Unlike General Purpose software (which is packaged off-the-shelf software developed to satisfy broad, generic needs of the mass public, e.g., MS Excel), customized software is purpose-engineered to satisfy the unique workflow, legal rules, and operational requirements of a single designated client or enterprise.

4. **Question:** Define an **Integrated Development Environment (IDE)** according to CBSE. Name the **three essential software components** that must be bundled inside an IDE.
   - **Student Answer:** An IDE is a complete environment to develop software in. It has the code editor, the debugger, the compiler, and all other necessary software.
   - **Evaluation:** **Correct.**
   - **CBSE Model Answer:** An **IDE** is a comprehensive software application that provides an integrated developer environment for writing, building, testing, and debugging programs in a unified interface. Three essential components:
     1. A **Source Code Editor** (with syntax highlighting and auto-completion).
     2. A **Language Translator** (Compiler or Interpreter).
     3. An interactive **Debugger**.

#### True / False Statements
*   **Statement 1:** Antivirus software and Disk Defragmenters are classified as Application Software because they are explicitly launched and interacted with by the user.  
    - *Answer:* **False** (They are System Software $\rightarrow$ System Utilities).
*   **Statement 2:** A Device Driver is a physical integrated circuit chip located on the motherboard that controls an external peripheral.  
    - *Answer:* **False** (It is strictly software, not hardware).
*   **Statement 3:** Both Operating Systems and Language Translators fall under the broad category of System Software.  
    - *Answer:* **True / False nuance:** In traditional CBSE/2-tier classification, **True** (Translators are System Software). In NCERT 3-tier classification, Translators are listed under "Programming Tools".
*   **Statement 4:** General Purpose application software is developed to meet the custom, bespoke workflow requirements of a single designated client organization.  
    - *Answer:* **False** (That defines Customized/Bespoke software).
*   **Statement 5:** Python's default IDLE environment qualifies as an Integrated Development Environment (IDE) because it bundles an editor, an interactive interpreter shell, and a debugger.  
    - *Answer:* **True**.

---

### Topic 05: Language Translators (Assembler vs. Compiler vs. Interpreter)

#### Conceptual QnA
1. **Question:** Differentiate between a **Compiler** and an **Interpreter** on three distinct parameters: (a) unit of translation, (b) object code generation, and (c) error reporting behavior.
   - **Student Answer:** Compiler compiles whole human-readable code into machine-readable code at once and saves into an executable file; much faster. Interpreter translates line-by-line and executes simultaneously.
   - **Evaluation:** **Partially complete (2/3 marks).** Omitted parameter (c).
   - **CBSE Model Answer:**
     - *(a) Translation Unit:* Compiler translates the **entire program at once** before execution. Interpreter translates **statement-by-statement (line-by-line)**.
     - *(b) Object Code Generation:* Compiler generates an independent, permanent **standalone executable/object file** (`.exe`). Interpreter **does not generate** a permanent object file.
     - *(c) Error Reporting:* Compiler scans the entire program and lists **all syntax errors simultaneously with line numbers** at the end. Interpreter **halts execution immediately** upon encountering the first error and reports only that error.

2. **Question:** In terms of CPU efficiency, explain why a program running a $100,000$-iteration loop executes significantly faster when compiled compared to when it is interpreted.
   - **Student Answer:** When compiled, it is completely transformed into machine code and saved in a file so it runs blazingly fast. Interpreted code translates and executes in 2 steps for every line, almost doubling runtime.
   - **Evaluation:** **Correct.**
   - **CBSE Model Answer:** A compiler pre-translates the loop body into native machine code *once*. During runtime, the CPU executes raw binary instructions directly for all $100,000$ iterations. An interpreter must re-parse, decode, and translate the exact same lines of source code on *every single iteration* ($100,000$ repeated translation cycles), incurring massive computational overhead.

3. **Question:** What is an **Assembler**, and how does its input language differ from the input language accepted by a Compiler?
   - **Student Answer:** An assembler is a special language translator that only translates assembly language (a very low-level language) into machine code. A compiler translates compiled languages like C++, Java, Rust etc.
   - **Evaluation:** **Correct.**
   - **CBSE Model Answer:** An **Assembler** is a translator that converts low-level **Assembly Language** (which uses operational mnemonics such as `MOV`, `ADD`, `SUB`) into machine code. A Compiler accepts **High-Level Languages (HLL)** (which use English-like mathematical syntax, e.g., C, C++, Rust).

4. **Question:** A student claims: *"Python does not compile code at all; it translates raw English-like source text directly into electrical signals in real-time."* Explain why this statement is technically false, citing **Bytecode** and the **Python Virtual Machine (PVM)**.
   - **Student Answer:** False because Python even on interpreting produces `.pyc` files which are compiled versions of the human-readable code. The program is first compiled into intermediate bytecodes.
   - **Evaluation:** **Correct.**
   - **CBSE Model Answer:** Python is a two-stage hybrid system. When executed, the Python compiler first compiles source code (`.py`) into an intermediate, platform-independent low-level format called **Bytecode** (cached as `.pyc` files in `__pycache__`). The **Python Virtual Machine (PVM)** is the runtime engine/interpreter that executes this bytecode instruction by instruction.

#### True / False Statements
*   **Statement 1:** An interpreter generates a permanent, standalone `.exe` machine code file on secondary storage after translating a program.  
    - *Answer:* **False** (No permanent executable file is created).
*   **Statement 2:** A compiler scans the entire source program and reports all detected syntax errors together with their line numbers.  
    - *Answer:* **True**.
*   **Statement 3:** Assemblers translate human-readable high-level languages like Python and C++ into low-level assembly language.  
    - *Answer:* **False** (Translates assembly mnemonics into binary machine code).
*   **Statement 4:** An interpreted program requires both the original source code file and the interpreter software to be present on the computer every single time the program is run.  
    - *Answer:* **True**.
*   **Statement 5:** In standard Python, source code is first compiled into intermediate bytecode before being interpreted statement-by-statement by the PVM.  
    - *Answer:* **True**.

---

### Topic 06: Operating System Functions & User Interfaces (CLI vs. GUI)

#### Conceptual QnA
1. **Question:** Explain the mechanism and purpose of **Print Spooling** under the OS's Device Management function. Why is it necessary when coordinating a high-speed CPU with a slow mechanical printer?
   - **Student Answer:** The print data speed required by the printer is much lower (e.g. one page every second), but CPU/data transfer speed is very fast. The OS loads print jobs into disk/secondary storage and slowly feeds data to the printer so the CPU doesn't freeze and works efficiently.
   - **Evaluation:** **Correct.**
   - **CBSE Model Answer:** **Print Spooling (Simultaneous Peripheral Operations On-Line)** intercepts print jobs from applications and writes them to a temporary queue/buffer on secondary storage (the *spool*). Because the CPU is millions of times faster than mechanical printing hardware, spooling allows the CPU and user applications to finish immediately without being blocked (frozen) waiting for physical pages to print. The OS feeds data to the printer in the background at the printer's own pace.

2. **Question:** What is the fundamental difference between **Memory Management** and **File Management** in terms of the specific hardware component and nature of data each manages?
   - **Student Answer:** Memory management works upon primary memory (RAM) allocated/deallocated to running processes communicating directly with CPU. File management handles secondary memory, saving files/folders/directories for long-term persistent storage even after power is disconnected.
   - **Evaluation:** **Correct.**
   - **CBSE Model Answer:**
     - **Memory Management:** Governs volatile **Primary Memory (RAM)**. Tracks real-time byte addresses allocated to active running processes and CPU execution spaces.
     - **File Management:** Governs non-volatile **Secondary Storage (HDD/SSD)**. Organizes persistent files, folders, and directories in hierarchical tree structures, managing disk block allocations and access permissions.

3. **Question:** What does the acronym **WIMP** stand for in the context of Graphical User Interfaces? Which primary input device does the WIMP model rely upon?
   - **Student Answer:** Windows, Icons, Menus, Pointer. A pointing device such as a mouse.
   - **Evaluation:** **Correct.**
   - **CBSE Model Answer:** **W**indows, **I**cons, **M**enus, **P**ointer. Relies primarily on a **mouse / pointing device** (or touchscreen).

4. **Question:** A cloud architect chooses to deploy Linux enterprise servers using a pure **Command Line Interface (CLI)** with no GUI installed. State two technical advantages of a CLI over a GUI that justify this decision.
   - **Student Answer:**
     1. Hardware overhead is far less; saves GPU/CPU/RAM for actual server cloud workloads.
     2. Easy automation through scripting and full permission control.
   - **Evaluation:** **Correct.**
   - **CBSE Model Answer:**
     1. *Resource Efficiency:* A CLI consumes negligible RAM and zero graphics/GPU rendering power, leaving nearly 100% of server compute resources for actual database and network application workloads.
     2. *Scripting & Remote Automation:* CLI commands can be chained into shell scripts, automated via cron jobs, and managed seamlessly over low-bandwidth remote SSH connections.

#### True / False Statements
*   **Statement 1:** In Graphical User Interfaces, the interaction model is governed by the WIMP (Windows, Icons, Menus, Pointer) paradigm.  
    - *Answer:* **True**.
*   **Statement 2:** The Memory Management function of an Operating System is responsible for organizing files into directory trees and setting read/write permissions on hard disk drives.  
    - *Answer:* **False** (That is File Management; Memory Management tracks RAM).
*   **Statement 3:** A Command Line Interface (CLI) typically consumes significantly less RAM and CPU/GPU processing overhead than a Graphical User Interface (GUI).  
    - *Answer:* **True**.
*   **Statement 4:** Print Spooling copies print data into a temporary storage buffer so the user application does not freeze while waiting for the printer hardware.  
    - *Answer:* **True**.
*   **Statement 5:** Multitasking is impossible in a Command Line Interface (CLI) because the user can only type one command at a time on the screen.  
    - *Answer:* **False** (CLI systems like Linux Bash fully support multitasking via background jobs (`&`), daemons, terminal multiplexers, and pipes).

---

### Topics 07 & 08: Boolean Logic, Logic Gates, and De Morgan's Laws

#### Conceptual & Simplification QnA
1. **Question:** Why are **NAND** and **NOR** classified as **Universal Gates** in digital electronics? Demonstrate how a **NOT gate (Inverter)** can be constructed using only a single 2-input NAND gate.
   - **Student Answer:** Universal because we can construct all basic gates (AND, OR, NOT) using only them. Take input wire A, divide into two inputs connected to both pins of a 2-input NAND gate; output is identical to NOT gate on A.
   - **Evaluation:** **Correct.**
   - **CBSE Model Answer:** They are classified as **Universal Gates** because any Boolean logic function (AND, OR, NOT) can be synthesized using *only* NAND gates or *only* NOR gates without any other gate type.
     - *NOT gate from 2-input NAND:* Tie both input pins together to a common input signal $A$. Output $= \overline{A \cdot A} = \overline{A}$.

2. **Question:** State **De Morgan's First and Second Laws** both in words and as algebraic formulas.
   - **Student Answer:**
     - 1st: Complement of logical product of two terms is equal to logical sum of individual complements: $(A \cdot B)' = A' + B'$.
     - 2nd: Complement of logical sum of two terms is equal to logical product of individual complements: $(A + B)' = A' \cdot B'$.
   - **Evaluation:** **Correct.**
   - **CBSE Model Answer:**
     - **First Law:** The complement of a logical product (AND) is equal to the logical sum (OR) of the individual complements:
       $$\overline{A \cdot B} = \overline{A} + \overline{B} \quad (\text{NAND} \equiv \text{Bubbled OR})$$
     - **Second Law:** The complement of a logical sum (OR) is equal to the logical product (AND) of the individual complements:
       $$\overline{A + B} = \overline{A} \cdot \overline{B} \quad (\text{NOR} \equiv \text{Bubbled AND})$$

3. **Question:** Simplify the following Boolean expression algebraically, stating the specific Boolean law used at every step:
   $$F = A \cdot B + A \cdot (B + C) + B \cdot (B + C)$$
   - **Student Answer:**
     $= AB + AB + AC + BB + BC$ (Distributive)  
     $= AB + AC + B + BC$ (Idempotent: $AB+AB=AB$, $BB=B$)  
     $= AB + BC + B + AC$  
     $= (A + C + 1)B + AC$ (Factoring $B$)  
     $= B + AC$ (Dominance: $1 + A + C = 1$)  
     $\mathbf{F = B + AC}$
   - **Evaluation:** **Flawless.** 100% mathematically correct and all laws cited accurately.

4. **Question:** Write the truth table for a 2-input **XOR gate**. What is the exact behavioral rule determining when an XOR gate outputs logic $1$?
   - **Student Answer:** Wrote truth table with last row $1 \oplus 1 = 1$. Unsure of exact behavioral rule.
   - **Evaluation:** **Correction needed on row 4.**
   - **CBSE Model Answer:**
     | A | B | $Y = A \oplus B$ |
     | :-: | :-: | :-: |
     | 0 | 0 | **0** |
     | 0 | 1 | **1** |
     | 1 | 0 | **1** |
     | 1 | 1 | **0** |
     - *Behavioral Rule:* An XOR gate outputs logic $1$ **if and only if its inputs are different / unequal** ($0, 1$ or $1, 0$). If both inputs are identical ($0, 0$ or $1, 1$), it outputs logic $0$.

#### True / False Statements
*   **Statement 1:** An XOR gate outputs logic $1$ when both of its inputs are logic $1$.  
    - *Answer:* **False** ($1 \oplus 1 = 0$).
*   **Statement 2:** According to De Morgan's laws, a NOR gate is functionally equivalent to a Bubbled AND gate (an AND gate with inverted inputs).  
    - *Answer:* **True** ($\overline{A + B} = \overline{A} \cdot \overline{B}$).
*   **Statement 3:** The Boolean expression $A + \overline{A} \cdot B$ simplifies directly to $A + B$.  
    - *Answer:* **True** (Redundant literal rule / distributive law: $(A + \overline{A})(A + B) = 1 \cdot (A + B) = A + B$).
*   **Statement 4:** In Boolean algebra, the Second Distributive Law states that $A + (B \cdot C) = (A + B) \cdot (A + C)$.  
    - *Answer:* **True**.
*   **Statement 5:** A 2-input NAND gate produces an output of $0$ only when both of its inputs are $0$.  
    - *Answer:* **False** (NAND outputs $0$ only when both inputs are $1$).

---

### Topic 09: Number Systems & Multi-Directional Conversions

#### Conversion Problems
1. **Decimal to Binary:** Convert $(45.625)_{10}$ to its exact **Binary** equivalent.
   - **Student Answer:** `(101101.101)2`.
   - **Evaluation:** **Correct.**
   - **CBSE Steps:**
     - Integer: $45 \div 2 \rightarrow 22$ R $1$; $11$ R $0$; $5$ R $1$; $2$ R $1$; $1$ R $0$; $0$ R $1 \implies (101101)_2$.
     - Fractional: $0.625 \times 2 = 1.25$ (1); $0.25 \times 2 = 0.5$ (0); $0.5 \times 2 = 1.0$ (1) $\implies (.101)_2$.
     - Result: $\mathbf{(101101.101)_2}$.

2. **Binary to Decimal & Hexadecimal:** Convert $(110110.11)_2$ to:
   - (a) **Decimal:**
     - **Student Answer:** `(54.75)10`.
     - **Evaluation:** **Correct.** ($32 + 16 + 4 + 2 + 0.5 + 0.25 = \mathbf{54.75_{10}}$).
   - (b) **Hexadecimal:**
     - **Student Answer:** `(36.C)16`.
     - **Evaluation:** **Correct.**
     - Integer: $\underbrace{0011}_{3} \;\underbrace{0110}_{6} \implies 36_{16}$.
     - Fraction: $\underbrace{1100}_{\text{C}} \implies \text{C}_{16}$. Result: $\mathbf{(36.\text{C})_{16}}$.

3. **Octal to Hexadecimal (via Binary Bridge):** Convert $(734)_8$ directly to **Hexadecimal**.
   - **Student Answer:** `734)8 = (111 011 100)2 = (1 1101 1100)2 = (1DC)16`.
   - **Evaluation:** **Correct.**
   - Step 1 (Octal to 3-bit Binary): $7 \rightarrow 111, 3 \rightarrow 011, 4 \rightarrow 100 \implies (111011100)_2$.
   - Step 2 (Regroup into 4-bit Nibbles): $\underbrace{0001}_{1} \;\underbrace{1101}_{\text{D}} \;\underbrace{1100}_{\text{C}} \implies \mathbf{(1\text{DC})_{16}}$.

4. **Hexadecimal to Octal (via Binary Bridge):** Convert $(\text{B}2)_{16}$ directly to **Octal**.
   - **Student Answer:** `(B2)16 = (1011 0010)2 = (010 110 010)2 = (262)8`.
   - **Evaluation:** **Correct.**
   - Step 1 (Hex to 4-bit Binary): $\text{B} \rightarrow 1011, 2 \rightarrow 0010 \implies (10110010)_2$.
   - Step 2 (Regroup into 3-bit Triplets): $\underbrace{010}_{2} \;\underbrace{110}_{6} \;\underbrace{010}_{2} \implies \mathbf{(262)_8}$.

#### True / False Statements
*   **Statement 1:** In hexadecimal notation, the symbol 'E' represents the decimal value $14$.  
    - *Answer:* **True** ($\text{A}=10, \text{B}=11, \text{C}=12, \text{D}=13, \text{E}=14, \text{F}=15$).
*   **Statement 2:** When converting a fractional binary number to octal, grouping of 3 bits must proceed from right to left starting from the extreme right digit.  
    - *Answer:* **False** (Fractional bits must group **left-to-right** starting from the radix point, padding zeroes on the right).
*   **Statement 3:** The octal number $(384)_8$ is a valid representation in base 8.  
    - *Answer:* **False** (Base 8 only permits digits $0\text{--}7$; digit $8$ is invalid).
*   **Statement 4:** The hexadecimal number $(2\text{F})_{16}$ is equivalent to the decimal value $47$.  
    - *Answer:* **True** ($2 \times 16 + 15 = 32 + 15 = 47_{10}$).
*   **Statement 5:** Converting an octal number to binary requires substituting each octal digit with a 3-bit binary group because $2^3 = 8$.  
    - *Answer:* **True**.

---

### Topic 10: Encoding Schemes (ASCII, ISCII, and Unicode: UTF-8, UTF-32)

#### Conceptual & Calculation QnA
1. **Question:** The ASCII code for uppercase character `'D'` is $(68)_{10}$. Calculate the 8-bit binary representation for lowercase character `'f'`. Show your intermediate decimal addition step.
   - **Student Answer:** `(102)10 = (1100110)2`.
   - **Evaluation:** **Correct.**
   - **CBSE Steps:**
     - Offset from `'D'` to `'F'` is $+2 \implies \text{'F'} = 68 + 2 = 70_{10}$.
     - Add case offset ($+32$): $\text{'f'} = 70 + 32 = \mathbf{102_{10}}$.
     - Convert $102_{10}$ to binary: $64 + 32 + 4 + 2 = \mathbf{(01100110)_2}$.

2. **Question:** Differentiate between standard **7-bit ASCII** and **8-bit ISCII** in terms of total character capacity and regional language support. How does ISCII ensure seamless font transliteration between different Indian languages?
   - **Student Answer:** 7-bit ASCII accommodates English and control characters, 128 characters. ISCII accommodates Indian characters along with English. First 128 are identical to ASCII, next 128 are Indian scripts. ISCII transliterates by assigning a single character code to a sound across languages.
   - **Evaluation:** **Correct.**
   - **CBSE Model Answer:** Standard ASCII is a **7-bit** encoding supporting $2^7 = \mathbf{128\text{ characters}}$, strictly limited to English and basic control symbols. ISCII is an **8-bit** encoding supporting $2^8 = \mathbf{256\text{ characters}}$; its lower 128 are identical to 7-bit ASCII, while the upper 128 encode scripts derived from Brahmi (Devanagari, Tamil, Bengali, etc.). It facilitates instant font transliteration because it assigns the **exact same code byte to phonetically identical characters across all Indian scripts**. Changing the font on an ISCII byte stream renders the text in a different Indian script without changing the underlying data.

3. **Question:** A student states: *"UTF-8 is an 8-bit fixed encoding scheme just like Extended ASCII."* Disprove this statement by explaining the variable-width allocation mechanism of UTF-8 and stating how many bytes it allocates to: (a) English ASCII characters, (b) Indian Devanagari script characters, and (c) Emojis.
   - **Student Answer:** It is not fixed; uses variable lengths. English: 1 byte (8 bits). Devanagari: 2 bytes (16 bits). Emojis: 4 bytes (32 bits).
   - **Evaluation:** **Partially correct (Devanagari correction).**
   - **CBSE Model Answer:** UTF-8 is **variable-width**, dynamically allocating **1 to 4 bytes** per character depending on code point range:
     - *(a) Standard English ASCII (`U+0000` to `U+007F`):* **1 Byte** (`0xxxxxxx`).
     - *(b) Indian Devanagari characters (`U+0900` to `U+097F`):* **3 Bytes** (`1110xxxx 10xxxxxx 10xxxxxx`). *(Note: 2 bytes only covers up to `U+07FF`; Devanagari falls in the 3-byte range `U+0800` to `U+FFFF`)*.
     - *(c) Emojis (`U+10000` to `U+10FFFF`):* **4 Bytes** (`11110xxx 10xxxxxx 10xxxxxx 10xxxxxx`).

4. **Question:** A digital article contains: $600$ standard English characters, $150$ Hindi Devanagari characters, and $25$ modern Emojis. Calculate the total storage requirement of this document in **Bytes** when stored under: (a) **UTF-8**, (b) **UTF-32**.
   - **Student Answer:**
     - (a) $600\times 1 + 150\times 2 + 25\times 4 = 1000\text{ Bytes}$ *(used 2 bytes for Devanagari)*.
     - (b) $(600 + 150 + 25)\times 4 = 775 \times 4 = 3100\text{ Bytes}$.
   - **Evaluation:** **(b) is correct; (a) adjusted for 3 bytes.**
   - **CBSE Model Answer:**
     - *(a) UTF-8:*
       - English: $600 \times 1\text{ Byte} = 600\text{ Bytes}$
       - Devanagari: $150 \times \mathbf{3\text{ Bytes}} = 450\text{ Bytes}$
       - Emojis: $25 \times 4\text{ Bytes} = 100\text{ Bytes}$
       - Total $= 600 + 450 + 100 = \mathbf{1150\text{ Bytes}}$.
     - *(b) UTF-32:*
       - Fixed 4 bytes for all characters: $(600 + 150 + 25) \times 4\text{ Bytes} = 775 \times 4 = \mathbf{3100\text{ Bytes}}$.

#### True / False Statements
*   **Statement 1:** In standard ASCII, adding $(32)_{10}$ to the code point of any uppercase English letter yields the exact code point of its corresponding lowercase letter.  
    - *Answer:* **True**.
*   **Statement 2:** The character symbol `'0'` and the numeric integer $0$ have identical binary representations in computer memory.  
    - *Answer:* **False** (Character `'0'` is ASCII code $48 = 00110000_2$; Integer $0 = 00000000_2$).
*   **Statement 3:** Any valid ASCII text file is simultaneously a valid UTF-8 encoded text file without requiring any character translation.  
    - *Answer:* **True** (100% backward compatible).
*   **Statement 4:** In UTF-32, the standard English character `'A'` consumes exactly 1 byte of storage space.  
    - *Answer:* **False** (UTF-32 assigns strictly 4 bytes to every character).
*   **Statement 5:** ISCII uses a 16-bit encoding system to represent Indian scripts.  
    - *Answer:* **False** (ISCII is an 8-bit encoding standard).

