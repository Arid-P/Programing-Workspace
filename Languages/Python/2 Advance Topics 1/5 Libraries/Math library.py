# Notes for `math` Library
# This file contains explanations and code examples for working with the `math` library in Python.

# 1. Importing the `math` Library
# To use the `math` library, you need to import it first. 
# You can use an alias for convenience (optional).
import math as m

# 2. Constants in the `math` Library
# - m.pi: Represents the value of π (approximately 3.14159).
# - m.e: Represents the base of the natural logarithm (approximately 2.71828).

print(f"The value of pi is: {m.pi}")  # Printing the value of pi
print(f"The value of e is: {m.e}")  # Printing the value of e

# 3. Common Mathematical Functions

# a. Trigonometric Functions
# The `math` library provides functions for trigonometric calculations.
# - m.sin(x): Sine of x (where x is in radians).
# - m.cos(x): Cosine of x (where x is in radians).
# - m.tan(x): Tangent of x (where x is in radians).
# - m.radians(x): Converts angle x from degrees to radians.
# - m.degrees(x): Converts angle x from radians to degrees.

angle_deg = 45  # Angle in degrees
angle_rad = m.radians(angle_deg)  # Convert angle to radians

# Using the trigonometric functions
print(f"Sine of 45°: {m.sin(angle_rad)}")  # Sine of 45 degrees
print(f"Cosine of 45°: {m.cos(angle_rad)}")  # Cosine of 45 degrees

# b. Logarithmic Functions
# - m.log(x): Natural logarithm of x.
# - m.log10(x): Base-10 logarithm of x.
# - m.log2(x): Base-2 logarithm of x.

print(f"Natural logarithm of 10: {m.log(10)}")  # Natural log of 10
print(f"Log base 10 of 1000: {m.log10(1000)}")  # Base-10 log of 1000

# c. Power and Roots
# - m.pow(x, y): Returns x raised to the power y (x**y).
# - m.sqrt(x): Returns the square root of x.

print(f"2 raised to the power 3: {m.pow(2, 3)}")  # 2^3
print(f"Square root of 16: {m.sqrt(16)}")  # Square root of 16

# d. Ceiling and Floor
# - m.ceil(x): Rounds x up to the nearest integer.
# - m.floor(x): Rounds x down to the nearest integer.

print(f"Ceiling of 4.7: {m.ceil(4.7)}")  # Ceiling of 4.7
print(f"Floor of 4.7: {m.floor(4.7)}")  # Floor of 4.7

# e. Factorials
# - m.factorial(x): Returns the factorial of x, where x must be a non-negative integer.

print(f"Factorial of 5: {m.factorial(5)}")  # Factorial of 5

# f. GCD (Greatest Common Divisor) and LCM (Least Common Multiple)
# - m.gcd(a, b): Computes the greatest common divisor of a and b.
# - For Least Common Multiple (LCM), Python 3.9+ has m.lcm(a, b).

print(f"GCD of 12 and 18: {m.gcd(12, 18)}")  # GCD of 12 and 18

# g. Exponential Function
# - m.exp(x): Computes e raised to the power of x.

print(f"e raised to the power 2: {m.exp(2)}")  # e^2

# h. Specialized Functions (Python 3.8+)
# - m.comb(n, k): Number of ways to choose k items from n items without repetition (combination).
# - m.perm(n, k): Number of ways to choose k items from n items with order (permutation).

print(f"Combinations (5C2): {m.comb(5, 2)}")  # Combinations (5 choose 2)
print(f"Permutations (5P2): {m.perm(5, 2)}")  # Permutations (5P2)

# i. Comparison and Approximation
# - m.isclose(a, b): Checks if two numbers are approximately equal.
# - m.fabs(x): Returns the absolute value of x.

print(f"Is 0.1 + 0.2 close to 0.3? {m.isclose(0.1 + 0.2, 0.3)}")  # Check if 0.1 + 0.2 is close to 0.3