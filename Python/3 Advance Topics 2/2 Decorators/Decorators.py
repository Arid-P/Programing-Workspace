# ===================================================
# 🔶 DECORATORS IN PYTHON — PARTS 1 & 2 COMBINED
# ===================================================

# -------------------------------
# 🔹 What is a Decorator?
# -------------------------------
# A decorator is a function that:
# ▪ Takes another function as input
# ▪ Adds extra functionality before/after it runs
# ▪ Returns a new function

# It's used to "decorate" or wrap the original function behavior.

# -------------------------------
# 🔹 Basic Decorator (No Args)
# -------------------------------

def announce(func):
    # This is the wrapper that will replace the original function
    def wrapper():
        print("Starting the function")
        func()  # Call the actual function
        print("Function ended")
    return wrapper

@announce  # say_hi = announce(say_hi)
def say_hi():
    print("hi")

say_hi()

# Output:
# Starting the function
# hi
# Function ended

# -------------------------------
# 🔹 Decorators with Arguments
# -------------------------------
# This is needed when the function you decorate takes parameters

def log_args(func):
    def wrapper(*args, **kwargs):
        # args = all positional arguments
        # kwargs = all keyword arguments
        print(f"Calling {func.__name__} with {args} and {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_args
def multiply(x: int, y: int) -> int:
    return x * y

print(multiply(4, 5))  # Output:
# Calling multiply with (4, 5) and {}
# 20

# -------------------------------
# 🔹 Why Use Decorators?
# -------------------------------
# ✅ Add logging, authentication, timing, etc.
# ✅ Reuse behavior without modifying original functions
# ✅ Clean, modular, and scalable

# -------------------------------
# 🔹 Summary
# -------------------------------
# ▪ Use `@decorator_name` to apply a decorator
# ▪ Return a `wrapper()` from the decorator
# ▪ Use `*args` and `**kwargs` to handle functions with parameters
# ▪ Powerful for web frameworks, testing, security, etc.

# -------------------------------
# 🔹 Decorator Without @ Syntax
# -------------------------------
# Instead of writing @decorate, you can write:
# say_hello = announce(say_hello)