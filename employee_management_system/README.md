# Employee Management System with Method Overriding

This Python project demonstrates OOP concepts like inheritance, polymorphism, and method overriding to simulate a company structure with employees, developers, and managers.

---

## 🔧 Key Concepts:
- Inheritance: `Employee → Developer`, `Employee → Manager`
- Method Overriding: `work()` method redefined in each class
- Magic Methods: `__str__`, `__repr__`, `__eq__`, `__len__`, `__gt__`
- Regex validation for email format
- Object creation via `from_string()` methods
- Object tracking via class variables

---

## 👨‍💼 Features:
- Create and display employees, developers, and managers
- Validate email inputs
- Compare salaries and employees
- Track total counts and store all instances
- Demonstrate custom behavior using overridden methods

---

## 🚀 How to Run:
```bash
python employee_management_system.py

## Sample Output:
Employee: Ali is working.
Developer: Sohail is coding in Python.
Manager: Zaheer is managing a team of 5 people.
Total Employees are: 6 out of which there are 2 developers and 2 managers.
