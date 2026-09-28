# Notes on Composition vs Inheritance

# Inheritance: "is-a" relationship
# Example of Inheritance:
class Vehicle:
    """A base class representing a vehicle."""
    def move(self) -> None:
        print("This vehicle can move")

class Car(Vehicle):
    """A Car 'is-a' Vehicle."""
    def wheels(self) -> None:
        print("This car has 4 wheels")

# Using inheritance
car = Car()
car.move()  # Inherited method from Vehicle
car.wheels()  # Defined in Car

# ----------------------------------------------------

# Composition: "has-a" relationship
# Example 1: A Car "has-a" Engine
class Engine:
    """A class representing an engine."""
    def start(self) -> None:
        print("Engine starts")

class Car:
    """A Car 'has-a' Engine."""
    def __init__(self) -> None:
        self.engine = Engine()  # Engine is a part of Car

    def start_engine(self) -> None:
        self.engine.start()  # Delegating behavior to Engine

# Using composition
car = Car()
car.start_engine()  # Calls Engine's method

# ----------------------------------------------------

# Example 2: A Library "has-a" Collection of Books
class Book:
    """A class representing a book."""
    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author

    def display_info(self) -> None:
        print(f"Title: {self.title}, Author: {self.author}")

class Library:
    """A Library 'has-a' Collection of Books."""
    def __init__(self) -> None:
        self.books = []  # List of books

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def show_books(self) -> None:
        for book in self.books:
            book.display_info()

# Using composition
library = Library()
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")

library.add_book(book1)
library.add_book(book2)
library.show_books()  # Displays info for all books in the library

# ----------------------------------------------------

# Example 3: A Team "has-a" Collection of Players
class Player:
    """A class representing a player."""
    def __init__(self, name: str, position: str) -> None:
        self.name = name
        self.position = position

    def display(self) -> None:
        print(f"Player: {self.name}, Position: {self.position}")

class Team:
    """A Team 'has-a' Collection of Players."""
    def __init__(self, team_name: str) -> None:
        self.team_name = team_name
        self.players = []  # List of players

    def add_player(self, player: Player) -> None:
        self.players.append(player)

    def show_team(self) -> None:
        print(f"Team: {self.team_name}")
        for player in self.players:
            player.display()

# Using composition
team = Team("The Avengers")
player1 = Player("Tony", "Captain")
player2 = Player("Steve", "Leader")

team.add_player(player1)
team.add_player(player2)
team.show_team()  # Displays all players in the team# Notes on Composition vs Inheritance

# Inheritance: "is-a" relationship
# Example of Inheritance:
class Vehicle:
    """A base class representing a vehicle."""
    def move(self) -> None:
        print("This vehicle can move")

class Car(Vehicle):
    """A Car 'is-a' Vehicle."""
    def wheels(self) -> None:
        print("This car has 4 wheels")

# Using inheritance
car = Car()
car.move()  # Inherited method from Vehicle
car.wheels()  # Defined in Car

# ----------------------------------------------------

# Composition: "has-a" relationship
# Example 1: A Car "has-a" Engine
class Engine:
    """A class representing an engine."""
    def start(self) -> None:
        print("Engine starts")

class Car:
    """A Car 'has-a' Engine."""
    def __init__(self) -> None:
        self.engine = Engine()  # Engine is a part of Car

    def start_engine(self) -> None:
        self.engine.start()  # Delegating behavior to Engine

# Using composition
car = Car()
car.start_engine()  # Calls Engine's method

# ----------------------------------------------------

# Example 2: A Library "has-a" Collection of Books
class Book:
    """A class representing a book."""
    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author

    def display_info(self) -> None:
        print(f"Title: {self.title}, Author: {self.author}")

class Library:
    """A Library 'has-a' Collection of Books."""
    def __init__(self) -> None:
        self.books = []  # List of books

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def show_books(self) -> None:
        for book in self.books:
            book.display_info()

# Using composition
library = Library()
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")

library.add_book(book1)
library.add_book(book2)
library.show_books()  # Displays info for all books in the library

# ----------------------------------------------------

# Example 3: A Team "has-a" Collection of Players
class Player:
    """A class representing a player."""
    def __init__(self, name: str, position: str) -> None:
        self.name = name
        self.position = position

    def display(self) -> None:
        print(f"Player: {self.name}, Position: {self.position}")

class Team:
    """A Team 'has-a' Collection of Players."""
    def __init__(self, team_name: str) -> None:
        self.team_name = team_name
        self.players = []  # List of players

    def add_player(self, player: Player) -> None:
        self.players.append(player)

    def show_team(self) -> None:
        print(f"Team: {self.team_name}")
        for player in self.players:
            player.display()

# Using composition
team = Team("The Avengers")
player1 = Player("Tony", "Captain")
player2 = Player("Steve", "Leader")

team.add_player(player1)
team.add_player(player2)
team.show_team()  # Displays all players in the team