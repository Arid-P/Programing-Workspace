# Notes: Polymorphism in Python OOP
from abc import ABC, abstractmethod #for line 55

# Polymorphism allows different objects to use the same interface or method name with unique implementations.

# Example: Method Overriding
class Animal:
    def speak(self) -> None:
        print("Animal makes a sound.")

class Dog(Animal):
    def speak(self) -> None:
        # Overriding the parent class method
        print("Dog barks.")

class Cat(Animal):
    def speak(self) -> None:
        print("Cat meows.")

# Using a single interface (speak) for different objects
animals = [Dog(), Cat()]
for animal in animals:
    animal.speak()


# Example: Method Overloading (Simulated in Python)
class Calculator:
    def add(self, a: int, b: int, c: int = 0) -> int:
        # Method with optional third argument
        return a + b + c

calc = Calculator()
print(calc.add(10, 20))       # Outputs: 30
print(calc.add(10, 20, 30))   # Outputs: 60


# Example: Duck Typing
class Bird:
    def fly(self) -> None:
        print("Bird is flying.")

class Airplane:
    def fly(self) -> None:
        print("Airplane is flying.")

# Duck typing example
def lift_off(entity: object) -> None:
    # No need to check the type of the object
    entity.fly()

lift_off(Bird())      # Outputs: Bird is flying.
lift_off(Airplane())  # Outputs: Airplane is flying.


# Example: Abstract Classes for Polymorphism
#line 2

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return 3.14 * self.radius * self.radius

    def perimeter(self) -> float:
        return 2 * 3.14 * self.radius

class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self) -> float:
        return self.length * self.width

    def perimeter(self) -> float:
        return 2 * (self.length + self.width)

# Using polymorphism
shapes = [Circle(5), Rectangle(4, 6)]
for shape in shapes:
    print(f"Area: {shape.area()}, Perimeter: {shape.perimeter()}")