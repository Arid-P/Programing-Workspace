import sys

def add_path_cwd() -> None:
    sys.path.append("/storage/emulated/0/Programing/Python/")  # Add current directory to sys.path
    return

# Change directory and update sys.path
add_path_cwd()

# Now, import the module
import math_operation

# Use functions from the module
result_add = math_operation.add(5, 3)
result_sub = math_operation.subtract(9, 4)
result_mul = math_operation.multiply(7, 2)

# Print results
print(f"Addition: {result_add}")
print(f"Subtraction: {result_sub}")
print(f"Multiplication: {result_mul}")


