# Academic People Hierarchy System

This Python project models a university-like hierarchy using multi-level inheritance (`Person → Staff → Faculty`). It includes validation, introspection, and class-level object tracking.

### 💡 Concepts Covered:
- Multi-Level Inheritance using `super()`
- Email and Employee ID validation using regex
- `from_string()` alternative constructors
- Object tracking with `total_*` and `all_*` variables
- Introspection with `__dict__`, `dir()`, `help()`
- Behavior extension with `add_course()` for Faculty

### 🧪 Features:
- Create and validate persons, staff, and faculty
- Assign courses to faculty
- Display and track all objects
- Inspect internals using built-in Python methods

### 🚀 How to Run:
```bash
python academic_people_hierarchy.py

### Sample Output
The entered email is valid.
The entered Employee ID is valid.
Faculty designation: Assistant Professor
Courses taught by Faculty: ['Physics', 'Chemistry']
Total persons: 6
Total staff: 2
Total faculty: 2
