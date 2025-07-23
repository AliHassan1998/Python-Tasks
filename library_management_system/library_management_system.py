# Library Management System with Method Overriding
import re


class Book:
    total_books = 0
    all_books = []

    def __init__(self, title, author, isbn, price):
        self.title = title
        self.author = author
        if Book.validate_isbn(isbn):
            self.isbn = isbn
        else:
            raise ValueError("Error: Oops! Invalid ISBN. It must be a valid 13 digit ISBN.")
        if Book.validate_price(price):
            self.price = price
        else:
            raise ValueError("Error: Oops! Price can't be negative.")
        Book.total_books += 1
        Book.all_books.append(self)

    @staticmethod
    def validate_isbn(isbn):
        pattern = r'^\d{13}$'
        if re.fullmatch(pattern, isbn):
            return True
        else:
            return False

    @staticmethod
    def validate_price(price):
        if price >= 0:
            return True
        else:
            return False

    def __str__(self):
        return f"Book's Details: \nBook Title: {self.title} \nBook Author: {self.author} \n" \
               f"Book ISBN: {self.isbn} \nBook Price: {self.price}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', '{self.isbn}', {self.price})"

    def get_format(self):
        return f"Physical Copy of {self.title}"

    def discounted_price(self, discount_percent):
        if 0 <= discount_percent <= 100:
            discount = (discount_percent / 100) * self.price
            return self.price - discount
        else:
            raise ValueError("Error: Oops! Discount Percent must be between 0-100.")

    @classmethod
    def from_string(cls, book_str):
        try:
            title, author, isbn, price = book_str.strip().split(",")
            return cls(title, author, isbn, float(price))
        except Exception as e:
            print(f"Error: {e}")

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
            print("Oops! There are no Books to display.")


class EBook(Book):
    total_ebooks = 0
    all_ebooks = []

    def __init__(self, title, author, isbn, price, file_size):
        super().__init__(title, author, isbn, price)
        if EBook.validate_file_size(file_size):
            self.file_size = file_size
        else:
            raise ValueError("Error: Oops! File Size can't be negative.")
        EBook.total_ebooks += 1
        EBook.all_ebooks.append(self)

    @staticmethod
    def validate_file_size(file_size):
        if file_size >= 0:
            return True
        else:
            return False

    def get_format(self):
        return f"Digital PDF/Epub {self.title} of size: {self.file_size}MB"

    def __str__(self):
        return str(super().__str__() + f" \nBook File Size: {self.file_size}MB").replace("Book", "EBook")

    def __repr__(self):
        return f"EBook('{self.title}', '{self.author}', '{self.isbn}', {self.price}, {self.file_size})"

    @classmethod
    def from_string(cls, ebook_str):
        try:
            title, author, isbn, price, file_size = ebook_str.strip().split(",")
            return cls(title, author, isbn, float(price), float(file_size))
        except Exception as e:
            print(f"Error: {e}")

    @classmethod
    def display_all_ebooks(cls):
        if cls.all_ebooks:
            print("All EBook's Details: ")
            print("--" * 30)
            for no, ebook in enumerate(cls.all_ebooks, start=1):
                print(f"Ebook {no}: ")
                print(ebook)
                print("--" * 30)
        else:
            print("Oops! There are no EBooks to display.")


class AudioBook(Book):
    total_audio_books = 0
    all_audio_books = []

    def __init__(self, title, author, isbn, price, duration):
        super().__init__(title, author, isbn, price)
        if AudioBook.validate_duration(duration):
            self.duration = duration
        else:
            raise ValueError("Error: Oops! Audio Duration can't be negative.")
        AudioBook.total_audio_books += 1
        AudioBook.all_audio_books.append(self)

    @staticmethod
    def validate_duration(duration):
        if duration >= 0:
            return True
        else:
            return False

    def get_format(self):
        return f"MP3 AudioBook {self.title} of duration: {self.duration} minutes."

    def __str__(self):
        return str(super().__str__() + f" \nBook Duration: {self.duration} minutes").replace("Book", "AudioBook")

    def __repr__(self):
        return f"AudioBook('{self.title}', '{self.author}', '{self.isbn}', {self.price}, {self.duration})"

    @classmethod
    def from_string(cls, audiobook_str):
        try:
            title, author, isbn, price, duration = audiobook_str.strip().split(",")
            return cls(title, author, isbn, float(price), int(duration))
        except Exception as e:
            print(f"Error: {e}")

    @classmethod
    def display_all_audio_books(cls):
        if cls.all_audio_books:
            print("All Audio Book's Details: ")
            print("--" * 30)
            for no, audio_book in enumerate(cls.all_audio_books, start=1):
                print(f"Audio Book {no}: ")
                print(audio_book)
                print("--" * 30)
        else:
            print("Oops! There are no Audio Books to display.")


if __name__ == "__main__":
    book1 = Book("BatMan", "Ali", "1234567890123", 350.0)
    book2 = Book.from_string("SuperMan,Hassan,4567890123456,450")
    ebook1 = EBook("Ironman", "Sohail", "7890123456789", 550.0, 22.0)
    ebook2 = EBook.from_string("SpiderMan,Abbas,0123456789012,650,34")
    audio_book1 = AudioBook("AntMan", "Zaheer", "3456789012345", 750.0, 16)
    audio_book2 = AudioBook.from_string("HardMan,Asif,6789012345678,850,11")
    print(book1)
    print(repr(book1))
    print(book2)
    print(repr(book2))
    print(ebook1)
    print(repr(ebook1))
    print(ebook2)
    print(audio_book1)
    print(repr(audio_book1))
    print(audio_book2)
    print(repr(audio_book2))
    print(f"The new price of {book1.title} after discount is: {book1.discounted_price(5)}")
    print(f"The new price of {book2.title} after discount is: {book2.discounted_price(6)}")
    print(f"The new price of {ebook1.title} after discount is: {ebook1.discounted_price(7)}")
    print(f"The new price of {ebook2.title} after discount is: {ebook2.discounted_price(8)}")
    print(f"The new price of {audio_book1.title} after discount is: {audio_book1.discounted_price(9)}")
    print(f"The new price of {audio_book2.title} after discount is: {audio_book2.discounted_price(10)}")
    print(book1.get_format())
    print(book2.get_format())
    print(ebook1.get_format())
    print(ebook2.get_format())
    print(audio_book1.get_format())
    print(audio_book2.get_format())
    print(f"There are {Book.total_books} books in total, out of which {EBook.total_ebooks} are EBooks and "
          f"{AudioBook.total_audio_books} are Audio Books.")
    AudioBook.display_all_audio_books()
    EBook.display_all_ebooks()
    Book.display_all_books()
