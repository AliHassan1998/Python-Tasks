# 🎓 University System using Single Inheritance

This project simulates a university system where `Student` inherits from the base class `Person`.

## 🧱 Classes

- `Person`: Represents basic individual data (name, age, email).
- `Student`: Inherits from Person and adds student-specific info (ID, GPA, courses).

## 🧠 Concepts Covered

- Single Inheritance
- Data Validation with Static Methods
- Operator Overloading:
  - `__eq__` → compare students/persons
  - `__len__` → course count or name length
  - `__call__` → enroll course
- Class Tracking with `total_` and `all_` class variables

## 🧪 Example
```python
student1 = Student("Ali", 20, "EME101", 3.5)
student1("Physics")
student1.display_courses()
```
## 📦 Output

All Courses Enrolled by Ali:
1: Physics
