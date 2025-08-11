# Fraction Class (operator overloading)

A small Python class that implements rational numbers (fractions) with operator overloading.

## Features
- Normalization (keeps fractions reduced)
- Supports operations with other `Fraction` instances and `int`:
  - `+`, `-`, `*`, `/`
  - reflected ops: `__radd__`, `__rsub__`, `__rmul__`, `__rtruediv__`
  - comparisons: `==`, `<`, `>`
  - conversions: `float()`, `int()`
  - unary ops: `-` (negation), `abs()`
- Defensive validation (zero denominator / division-by-zero errors)

## Example

```python
from fraction_class.fraction_class import Fraction

f1 = Fraction(1, 2)
f2 = Fraction(1, 3)

print(f1 + f2)       # 5/6
print(1 + f1)        # 3/2
print(Fraction(2,4)) # 1/2 (normalized)
print(float(Fraction(3,2)))   # 1.5
print(int(Fraction(7,3)))     # 2
