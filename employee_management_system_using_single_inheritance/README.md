# 👔 Employee Management System (Single Inheritance)

This project demonstrates an employee management system using Python OOP concepts with single inheritance.

## 👨‍💼 Classes

- `Employee`: Base class with common attributes and salary logic.
- `Manager`: Subclass that extends `Employee` with department and team size.

## ✅ Features

- Dunder Methods: `__str__`, `__repr__`, `__eq__`, `__len__`, `__call__`
- Input validation (age, salary, team size)
- Class methods & static methods
- Email auto-generation
- Senior manager identification

## 🧪 Example

```python
manager2 = Manager.from_string("Abbas,29,45000,IT,6")
print(manager2.is_senior())  # Output: True
manager2(4)  # Increases team size by 4
print(manager2.team_size)    # Output: 10
