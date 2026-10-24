# NumPy Advanced Topics Notes
# ---------------------------
import numpy as np
import time

# 1. Array Indexing and Slicing
# ---------------------------
# Basic Indexing
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(f"array: {array}")
# Access an element at row 1, column 2
element = array[1, 2]  # Element at 2nd row, 3rd column (value: 6)
print("Element at (1, 2):", element)

# Access an entire row (2nd row)
row = array[1]
print("Second row:", row)

# Access an entire column (3rd column)
column = array[:, 2]
print("Third column:", column)

# Fancy Indexing: Accessing multiple rows
indices = [0, 2]
fancy_row = array[indices]
print("Rows at indices [0, 2]:\n", fancy_row)

# Boolean Indexing: Access elements greater than 5
mask = array > 5
filtered = array[mask]
print("Filtered elements (greater than 5):\n", filtered)

print()
# 2. Mathematical and Statistical Functions
# ----------------------------------------
# Sum, Mean, and Standard Deviation
sum_result = array.sum()  # Sum of all elements
mean_result = array.mean()  # Mean of all elements
std_result = array.std()  # Standard deviation of all elements
print("Sum:", sum_result)
print("Mean:", mean_result)
print("Standard Deviation:", std_result)

# Axis-wise Operations (Row and Column-wise Sum)
row_sum = array.sum(axis=1)  # Sum along rows
col_sum = array.sum(axis=0)  # Sum along columns
print("Sum along rows:", row_sum)
print("Sum along columns:", col_sum)

print()
# 3. Linear Algebra
# -----------------
# Determinant and Inverse of a Matrix
matrix = np.array([[1, 2], [3, 4]])
det_result = np.linalg.det(matrix)  # Determinant of the matrix
inv_result = np.linalg.inv(matrix)  # Inverse of the matrix
print(f"matrix: {matrix}")
print("Determinant:", det_result)
print("Inverse:\n", inv_result)

# Eigenvalues and Eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(matrix)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)

print()
# 4. Random Number Generation
# ---------------------------
# Random integers between 0 and 10 (3x3 array)
random_integers = np.random.randint(0, 10, size=(3, 3))
print("Random Integers:\n", random_integers)

# Random floats between 0 and 1 (3x3 array)
random_floats = np.random.rand(3, 3)
print("Random Floats (0-1):\n", random_floats)

# Random numbers from a normal distribution (3x3 array)
normal_dist = np.random.randn(3, 3)
print("Random Numbers from Normal Distribution:\n", normal_dist)

print()
# 5. Performance Comparison: NumPy vs Python Lists
# ------------------------------------------------
# Comparing sum operation in NumPy and Python lists

# Python list example
python_list = [i for i in range(1000000)]
start_time = time.time()
sum(python_list)  # Summing elements in Python list
print("Python List Sum Time:", time.time() - start_time)

# NumPy array example
numpy_array = np.array([i for i in range(1000000)])
start_time = time.time()
numpy_array.sum()  # Summing elements in NumPy array
print("NumPy Array Sum Time:", time.time() - start_time)

print()
# 6. Manipulating Arrays
# ----------------------
# Stacking arrays vertically (row-wise) and horizontally (column-wise)
array1 = np.array([1, 2, 3, 4])
array2 = np.array([4, 5, 6, 7])

# Vertical Stack (row-wise)
vertical_stack = np.vstack((array1, array2))
# Horizontal Stack (column-wise)
horizontal_stack = np.hstack((array1, array2))

print("Vertical Stack:\n", vertical_stack)
print("Horizontal Stack:", horizontal_stack)

# Splitting an array into two parts
split_array = np.split(array1, 2)
print("Split Array:", split_array)

print()
# 7. Universal Functions (ufuncs)
# ------------------------------
# Element-wise functions: np.sin, np.exp, np.sqrt

print(f"array1: {array1}")
# Apply sin function element-wise
sine_values = np.sin(array1)
print("Sine of each element:", sine_values)

# Apply exponential function element-wise
exp_values = np.exp(array1)
print("Exponential of each element:", exp_values)

# Apply square root function element-wise
sqrt_values = np.sqrt(array1)
print("Square root of each element:", sqrt_values)