# Static Methods and Class Methods

# 1. Static Method
# A static method doesn't take `self` or `cls` as its first parameter.
# It behaves like a normal function but belongs to the class's namespace.

class MathOperations:
    @staticmethod
    def add(a: int, b: int) -> int:
        return a + b

    @staticmethod
    def subtract(a: int, b: int) -> int:
        return a - b

print(MathOperations.add(10, 20))  # Output: 30
print(MathOperations.subtract(30, 10))  # Output: 20

# Static methods are useful when the method does not need to access or modify class or instance attributes,
# but you want to logically group it within the class.

# 2. Class Method
# A class method takes `cls` as its first parameter, representing the class itself.
# It can modify class-level variables and can be called using the class name or an instance.

class MyClass:
    class_variable = 0

    @classmethod
    def increment(cls) -> None:
        cls.class_variable += 1

    @classmethod
    def get_class_variable(cls) -> int:
        return cls.class_variable

# Calling the class method using the class name
MyClass.increment()
print(MyClass.get_class_variable())  # Output: 1

# Calling the class method using an instance
obj = MyClass()
obj.increment()
print(obj.get_class_variable())  # Output: 2

# Difference between Static Method and Class Method:
# - Static Method: Does not take `self` or `cls` as arguments, doesn't access or modify instance or class attributes.
# - Class Method: Takes `cls` as an argument, can modify class-level attributes but does not modify instance attributes.

# 3. Practical Example of Class Method

class Employee:
    raise_percentage = 5  # Class variable

    def __init__(self, name: str, salary: float) -> None:
        self.name = name
        self.salary = salary

    def apply_raise(self) -> None:
        self.salary += self.salary * (self.raise_percentage / 100)

    @classmethod
    def set_raise_percentage(cls, percentage: float) -> None:
        cls.raise_percentage = percentage

    def display_info(self) -> None:
        print(f"{self.name}: {self.salary}")

# Create instances
e1 = Employee("John", 50000)
e2 = Employee("Jane", 60000)

# Applying raise based on the default raise percentage
e1.apply_raise()
e2.apply_raise()

e1.display_info()  # Output: John: 52500.0
e2.display_info()  # Output: Jane: 63000.0

# Change the class-level raise percentage using class method
Employee.set_raise_percentage(10)

# Apply the new raise percentage
e1.apply_raise()
e2.apply_raise()

e1.display_info()  # Output: John: 57750.0
e2.display_info()  # Output: Jane: 69300.0