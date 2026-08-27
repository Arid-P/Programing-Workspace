# Notes: Constructors, Methods, and self in Python OOP

# A class is a blueprint, and objects are created using that blueprint.
class Car:
    # Class variable (shared by all objects of this class)
    wheels = 4  # All cars generally have 4 wheels

    # Constructor (__init__ method)
    # - Automatically called when an object is created
    # - Used to initialize instance variables
    def __init__(self, brand: str, model: str, color: str):
        self.brand = brand  # Instance variable (specific to each object)
        self.model = model  # Instance variable
        self.color = color  # Instance variable

    # Instance method
    # - Works on the specific object of the class
    # - Requires 'self' as the first parameter
    def display_details(self) -> None:
        # Accessing instance variables using 'self'
        print(f"Car: {self.brand} {self.model}, Color: {self.color}")

    # Class method
    # - Operates on the class as a whole
    # - Uses the '@classmethod' decorator and 'cls' parameter
    @classmethod
    def change_wheel_count(cls, count: int) -> None:
        cls.wheels = count  # Modifies the class variable

    # Static method
    # - Does not operate on class or instance variables
    # - Uses the '@staticmethod' decorator
    @staticmethod
    def is_motor_vehicle() -> bool:
        return True  # Simply returns a boolean value


# Creating objects (instances of the class)
car1 = Car("Toyota", "Corolla", "Red")  # Calls the constructor (__init__)
car2 = Car("Honda", "Civic", "Blue")    # Calls the constructor (__init__)

# Using instance method
car1.display_details()  # Outputs: Car: Toyota Corolla, Color: Red
car2.display_details()  # Outputs: Car: Honda Civic, Color: Blue

# Accessing and modifying the class variable via class method
print(f"Default wheels: {Car.wheels}")  # Outputs: Default wheels: 4
Car.change_wheel_count(6)  # Updates the class variable
print(f"Updated wheels: {Car.wheels}")  # Outputs: Updated wheels: 6

# Using the static method
print(f"Is a car a motor vehicle? {Car.is_motor_vehicle()}")  # Outputs: True

# Key Points:
# 1. The 'self' parameter in instance methods allows access to object-specific data.
# 2. The constructor (__init__) initializes the object's instance variables.
# 3. Class methods modify or interact with class variables and require the 'cls' parameter.
# 4. Static methods are independent of the class and instance; they work like regular functions.