# 🏦 Banking System with Magic Methods

This Python project simulates a banking system using OOP and magic (dunder) methods.

## 📌 Features

- Base `Account` class and `SavingsAccount` subclass
- Operator overloading using:
  - `__str__`, `__repr__`, `__eq__`, `__lt__`, `__add__`, `__len__`, `__call__`
- Deposit and withdraw with validation
- Callable accounts to deposit/apply interest

## 🧠 Concepts Covered

- Inheritance and Method Overriding
- Class & Static Methods
- Dunder methods and polymorphism
- Input validation

## 🚀 Example Usage

```python
account1 = Account("Ali", "AZ101", 12000)
savings = SavingsAccount("Sohail", "CX303", 34000, 2.5)

account1(1000)          # Deposit
savings()               # Apply interest
savings(2000)           # Deposit with __call__
