# 🏦 Bank Account System with Operator Overloading

This project demonstrates a simple bank account system in Python using **OOP** concepts and **operator overloading**.

## 👨‍💼 Classes

- `BankAccount`: Main class with balance management, deposit, withdrawal, and transaction log.

## 💡 Concepts Covered

- Operator Overloading (`__add__`, `__eq__`, `__gt__`, `__call__`, etc.)
- Static & Class Methods
- Input Validation
- String Parsing (`from_string`)
- Custom `__str__` and `__repr__`

## ✅ Example

```python
account1 = BankAccount("Ali", 12000.0, "Saving")
account2 = BankAccount("Hassan", 14000.0, "Current")
account3 = account1 + account2  # Joint account
```
## 📂 Outputs & Testing

You can run the file to:
See all accounts
Test deposit, withdrawal, balance comparison
View transaction logs
