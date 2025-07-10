# Library System with Method Overriding and Dunder Methods
import re


class LibraryItem:
    total_items = 0
    all_items = []

    def __init__(self, title, item_id):
        self.title = title
        if LibraryItem.is_valid_item_id(item_id):
            self.item_id = item_id
            LibraryItem.total_items += 1
            LibraryItem.all_items.append(self)
        else:
            raise ValueError("Invalid Item ID.")

    @staticmethod
    def is_valid_item_id(item_id):
        pattern = r'^[a-zA-Z]{3}\d{3}$'
        if re.fullmatch(pattern, item_id):
            return True
        else:
            return False

    def __str__(self):
        return (f"Library Item's Details: \nItem Title: {self.title} \n"
                f"Item ID: {self.item_id}")

    def __repr__(self):
        return f"LibraryItem('{self.title}', '{self.item_id}')"

    def __eq__(self, other):
        if isinstance(other, LibraryItem):
            return self.item_id == other.item_id
        return NotImplemented

    def __len__(self):
        return len(self.title)

    def borrow(self):
        return f"Borrowing a library item of id '{self.item_id}' ..."

    @classmethod
    def from_string(cls, string):
        title, item_id = string.strip().split(",")
        return cls(title, item_id)

    @classmethod
    def display_all_items(cls):
        if cls.all_items:
            print("All Item's Details: ")
            print("--" * 30)
            for no, item in enumerate(cls.all_items, start=1):
                print(f"Item {no}: ")
                print(item)
                print("--" * 30)
        else:
            print("Oops! There are no items to display.")


class Book(LibraryItem):
    total_books = 0
    all_books = []

    def __init__(self, title, item_id, author):
        super().__init__(title, item_id)
        self.author = author
        Book.total_books += 1
        Book.all_books.append(self)

    def __str__(self):
        return str(super().__str__() + f"\nBook Author: {self.author}").replace("Item", "Book")

    def __repr__(self):
        return f"Book('{self.title}', '{self.item_id}', '{self.author}')"

    def borrow(self):
        return f"Borrowing the book '{self.title}' by '{self.author}'."

    @classmethod
    def from_string(cls, string):
        title, item_id, author = string.strip().split(",")
        return cls(title, item_id, author)

    @classmethod
    def display_all_books(cls):
        if cls.all_books:
            print("All Book's Details: ")
            print("--" * 30)
            for no, book in enumerate(cls.all_books, start=1):
                print(f"Book {no}: ")
                print(book)
                print("--" * 30)
        else:
            print("Oops! There are no books to display.")


class Magazine(LibraryItem):
    total_magazines = 0
    all_magazines = []

    def __init__(self, title, item_id, issue_number):
        super().__init__(title, item_id)
        self.issue_number = issue_number
        Magazine.total_magazines += 1
        Magazine.all_magazines.append(self)

    def __str__(self):
        return str(super().__str__() + f"\nMagazine Issue Number: {self.issue_number}").replace("Item", "Magazine")

    def __repr__(self):
        return f"Magazine('{self.title}', '{self.item_id}', {self.issue_number})"

    def borrow(self):
        return f"Borrowing magazine '{self.title}', issue #{self.issue_number}."

    @classmethod
    def from_string(cls, string):
        title, item_id, issue_number = string.strip().split(",")
        return cls(title, item_id, int(issue_number))

    @classmethod
    def display_all_magazines(cls):
        if cls.all_magazines:
            print("All Magazine's Details: ")
            print("--" * 30)
            for no, magazine in enumerate(cls.all_magazines, start=1):
                print(f"Magazine {no}: ")
                print(magazine)
                print("--" * 30)
        else:
            print("Oops! There are no magazines to display.")


if __name__ == "__main__":
    item1 = LibraryItem("Harry Potter", "ABC123")
    item2 = LibraryItem.from_string("Games of Thrones,DEF456")
    book1 = Book("Veronica decides to die", "GHI789", "Paul Cole")
    book2 = Book.from_string("God and Love,JKL012,Hashim Nadeem")
    magazine1 = Magazine("Sunday Magazine", "MNO345", 10)
    magazine2 = Magazine.from_string("Tuesday Magazine,PQR678,15")
    print(item1.borrow())
    print(item2.borrow())
    print(book1.borrow())
    print(book2.borrow())
    print(magazine1.borrow())
    print(magazine2.borrow())
    print(item1 == book2)
    print(item2 == magazine1)
    print(book1 == magazine2)
    print(len(item1))
    print(len(book2))
    print(len(magazine1))
    print(item1)
    print(repr(item2))
    print(book1)
    print(repr(book2))
    print(magazine2)
    print(repr(magazine1))
    LibraryItem.display_all_items()
    Book.display_all_books()
    Magazine.display_all_magazines()
    print(f"Total Items are: {LibraryItem.total_items}, out of which {Book.total_books} are books and "
          f"{Magazine.total_magazines} are magazines.")
