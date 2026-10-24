# 📝 **Typing Module in Python**
# The `typing` module provides support for type hints in Python, allowing us to specify 
# expected data types for function parameters, return values, and variables.

# ✅ **1. Basic Type Hints**
# We can specify basic types like int, float, str, and bool.

from typing import Any

def add(x: int, y: int) -> int:
    """Adds two integers and returns an integer."""
    return x + y

def greet(name: str) -> str:
    """Returns a greeting message."""
    return f"Hello, {name}!"

# ✅ **2. Using `Any` for Flexible Typing**
# The `Any` type allows a variable to accept any data type.

def flexible_function(value: Any) -> Any:
    """Accepts any type and returns the same value."""
    return value

# ✅ **3. Type Aliases**
# We can create type aliases for better readability.

from typing import Tuple

Coordinates = Tuple[float, float]  # Alias for latitude and longitude

def get_location() -> Coordinates:
    """Returns latitude and longitude as a tuple."""
    return (27.1751, 78.0421)

# ✅ **4. Lists, Tuples, and Dictionaries**
# The `List`, `Tuple`, and `Dict` types allow specifying element types.

from typing import List, Dict

def process_numbers(numbers: List[int]) -> List[int]:
    """Doubles each number in a list and returns a new list."""
    return [num * 2 for num in numbers]

def student_scores() -> Dict[str, float]:
    """Returns a dictionary of student names and their scores."""
    return {"Alice": 85.5, "Bob": 92.0}

# ✅ **5. Optional Types**
# Use `Optional` when a parameter can be `None`.

from typing import Optional

def find_user(username: str) -> Optional[str]:
    """Returns the username if found, otherwise None."""
    users = ["Alice", "Bob", "Charlie"]
    return username if username in users else None

# ✅ **6. Union for Multiple Possible Types**
# Use `Union` when a variable or return value can be of different types.

from typing import Union

def square_or_message(value: Union[int, str]) -> Union[int, str]:
    """Returns square of number or an error message if input is not an integer."""
    if isinstance(value, int):
        return value ** 2
    return "Invalid input"

# ✅ **7. Callable for Function Signatures**
# `Callable` is used to define functions with specific input and output types.

from typing import Callable

def apply_operation(x: int, y: int, operation: Callable[[int, int], int]) -> int:
    """Applies a function (e.g., addition, multiplication) to two numbers."""
    return operation(x, y)

def multiply(a: int, b: int) -> int:
    return a * b

result = apply_operation(3, 4, multiply)  # Output: 12

# ✅ **8. TypeVar for Generic Functions**
# `TypeVar` allows defining functions that work with different types.

from typing import TypeVar

T = TypeVar("T")  # Generic Type Variable

def reverse_list(items: List[T]) -> List[T]:
    """Reverses a list of any type."""
    return items[::-1]

reversed_nums = reverse_list([1, 2, 3, 4])  # Output: [4, 3, 2, 1]
reversed_strings = reverse_list(["A", "B", "C"])  # Output: ["C", "B", "A"]

# ✅ **9. Literal for Specific Values**
# `Literal` is used when a variable should accept only specific values.

from typing import Literal

def set_mode(mode: Literal["auto", "manual", "off"]) -> str:
    """Sets the mode with only specific values."""
    return f"Mode set to {mode}"

mode1 = set_mode("auto")  # ✅ Valid
# mode2 = set_mode("fast")  # ❌ Type error

# ✅ **10. New Style Type Hinting (PEP 585)**
# In Python 3.9+, we can use built-in types instead of `List`, `Dict`, etc.

def numbers_list(nums: list[int]) -> list[int]:
    """Doubles numbers in a list using new-style hinting."""
    return [num * 2 for num in nums]

def student_data() -> dict[str, float]:
    """Returns student scores using new-style hinting."""
    return {"Alice": 90.0, "Bob": 88.5}

# ✅ **11. Self Type for OOP**
# `Self` is used in method return types to indicate the current instance.

from typing import Self

class Counter:
    def __init__(self, count: int = 0) -> None:
        self.count = count
    
    def increment(self) -> Self:
        """Increments the counter and returns self."""
        self.count += 1
        return self

counter = Counter().increment().increment()
print(counter.count)  # Output: 2