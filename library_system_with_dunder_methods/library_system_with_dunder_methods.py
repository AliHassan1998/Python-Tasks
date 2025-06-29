# Library System using Magic/Dunder Methods
import re


class Book:
    total_books = 0
    all_books = []

    def __init__(self, title, author, isbn, pages):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.pages = pages
        if Book.is_valid_isbn(self.isbn):
            Book.total_books += 1
            Book.all_books.append(self)
        else:
            raise ValueError(f"Invalid ISBN format: {isbn}")

    @staticmethod
    def is_valid_isbn(isbn):
        pattern = r"^\d{3}-\d{10}$"
        if re.fullmatch(pattern, isbn):
            return True
        else:
            return False

    def __str__(self):
        return f"Book: {self.title} by {self.author}."

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', '{self.isbn}', '{self.pages}')"

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.isbn == other.isbn
        return NotImplemented

    def __len__(self):
        return self.pages

    @classmethod
    def from_string(cls, string):
        title, author, isbn, pages = string.strip().split(",")
        return cls(title, author, isbn, int(pages))

    @classmethod
    def display_all_books(cls):
        if cls.all_books:
            print("All books are: ")
            print("--" * 30)
            for no, book in enumerate(cls.all_books, start=1):
                print(f"Book {no}: ")
                print(book)
                print("--" * 30)
        else:
            print("Oops! There are no books to show.")


class Member:
    total_members = 0
    all_members = []

    def __init__(self, name, email, borrowed_books=None):
        self.name = name
        if Member.is_valid_email(email):
            self.email = email
        else:
            raise ValueError(f"Invalid Email: {email}.")
        if borrowed_books is None:
            borrowed_books = []
        self.borrowed_books = borrowed_books
        Member.total_members += 1
        Member.all_members.append(self)

    @staticmethod
    def is_valid_email(email):
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if re.fullmatch(pattern, email):
            return True
        else:
            return False

    def borrow_book(self, book):
        if book in Book.all_books:
            self.borrowed_books.append(book)
            Book.all_books.remove(book)
            print("The book has been successfully borrowed.")
        else:
            print(f"Oops! The required book is not available.")

    def __str__(self):
        return f"Member: {self.name} has borrowed {len(self)} books."

    def __len__(self):
        return len(self.borrowed_books)

    def __contains__(self, book):
        return book in self.borrowed_books

    @classmethod
    def from_string(cls, string):
        name, email = string.strip().split(",")
        return cls(name, email)

    @classmethod
    def display_all_members_details(cls):
        if cls.all_members:
            print("All Members are: ")
            print("--" * 30)
            for no, member in enumerate(cls.all_members, start=1):
                print(f"Member {no}: ")
                print(member)
                print("--" * 30)
        else:
            print(f"Oops! There are no members to show.")


class Librarian(Member):
    all_librarians = []
    total_librarians = 0

    def __init__(self, name, email, employee_id, borrowed_books=None):
        super().__init__(name, email, borrowed_books)
        self.employee_id = employee_id
        Librarian.total_librarians += 1
        Librarian.all_librarians.append(self)

    def __str__(self):
        return f"Librarian: {self.name} (ID: {self.employee_id}) has borrowed {len(self)} books."

    @classmethod
    def from_string(cls, string):
        name, email, employee_id = string.strip().split(",")
        return cls(name, email, employee_id)

    @classmethod
    def display_all_librarians_details(cls):
        if cls.all_librarians:
            print("All Librarians are: ")
            print("--" * 30)
            for no, librarian in enumerate(cls.all_librarians, start=1):
                print(f"Librarian {no}: ")
                print(librarian)
                print("--" * 30)
        else:
            print(f"Oops! There are no librarians to show.")


if __name__ == "__main__":
    book1 = Book("1984", "George Orwell",  "123-1234567890", 328)
    book2 = Book("Brave New World", "Aldous Huxley", "123-0987654321", 311)
    print(f"Total books are: {Book.total_books}")
    Book.display_all_books()
    print(book1)
    print(repr(book1))
    print(book1 == book2)
    print(len(book1))
    member1 = Member("Ali", "ali@gmail.com")
    print(f"Total members are: {Member.total_members}")
    member1.borrow_book(book1)
    print(member1)
    print(len(member1))
    print(book1 in member1)
    print(book2 in member1)
    Member.display_all_members_details()
    librarian1 = Librarian("Sara", "sara@gmail.com", "EMP001")
    librarian1.borrow_book(book2)
    print(librarian1)
    Librarian.display_all_librarians_details()
    print(book2 in librarian1)
