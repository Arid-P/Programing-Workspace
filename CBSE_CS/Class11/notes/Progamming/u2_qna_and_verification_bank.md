# CBSE Class 11 Computer Science (083)
## Unit 2: Raw QnA & Verification Archive

This file records the **exact, raw questions** presented during the sessions, the **exact, verbatim answers** submitted by the student (unedited), and the **CBSE model solutions / corrections**.

---

### Topic 01 & 02: Problem Solving Steps, Flowcharting, Pseudocode, and Decomposition

#### Raw Questions Given:
##### Conceptual QnA
1. In CBSE marking schemes, what is the precise difference between **Testing** and **Debugging**? Explain why testing can succeed in finding bugs while debugging might still fail.
2. If an algorithm is given to compute $1 / (x - 5)$, which essential characteristic of an algorithm is violated when $x = 5$ if no conditional check is included?
3. What is the geometric difference in a flowchart between reading an integer from the keyboard (`n = int(input())`) versus assigning a computed value to a variable (`count = count + 1`)? Name both shapes.
4. Explain the principle of **Decomposition** in problem-solving and name two concrete software engineering benefits it provides.

##### True / False Statements
* Statement 1: A connector symbol in a flowchart is represented by a small triangle.
* Statement 2: Pseudocode must follow the exact indentation and syntax rules of the target programming language to be considered valid.
* Statement 3: An algorithm must produce at least one output, but can accept zero inputs.
* Statement 4: The Decision box (Diamond) can have only one incoming path and must have at least two exiting alternative flow lines.
* Statement 5: Testing is carried out before the coding phase is initiated.

#### Raw Student Answer (Verbatim):
> Testing is the process of finding if the program has any error by running it with known test datasets. While debugging is the process of diagnosis and correcting a known error by finding it in the source code.
> 
> The definiteness of the algorithm is violated here, as for x equals to 5, the algorithm is not clearly defined.
> 
> The main geometric difference in a flowchart between reading an integer would be that it is present in a parallel diagram to show that it is either an input or an output, while assigning a computed value to a variable is present in a rectangular box to show that it is a process that is present.
> 
> The principle of decomposition is breaking a large problem into smaller sub-problems which are independent of each other, hence can be solved alone and after solving each one of them We can combine them both and we get the solution to the meal.
> 2 main and concrete benefits that software engineer see through it that large problems or problems he has to ask. Now there is a small problem that needs to be solved and each one of them or each one of the problems are loosely solved about it. Hence there is not much hassle within solving each one of them and then combining back. Second, it saves the opponent time or kicking time that now we have to do this and all that new. After breaking down, each shoon of the dungeon independently sorts these without heading to plan.
> 
> f, t, f, t, f

#### CBSE Evaluation & Model Answers:
*   **Q1:** **Correct.** Testing is executing a program with known inputs to detect anomalies, failures, or incorrect outputs. Debugging is the subsequent diagnostic phase of identifying the root cause in the source code and removing the defect.
*   **Q2:** **Correct.** **Definiteness** (and **Effectiveness**) is violated. At $x = 5$, $1/(5 - 5) = 1/0$ is mathematically undefined. Every instruction of an algorithm must have a single, definite meaning and must be computationally feasible.
*   **Q3:** **Correct.** Reading an input is placed in a **Parallelogram** (Input/Output symbol). Variable assignments and arithmetic computations are placed in a **Rectangle** (Process symbol).
*   **Q4:** **Correct.** Decomposition is top-down modularization: breaking a complex problem into independent, smaller sub-problems. Key benefits:
    1. *Reduced Complexity / Cognitive Load:* Sub-problems are easier to implement, test, and maintain in isolation.
    2. *Reusability & Team Parallelism:* Modules can be reused across different programs or developed concurrently by multiple developers.
*   **True/False Statements:** `f, t, f, t, f` (3/5 Correct)
    *   *Correction on Statement 2:* Statement 2 is **FALSE**. Pseudocode is intentionally informal, language-agnostic, and relaxed; it does not follow strict syntax, keywords, or punctuation of any specific compiler/interpreter.
    *   *Correction on Statement 3:* Statement 3 is **TRUE**. An algorithm can take zero inputs (e.g., an algorithm that prints the first 50 Fibonacci numbers or current time requires no external input), but it **must** produce at least one output to be meaningful.

