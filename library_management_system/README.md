# 📚 Library Management System with Method Overriding

A Python-based system to manage different book formats including physical books, eBooks, and audiobooks.

## 🧱 Classes

- `Book`: Base class with ISBN validation and price discount logic.
- `EBook`: Inherits `Book`, adds `file_size` and overrides display methods.
- `AudioBook`: Inherits `Book`, adds `duration` and overrides display methods.

## 💡 Key Concepts

- Inheritance and Method Overriding
- Dunder Methods: `__str__`, `__repr__`
- Static and Class Methods
- Validation and Discount Calculation
- Object Tracking with Class Variables

## 🔄 Example

```python
ebook = EBook("SpiderMan", "Abbas", "0123456789012", 650, 34)
print(ebook.discounted_price(10))  # Output: 585.0
print(ebook.get_format())          # Output: Digital PDF/Epub SpiderMan of size: 34MB

## 📊 Stats
Total Books Tracked
Total EBooks & AudioBooks
