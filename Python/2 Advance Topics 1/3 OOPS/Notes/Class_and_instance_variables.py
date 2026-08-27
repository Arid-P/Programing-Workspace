# In Python, class variables are shared by all instances of a class, while instance variables are unique to each instance.

class Car:
    # Class variable shared by all instances
    wheels = 4

    def __init__(self, make: str, model: str) -> None:
        # Instance variables unique to each instance
        self.make = make
        self.model = model

    def display_info(self) -> None:
        # Method accessing both class and instance variables
        print(f"Make: {self.make}, Model: {self.model}, Wheels: {self.wheels}")

# Creating two car instances with different make and model
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

# Accessing class variable using the class name
print(f"Class variable wheels: {Car.wheels}")

# Accessing class variable through instances
print(f"Car1 wheels: {car1.wheels}, Car2 wheels: {car2.wheels}")

# Changing class variable, which affects all instances
Car.wheels = 6
print(f"After changing the class variable, car1 wheels: {car1.wheels}, car2 wheels: {car2.wheels}")

# Accessing instance variables
car1.display_info()  # Make: Toyota, Model: Corolla, Wheels: 6
car2.display_info()  # Make: Honda, Model: Civic, Wheels: 6