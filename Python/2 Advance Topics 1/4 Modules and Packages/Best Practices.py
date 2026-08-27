# Best Practices for Creating Python Modules and Packages

# 1. Organize Code into Small, Reusable Modules
# - Keep modules small and focused on a single task.
# - Each module should ideally contain related functions, classes, or constants.
# - Aim for high cohesion and low coupling. Related functionality should be grouped together,
#   and a module should have minimal dependencies on other modules.

# 2. Follow Naming Conventions
# - Use descriptive and consistent names for your modules and packages.
# - Module names should be lowercase and can use underscores for readability.
# - Avoid using the names of standard Python libraries to prevent conflicts.

# Example:
# Correct naming: my_module.py, utils.py
# Incorrect naming: math.py (as 'math' is a standard library name)

# 3. Use `__init__.py` Properly in Packages
# - If creating a package (a directory containing multiple modules), include an __init__.py file.
# - The __init__.py file can be left empty, or it can be used to initialize the package, 
#   define variables, or import specific functions/classes from modules in the package.

# Example:
# In __init__.py:
# from .module1 import function1
# from .module2 import function2

# 4. Avoid Circular Imports
# - Circular imports happen when two or more modules depend on each other.
# - This can cause import errors and make code harder to maintain.
# - Structure your code to avoid circular dependencies, and use lazy imports (importing modules inside functions)
#   if necessary to avoid import errors.

# 5. Documentation: Use Docstrings for Functions and Classes
# - Provide clear documentation for your functions, classes, and modules using docstrings.
# - Docstrings should describe the purpose, parameters, and return values of a function or class.

# Example:
def add(a: int, b: int) -> int:
    """
    Add two numbers together.

    Parameters:
    a (int): First number.
    b (int): Second number.

    Returns:
    int: Sum of the two numbers.
    """
    return a + b

# 6. Keep Package Structure Consistent
# - A well-structured package improves maintainability and readability.
# - The basic structure of a package could look like this:
# my_package/
#     __init__.py
#     module1.py
#     module2.py
#     utils.py
#     tests/
#         test_module1.py
#         test_module2.py

# 7. Avoid Using `*` for Imports
# - It is best to avoid using `from module import *` as it can pollute the namespace and cause confusion.
# - Use explicit imports to make it clear where a particular function or class comes from.

# Example:
# Bad: from math_operations import *
# Good: from math_operations import add, subtract

# 8. Maintain Compatibility Across Python Versions
# - Ensure your code works across different versions of Python, especially if you're working in an environment with multiple versions.
# - If necessary, use tools like 'six' or 'future' to maintain compatibility between versions.

# 9. Testing Modules: Write Unit Tests for Your Code
# - Each module should be tested thoroughly. Write tests for your module functions using Python's unittest or pytest.
# - This ensures that your code works as expected and avoids regression errors.

# Example:
import unittest
from math_operations import add, subtract

class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
    
    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)

if __name__ == '__main__':
    unittest.main()

# 10. Version Control: Use Git for Code Management
# - Use version control (e.g., Git) to track changes in your code.
# - Git allows for collaboration, reverting to previous versions, and managing releases.

# 11. Keep Dependencies to a Minimum
# - Avoid unnecessary external dependencies in your modules or packages.
# - If your package depends on external libraries, document them in a requirements.txt file.

# Example:
# requests==2.25.1

# 12. Use `setup.py` for Distribution
# - If you're planning to distribute your package, create a setup.py file.
# - This file contains metadata for your package, like name, version, and dependencies.

# Example setup.py:
from setuptools import setup, find_packages

setup(
    name='my_package',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',  # Example external dependency
    ],
)

# Summary of Best Practices:
# - Organize code logically in small, reusable modules.
# - Name modules and packages consistently and descriptively.
# - Use `__init__.py` to define the package’s interface.
# - Avoid circular imports; use lazy imports if needed.
# - Document code with clear docstrings.
# - Keep the package structure consistent.
# - Use explicit imports instead of `import *`.
# - Write tests to ensure your modules are working correctly.
# - Track changes with version control (e.g., Git).
# - Minimize dependencies and keep them well-documented.