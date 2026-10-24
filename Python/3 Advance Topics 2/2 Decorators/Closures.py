# =========================================
# 🔷 CLOSURES IN PYTHON
# =========================================

# ----------------------------
# 🔹 What is a Closure?
# ----------------------------
# A closure is a function defined inside another function that remembers
# the variables from the outer function even after the outer function is done.

def outer(x: int):
    def inner(y: int) -> int:
        return x + y  # x is "remembered" from outer
    return inner  # inner is returned as a closure

# ----------------------------
# 🔹 Example Usage
# ----------------------------

add_5 = outer(5)
print(add_5(10))  # 15
print(add_5(7))   # 12
# inner() remembers x = 5 even though outer() is finished

# ----------------------------
# 🔹 Real-World Style Use
# ----------------------------

def tax_calculator(rate: float):
    def calculate_tax(amount: float) -> float:
        return amount * rate
    return calculate_tax

gst_18 = tax_calculator(0.18)
print(gst_18(1000))  # 180.0

# ----------------------------
# 🔹 Why Use Closures?
# ----------------------------
# ✅ Maintain state without global variables or classes
# ✅ Create function factories
# ✅ Required for decorators

# ----------------------------
# ✅ Summary
# ----------------------------
# ▪ Closure = function + remembered environment
# ▪ Use when you want functions that carry some memory
# ▪ Very useful for decorators, counters, and factories