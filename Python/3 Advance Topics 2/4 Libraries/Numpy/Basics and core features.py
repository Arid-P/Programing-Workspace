# NumPy Notes with Examples
# -------------------------
# NumPy (Numerical Python) is a powerful library for numerical computing. 
# It provides support for multi-dimensional arrays and a wide range of 
# mathematical operations.

# Importing NumPy
import numpy as np

# 1. Creating Arrays
# -------------------
# NumPy arrays can be created from Python lists or using built-in functions.

# Creating a 1D array
array_1d = np.array([1, 2, 3, 4, 5])
# Creating a 2D array
array_2d = np.array([[1, 2], [3, 4]])
# Creating arrays with zeros, ones, and a range of numbers
zeros_array = np.zeros((2, 3))  # 2 rows, 3 columns
ones_array = np.ones((3, 3))   # 3x3 matrix of ones
range_array = np.arange(1, 10, 2)  # Values from 1 to 10 with step 2

# 2. Array Operations
# --------------------
# NumPy supports element-wise operations such as addition, subtraction, multiplication, and division.

array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
# Element-wise addition
addition = array1 + array2
# Element-wise subtraction
subtraction = array1 - array2
# Element-wise multiplication
multiplication = array1 * array2
# Element-wise division
division = array1 / array2

# 3. Matrix Multiplication
# -------------------------
# Matrix multiplication can be performed using np.dot() or the @ operator.

matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

# Using np.dot()
dot_result = np.dot(matrix1, matrix2)
# Using @ operator
at_result = matrix1 @ matrix2

# 4. Shape and Reshaping
# -----------------------
# The shape of an array defines its dimensions. Reshaping can be used to change 
# the structure of an array without altering its data.

# Viewing the shape
original_shape = array_2d.shape
# Reshaping an array
reshaped_array = array1.reshape(3, 1)  # Reshape into 3 rows and 1 column

# 5. Broadcasting
# ----------------
# NumPy can automatically expand smaller arrays to match the shape of larger ones 
# during arithmetic operations.

array = np.array([1, 2, 3])
scalar = 2
broadcast_result = array * scalar  # Broadcast scalar to match array size

# 6. Example Outputs
# -------------------
print("1D Array:", array_1d)
print("2D Array:\n", array_2d)
print("Zeros Array:\n", zeros_array)
print("Ones Array:\n", ones_array)
print("Range Array:", range_array)

print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)

print("Matrix Multiplication (np.dot):\n", dot_result)
print("Matrix Multiplication (@ operator):\n", at_result)

print("Original Shape of 2D Array:", original_shape)
print("Reshaped Array (3 rows and 1column) :\n", reshaped_array)

print("Broadcast Result:", broadcast_result)