# 🧾 Employee Payroll System with Method Overriding

This project demonstrates an employee payroll system using Python OOP and method overriding.

## 👨‍💼 Classes

- `Employee`: Base class with salary calculation.
- `FullTimeEmployee`: Inherits and overrides salary by adding bonus.
- `PartTimeEmployee`: Inherits and overrides salary based on hours worked.

## 💡 Concepts Covered

- Inheritance and Method Overriding
- Static & Class Methods
- Data Validation & Error Handling
- Dunder Methods: `__str__`, `__repr__`

## 🚀 Example

```python
FullTimeEmployee("Ali", "FT101", 12000, 2000).calculate_salary()
# Output: 14000
