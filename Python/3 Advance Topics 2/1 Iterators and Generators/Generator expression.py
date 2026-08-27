# =========================================
# 🔶 GENERATOR EXPRESSIONS IN PYTHON
# =========================================

# ----------------------------
# 🔹 What are Generator Expressions?
# ----------------------------
# A generator expression is a concise way to create a generator
# — similar to list comprehensions, but it uses parentheses () instead of square brackets [].

# Example:
gen = (x**2 for x in range(5))  # This creates a generator that yields squares of 0 to 4

# You can use next() to get values one by one
print(next(gen))  # 0
print(next(gen))  # 1
print(next(gen))  # 4

# ----------------------------
# 🔹 Why Use Them?
# ----------------------------
# ✅ More memory-efficient than list comprehensions
# ✅ Useful for processing large data sets lazily (on-demand)

# Example: List comprehension vs Generator expression
squares_list = [x**2 for x in range(10)]   # Creates entire list in memory
squares_gen = (x**2 for x in range(10))    # Creates generator, lazy evaluation

# ----------------------------
# 🔹 Where Can You Use Generator Expressions?
# ----------------------------
# You can use them directly with built-in functions like sum(), any(), all(), max(), etc.

# Example 1: Sum of first 100 squares
print(sum(x**2 for x in range(1, 101)))  # 338350

# Example 2: Check if any number > 50 in list
nums = [10, 20, 30, 40, 60]
print(any(x > 50 for x in nums))  # True

# Example 3: Filter even numbers using generator expression
evens = (x for x in range(10) if x % 2 == 0)
for num in evens:
    print(num)  # 0 2 4 6 8

# ----------------------------
# 🔸 Note:
# ----------------------------
# Once a generator is exhausted, you cannot reuse it.
gen = (x for x in range(3))
print(list(gen))  # [0, 1, 2]
print(list(gen))  # [] → empty on second use

# ----------------------------
# ✅ Summary
# ----------------------------
# ▪ Syntax: (expression for item in iterable if condition)
# ▪ Saves memory by yielding values one at a time
# ▪ Very useful for large data, streaming, or lazy computations