class Book () :
    def __init__ (self, details: list) :
        # details = [title, author, genre]
        self.title = details[0]
        self.author = details[1]
        self.genre = details[2]
        self.availabilty = True
    
    def borrow (self) :
        self.availabilty = False
        print(f"You have successfully borrowed {self.title} \n")
    
    def returned (self) :
        self.availabilty = True
        print(f"You have successfully returned {self.title} \n")
    
    def is_available (self) -> bool :
        return self.availabilty


class Student () : 
    max_books: int = 5

    def __init__ (self, name, contact) :
        self.name = name
        self.contact = contact
        self.current_books_borrowed: int = 0
        self.books_borrowed: list = []
    
    def borrow_book (self, book) :
        if book.is_available() and len(self.books_borrowed) < self.max_books:
            self.current_books_borrowed += 1
            self.books_borrowed.append(book)
            book.borrow()
        elif len(self.books_borrowed) == self.max_books :
            print("your limit of 5 books has been reached so you cannot borrow {book.title} \n")
        else :
            print(f"{book.title} has been already borrowed \n")
    
    def return_book (self, book) :
        if not book.is_available() :
            self.current_books_borrowed -= 1
            self.books_borrowed.remove(book)
            book.returned()
        else :
            print(f"{book.title} has not been borrowed yet \n")
    


class Teacher () : 
    max_books = 10

    def __init__ (self, name, contact) :
        self.name = name
        self.contact = contact
        self.current_books_borrowed: int = 0
        self.books_borrowed: list = []
        
    
    def borrow_book (self, book) :
        if book.is_available() and len(self.books_borrowed) < self.max_books:
            self.current_books_borrowed += 1
            self.books_borrowed.append(book)
            book.borrow()
        elif len(self.books_borrowed) == self.max_books :
            print("your limit of 5 books has been reached \n")
        else :
            print(f"{book.title} has been already borrowed \n")
    
    def return_book (self, book) :
        if not book.is_available() :
            self.current_books_borrowed -= 1
            self.books_borrowed.remove(book)
            book.returned()
        else :
            print(f"{book.title} has not been borrowed yet \n")


def main () -> None :
    #raise ValueError('main not implemented')
    
    books = [
    Book(["Python Programming", "John Doe", "Education"]),
    Book(["Learn Data Science", "Jane Smith", "Education"]),
    Book(["AI and Machine Learning", "Alan Turing", "Technology"]),
    Book(["The Great Gatsby", "F. Scott Fitzgerald", "Novel"]),
    Book(["1984", "George Orwell", "Dystopian"]),
    Book(["Harry Potter and the Sorcerer's Stone", "J.K. Rowling", "Fantasy"]),
    Book(["The Catcher in the Rye", "J.D. Salinger", "Novel"]),
    Book(["Moby Dick", "Herman Melville", "Adventure"]),
    Book(["To Kill a Mockingbird", "Harper Lee", "Fiction"]),
    Book(["The Hobbit", "J.R.R. Tolkien", "Fantasy"]),
    Book(["Chemistry by Pw", "Physics Wallah", "Education"])
        ]

    jayesh = Student("Jayesh", 999-555-323)
    akash = Teacher("Akash", 888-666-224)
    
    for i in range(5) :
        jayesh.borrow_book(books[i])
    
    for i in range(3, 5) :
        jayesh.return_book(books[i])
    
    
    for i in range(2, 9, 2) :
        akash.borrow_book(books[i])
    
    
    return

if __name__ == "__main__" :
    main()