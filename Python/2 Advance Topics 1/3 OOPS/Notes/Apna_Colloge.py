# Object-Oriented Programming (OOP) Concepts
# Notes on the topics from Apna College Python OOP 2 videos

# 1. Object-Oriented Programming (OOP) Introduction
# OOP is a programming paradigm that organizes code into classes and objects.
# It allows for code reuse, modularity, and easier maintenance.

# Classes and Objects
# - A class is like a blueprint for creating objects.
# - An object is an instance of a class.
# Example:
class Car:
    # Constructor
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model
    
    def display_info(self) -> None:
        print(f"Car brand: {self.brand}, Model: {self.model}")

# Create an object (instance) of Car class
car1 = Car("Toyota", "Camry")
car1.display_info()  # Output: Car brand: Toyota, Model: Camry

# 2. Constructors (__init__), Methods, and Self
# The __init__() method is a special method (constructor) called when an object is created.
# 'self' refers to the current instance of the class, used to access its attributes and methods.

# Example of a constructor and methods:
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greet(self) -> None:
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating an object
person1 = Person("Alice", 30)
person1.greet()  # Output: Hello, my name is Alice and I am 30 years old.

# 3. Inheritance, Polymorphism, Encapsulation, Abstraction (Intro Level)
# - Inheritance: A mechanism where a new class inherits attributes and methods from an existing class.
# - Polymorphism: The ability of different classes to define methods with the same name, but with different behaviors.
# - Encapsulation: The concept of restricting access to certain details of an object's implementation.
# - Abstraction: The concept of hiding the complex implementation and showing only the necessary details.

# Inheritance Example:
class Animal:
    def speak(self) -> None:
        print("Animal speaks")

class Dog(Animal):
    def speak(self) -> None:
        print("Dog barks")

# Creating objects
animal = Animal()
dog = Dog()

animal.speak()  # Output: Animal speaks
dog.speak()     # Output: Dog barks

# Polymorphism Example:
# Same method name 'speak' in both Animal and Dog class, but different behaviors.

# Encapsulation Example (Private Attributes):
class BankAccount:
    def __init__(self, balance: float):
        self.__balance = balance  # Private attribute

    def deposit(self, amount: float) -> None:
        self.__balance += amount

    def get_balance(self) -> float:
        return self.__balance

# Creating an object and accessing methods
account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500
# The private attribute __balance is not directly accessible from outside the class.

# Abstraction Example (Abstract Classes):
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return 3.14 * self.radius * self.radius

# Creating an object of Circle class
circle = Circle(5)
print(circle.area())  # Output: 78.5