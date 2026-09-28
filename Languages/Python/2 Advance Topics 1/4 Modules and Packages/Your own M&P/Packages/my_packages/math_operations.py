# math_operations.py

def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

def subtract(a: int, b: int) -> int:
    """Subtract two numbers"""
    return a - b

def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

def divide(a: int, b: int) -> float:
    """Divide two numbers"""
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"