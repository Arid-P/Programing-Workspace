# Encapsulation is the bundling of data and methods that work on that data into a single unit (class).
# It also restricts direct access to some of the object's attributes to protect its state.

# Example of Public Attributes and Methods
class Car:
    def __init__(self, brand: str) -> None:
        self.brand = brand  # public attribute

    def show_brand(self) -> None:  # public method
        print(f"Car brand: {self.brand}")

car = Car("Toyota")
car.show_brand()  # Outputs: Car brand: Toyota
print(car.brand)   # Outputs: Toyota

# Example of Private Attributes and Methods
class Car:
    def __init__(self, brand: str, model: str) -> None:
        self.__brand = brand  # private attribute
        self.__model = model  # private attribute

    def __show_model(self) -> None:  # private method
        print(f"Car model: {self.__model}")

    def display_info(self) -> None:
        print(f"Car brand: {self.__brand}")
        self.__show_model()

car = Car("Toyota", "Corolla")
car.display_info()  # Outputs: Car brand: Toyota, Car model: Corolla

# Example of Protected Attributes and Methods
class Car:
    def __init__(self, brand: str, model: str) -> None:
        self._brand = brand  # protected attribute
        self._model = model  # protected attribute

    def _show_info(self) -> None:  # protected method
        print(f"Car brand: {self._brand}, Model: {self._model}")

car = Car("Toyota", "Corolla")
car._show_info()  # Outputs: Car brand: Toyota, Model: Corolla
print(car._brand)  # Outputs: Toyota

# Example of Getter and Setter Methods
class Car:
    def __init__(self, brand: str) -> None:
        self.__brand = brand  # private attribute

    # Getter method for brand
    def get_brand(self) -> str:
        return self.__brand

    # Setter method for brand
    def set_brand(self, brand: str) -> None:
        if len(brand) > 0:
            self.__brand = brand
        else:
            print("Brand name cannot be empty")

car = Car("Toyota")
print(car.get_brand())  # Outputs: Toyota

car.set_brand("Honda")
print(car.get_brand())  # Outputs: Honda

car.set_brand("")  # Outputs: Brand name cannot be empty