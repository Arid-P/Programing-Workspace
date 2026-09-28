# Notes: Inheritance in Python OOP

# Inheritance allows a child class to inherit attributes and methods from a parent class.
# This promotes code reuse and hierarchical class structures.

# Example: Single Inheritance
class Animal:
    def __init__(self, name: str):
        self.name = name  # Instance variable

    def speak(self) -> None:
        # Base class method
        print(f"{self.name} makes a sound.")

# Dog is a child class of Animal
class Dog(Animal):
    def speak(self) -> None:
        # Overriding the parent method
        print(f"{self.name} barks.")

# Creating objects
animal = Animal("Generic Animal")
dog = Dog("Buddy")

# Calling methods
animal.speak()  # Outputs: Generic Animal makes a sound.
dog.speak()     # Outputs: Buddy barks.


# Example: Multiple Inheritance
class Father:
    def profession(self) -> None:
        print("Father is an Engineer.")

class Mother:
    def hobby(self) -> None:
        print("Mother loves painting.")

# Child inherits from both Father and Mother
class Child(Father, Mother):
    def introduce(self) -> None:
        print("I am their child.")

# Creating object of Child
child = Child()
child.profession()  # Outputs: Father is an Engineer.
child.hobby()       # Outputs: Mother loves painting.
child.introduce()   # Outputs: I am their child.


# Example: Multilevel Inheritance
class Vehicle:
    def start(self) -> None:
        print("Vehicle is starting.")

class Car(Vehicle):
    def drive(self) -> None:
        print("Car is driving.")

class ElectricCar(Car):
    def charge(self) -> None:
        print("Electric car is charging.")

# Creating an object of ElectricCar
tesla = ElectricCar()
tesla.start()  # Outputs: Vehicle is starting.
tesla.drive()  # Outputs: Car is driving.
tesla.charge()  # Outputs: Electric car is charging.


# Example: Hierarchical Inheritance
class Shape:
    def display(self) -> None:
        print("This is a shape.")

class Circle(Shape):
    def area(self, radius: float) -> float:
        return 3.14 * radius * radius

class Rectangle(Shape):
    def area(self, length: float, width: float) -> float:
        return length * width

# Creating objects
circle = Circle()
rectangle = Rectangle()
circle.display()             # Outputs: This is a shape.
print(circle.area(5))        # Outputs: 78.5
print(rectangle.area(4, 6))  # Outputs: 24


# Key Concepts:
# 1. **Method Overriding**:
#    - A child class can redefine a parent class's method for its specific needs.
#    - Example: `speak` method in `Dog` class overrides `speak` in `Animal`.

# 2. **super()**:
#    - Used to call a parent class method in the child class.
class Cat(Animal):
    def speak(self) -> None:
        super().speak()  # Calls parent class's speak method
        print(f"{self.name} meows.")

cat = Cat("Whiskers")
cat.speak()
# Outputs:
# Generic Animal makes a sound.
# Whiskers meows.

# 3. **isinstance() and issubclass()**:
#    - `isinstance(object, class)` checks if an object is an instance of a class.
#    - `issubclass(child, parent)` checks if a class is a subclass of another class.
print(isinstance(dog, Animal))  # Outputs: True
print(issubclass(Dog, Animal))  # Outputs: True