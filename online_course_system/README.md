# Online Course System using `super()` in Python

A Python OOP project demonstrating inheritance and `super()` using an online course management system.

---

## Concepts Covered

- Single Inheritance
- `super()`
- Method Overriding
- Static Methods
- Class Methods
- Validation
- Dunder Methods:
  - `__str__`
  - `__repr__`
  - `__len__`
- Alternative Constructors (`from_string`)
- Class Variables

---

## Classes

### Course

Base course class.

Features:

- Course validation
- Discount application
- Free course checking
- Alternative constructor
- Course information display

### PremiumCourse

Derived class extending `Course`.

Additional Features:

- Support hours
- Certificate status
- Premium support session

Overrides:

- `course_details()`
- `__str__()`
- `from_string()`

---

## Example Usage

```python
course1 = Course("C101", "Programming Fundamentals", "Ali", 1200)

premium1 = PremiumCourse(
    "P303",
    "Pre-Calculus",
    "Sohail",
    1600,
    12,
    True
)

print(course1.course_details())

print(premium1.watch_support_session())
```

---

## Learning Goal

This task focuses on understanding Python inheritance and practical use of `super()` for extending parent class behavior.
