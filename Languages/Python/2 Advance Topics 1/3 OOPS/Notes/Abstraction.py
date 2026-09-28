# Abstraction in Python is achieved through abstract classes and abstract methods.
# An abstract class cannot be instantiated directly.
# Abstract methods do not have implementations in the abstract class and must be implemented by subclasses.

from abc import ABC, abstractmethod

# Abstract class Animal
class Animal(ABC):
    @abstractmethod
    def sound(self) -> None:
        pass

    @abstractmethod
    def move(self) -> None:
        pass

# Subclass Dog implementing abstract methods
class Dog(Animal):
    def sound(self) -> None:
        print("Bark")

    def move(self) -> None:
        print("Run")

# Subclass Cat implementing abstract methods
class Cat(Animal):
    def sound(self) -> None:
        print("Meow")

    def move(self) -> None:
        print("Walk")

# Creating objects of the subclasses
dog = Dog()
dog.sound()  # Outputs: Bark
dog.move()   # Outputs: Run

cat = Cat()
cat.sound()  # Outputs: Meowq
cat.move()   # Outputs: Walk

# We cannot instantiate the abstract class Animal directly.
# animal = Animal()  # TypeError: Can't instantiate abstract class Animal with abstract methods sound, move
print('hello')