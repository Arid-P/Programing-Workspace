from collections import namedtuple


# Defining a namedtuple
Point = namedtuple('Point', ['x', 'y'])

# Creating an instance of Point
p = Point(3, 4)
print(f"Point coordinates: {p.x}, {p.y}")

# Namedtuple fields can be accessed like attributes
print(f"Point x-coordinate: {p.x}")
print(f"Point y-coordinate: {p.y}")

# Converting namedtuple to a dictionary
point_dict = p._asdict()  # Returns an OrderedDict
print("Namedtuple as dictionary:", point_dict)

# Unpacking a namedtuple
x, y = p
print(f"Unpacked values: x={x}, y={y}")


#another example
# Defining a namedtuple with more fields
Car = namedtuple('Car', ['make', 'model', 'year', 'price'])

# Creating an instance of Car
car1 = Car(make='Toyota', model='Corolla', year=2022, price=25000)


# Accessing fields by name
print(f"Car make: {car1.make}")
print(f"Car model: {car1.model}")
print(f"Car year: {car1.year}")
print(f"Car price: ${car1.price}")


# Accessing the field names
print(f"Fields in Car: {car1._fields}")


# Accessing fields using indexing
print(f"First field (make): {car1[0]}")
print(f"Second field (model): {car1[1]}")


# Creating a modified copy of the namedtuple
car2 = car1._replace(price=24000)

# Displaying original and modified cars
print(f"Original Car price: ${car1.price}")
print(f"Modified Car price: ${car2.price}")


# Unpacking a namedtuple with multiple fields
make, model, year, price = car1

# Displaying the unpacked values
print(f"Make: {make}, Model: {model}, Year: {year}, Price: ${price}")