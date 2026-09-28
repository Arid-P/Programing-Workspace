class Car:
    def __init__(self, model: str, daily_price: float):
        self.model = model
        self.daily_price = daily_price
        self.is_rented = False  # Initially, the car is available
    
    def rent(self):
        """Marks the car as rented."""
        self.is_rented = True

    def return_car(self):
        """Marks the car as available."""
        self.is_rented = False

    def is_available(self) -> bool:
        """Returns whether the car is available for rent."""
        return not self.is_rented
    
    def __str__(self):
        """Returns a string representation of the car."""
        availability = "Available" if not self.is_rented else "Rented"
        return f"Model: {self.model}, Daily Price: {self.daily_price}, Status: {availability}"


class Customer:
    def __init__(self, name: str, contact: str):
        self.name = name
        self.contact = contact
        self.rented_car = None
        self.rental_days = 0
    
    def rent_car(self, car: Car, days: int):
        """Rents a car to the customer for a given number of days."""
        if car.is_available():
            self.rented_car = car
            self.rental_days = days
            car.rent()
            print(f"{self.name} has rented {car.model} for {days} days.")
        else:
            print(f"Sorry, {car.model} is currently rented out.")
    
    def return_car(self):
        """Returns the rented car."""
        if self.rented_car:
            total_cost = self.rented_car.daily_price * self.rental_days
            print(f"Total rental cost for {self.rented_car.model} is: {total_cost}")
            self.rented_car.return_car()
            self.rented_car = None
            self.rental_days = 0
        else:
            print(f"{self.name} has no car to return.")
    
    def __str__(self):
        return f"Customer: {self.name}, Contact: {self.contact}"


class RentalSystem:
    def __init__(self):
        self.cars = []
        self.customers = []
    
    def add_car(self, car: Car):
        """Adds a car to the rental system."""
        self.cars.append(car)
    
    def add_customer(self, customer: Customer):
        """Adds a customer to the rental system."""
        self.customers.append(customer)
    
    def display_available_cars(self):
        """Displays all available cars."""
        print("Available cars:")
        for car in self.cars:
            if car.is_available():
                print(car)


# Main function to simulate the rental system
def main():
    # Create rental system
    rental_system = RentalSystem()
    
    # Add cars to the system
    car1 = Car("Toyota Corolla", 50)
    car2 = Car("Honda Civic", 60)
    car3 = Car("Ford Mustang", 100)
    rental_system.add_car(car1)
    rental_system.add_car(car2)
    rental_system.add_car(car3)

    # Add customers to the system
    customer1 = Customer("John Doe", "123-456-7890")
    customer2 = Customer("Jane Smith", "987-654-3210")
    rental_system.add_customer(customer1)
    rental_system.add_customer(customer2)

    # Display available cars
    rental_system.display_available_cars()

    # Customer rents a car
    customer1.rent_car(car1, 3)  # John rents Toyota Corolla for 3 days
    rental_system.display_available_cars()

    # Customer returns the car
    customer1.return_car()
    rental_system.display_available_cars()


if __name__ == "__main__":
    main()