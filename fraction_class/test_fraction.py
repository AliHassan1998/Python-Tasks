3. Paste the sample pytest tests below:

```python
from fraction_class.fraction_class import Fraction

def test_add_fraction():
    assert Fraction(1,2) + Fraction(1,3) == Fraction(5,6)

def test_add_int_and_fraction():
    assert 1 + Fraction(1,2) == Fraction(3,2)

def test_mul_and_normalize():
    assert Fraction(2,4) == Fraction(1,2)
    assert Fraction(2,3) * Fraction(3,4) == Fraction(1,2)

def test_division_by_zero_raises():
    try:
        _ = Fraction(1,2) / Fraction(0,1)
        assert False, "Expected ZeroDivisionError"
    except ZeroDivisionError:
        assert True

def test_neg_abs_int_float():
    assert -Fraction(1,2) == Fraction(-1,2)
    assert abs(Fraction(-3,4)) == Fraction(3,4)
    assert float(Fraction(3,2)) == 1.5
    assert int(Fraction(7,3)) == 2
