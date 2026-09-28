# In Python, method overloading is not directly supported, but we can simulate it using default arguments or *args and **kwargs.

class Printer:
    def print_message(self, message: str, times: int = 1) -> None:
        """Simulated method overloading using default arguments."""
        for _ in range(times):
            print(message)

# Creating an object
printer = Printer()

# Calling method with one argument (default `times=1`)
printer.print_message("Hello, World!")

# Calling method with two arguments (message, times)
printer.print_message("Hello, World!", 3)

# Method overriding example
class Animal:
    def speak(self) -> None:
        """Base method to be overridden"""
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self) -> None:
        """Overriding the speak method"""
        print("Dog barks")

class Cat(Animal):
    def speak(self) -> None:
        """Overriding the speak method"""
        print("Cat meows")

# Create instances of Dog and Cat
dog = Dog()
cat = Cat()

# Calling overridden methods
dog.speak()  # Dog barks
cat.speak()  # Cat meows