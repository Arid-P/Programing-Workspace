# Magic Methods

# 1. __str__(self)
# The __str__ method is called when you use print() or str() on an object.
# It should return a user-friendly string representation of the object.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"
        
p = Person("Alice", 30)
print(p)  # This calls p.__str__() and prints "Person(name=Alice, age=30)"

# 2. __repr__(self)
# The __repr__ method is called when you use repr() or in the interactive interpreter.
# It should return a string that ideally represents a valid Python expression.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

p = Person("Alice", 30)
print(repr(p))  # This calls p.__repr__() and prints "Person('Alice', 30)"

# 3. __eq__(self, other)
# This method is called when you use == to compare two objects.
# You can define how two objects of your class are compared.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        return False

p1 = Person("Alice", 30)
p2 = Person("Alice", 30)
print(p1 == p2)  # This calls p1.__eq__(p2), and returns True

# 4. __add__(self, other)
# This method is called when you use the + operator with objects of your class.
# It allows you to define how objects are added together.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2  # This calls p1.__add__(p2)
print(p3)  # This calls p3.__repr__() and prints "Point(4, 6)"

# 5. __len__(self)
# This method is called when you use len() on an object.
# It allows you to define how the length of an object is determined.

class CustomList:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

clist = CustomList([1, 2, 3, 4])
print(len(clist))  # This calls clist.__len__() and prints 4

# 6. __getitem__(self, key)
# This method allows you to define how indexing works for your objects.
# It's called when you use square brackets [] to access elements of an object.

class CustomList:
    def __init__(self, items):
        self.items = items

    def __getitem__(self, index):
        return self.items[index]

clist = CustomList([1, 2, 3, 4])
print(clist[2])  # This calls clist.__getitem__(2) and prints 3

# 7. __setitem__(self, key, value)
# This method allows you to define how assignment to indexed elements works for your objects.

class CustomList:
    def __init__(self, items):
        self.items = items

    def __setitem__(self, index, value):
        self.items[index] = value

clist = CustomList([1, 2, 3, 4])
clist[2] = 10  # This calls clist.__setitem__(2, 10)
print(clist.items)  # Output: [1, 2, 10, 4]

# 8. __del__(self)
# This method is called when an object is about to be destroyed (when its reference count drops to zero).
# It allows you to define cleanup actions before the object is deleted.

class Person:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"{self.name} is being deleted")

p = Person("Alice")
del p  # This calls p.__del__(), and prints "Alice is being deleted"