# Library System using Magic/Dunder Methods

This project is a Python-based simulation of a library system that demonstrates the use of OOP principles, validation, and magic methods like `__str__`, `__repr__`, `__len__`, and `__eq__`.

---

## 🔧 Key Concepts:
- Inheritance: `Member → Librarian`
- Magic methods: `__str__`, `__repr__`, `__len__`, `__eq__`, `__contains__`
- Validation with regular expressions
- Object creation via factory methods
- Class-level tracking of all objects

---

## 📚 Features:
- Register books, members, and librarians
- Validate ISBN (`123-1234567890`) and email
- Borrow books and remove them from the library
- Compare books via ISBN (`__eq__`)
- Count borrowed books using `len()`
- Check if a book is borrowed using `in` operator

---

## 🚀 How to Run:
```bash
python library_system_with_dunder_methods.py

## Sample Output:
Book: 1984 by George Orwell.
Book('1984', 'George Orwell', '123-1234567890', '328')
False
The book has been successfully borrowed.
True
False
Librarian: Sara (ID: EMP001) has borrowed 1 books.
