# Smart Device Inspector using `dir()`, `__dict__`, and `help()`

This project demonstrates Python object introspection and inheritance concepts using a `Device` base class and a `SmartPhone` derived class.

## Concepts Covered

- Single Inheritance
- Static Methods
- Class Methods
- Method Overriding
- Dunder Methods:
  - `__str__`
  - `__repr__`
  - `__len__`
- Object Introspection:
  - `dir()`
  - `__dict__`
  - `help()`
- Validation Techniques
- Alternative Constructors (`from_string`)

---

## Classes

### Device

Base class representing a general electronic device.

Attributes:

- `device_id`
- `brand`
- `price`

Methods:

- `device_info()`
- `apply_discount()`
- `from_string()`

---

### SmartPhone

Derived class extending `Device`.

Additional attributes:

- `ram`
- `storage`

Additional methods:

- `install_app()`

Overrides:

- `device_info()`
- `from_string()`
- `__str__()`
- `__repr__()`

---

## Example Usage

```python
d1 = Device("D101", "Dell", 1500)

s1 = SmartPhone("S201", "Apple", 2200, 8, 256)

print(d1.device_info())

print(s1.device_info())

print(d1.__dict__)

print(dir(s1))

help(SmartPhone)
```

---

## Learning Goal

This task focuses on understanding how Python objects can be inspected dynamically using built-in introspection tools.
