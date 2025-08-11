# Build a Fraction class (operator overloading)
import math


class Fraction:
    def __init__(self, numerator: int, denominator: int):
        self.numerator = numerator
        if Fraction.validate_denominator(denominator):
            self.denominator = denominator
        else:
            raise ValueError("Error: Oops! Denominator can't be Zero and must be an Integer Value.")
        self._normalize()

    @staticmethod
    def validate_denominator(denominator):
        if denominator != 0 and isinstance(denominator, int):
            return True
        else:
            return False

    @staticmethod
    def gcd_calculation(numerator, denominator):
        return math.gcd(numerator, denominator)

    def _normalize(self):
        gcd = Fraction.gcd_calculation(self.numerator, self.denominator)
        self.numerator = self.numerator // gcd
        self.denominator = self.denominator // gcd
        if self.denominator < 0:
            self.numerator = self.numerator * -1
            self.denominator = self.denominator * -1

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
        return f"Fraction({self.numerator}, {self.denominator})"

    def __add__(self, other):
        if isinstance(other, Fraction):
            return Fraction((self.numerator * other.denominator) + (self.denominator * other.numerator),
                            self.denominator * other.denominator)
        elif isinstance(other, int):
            other = Fraction(other, 1)
            return Fraction((self.numerator * other.denominator) + (self.denominator * other.numerator),
                            self.denominator * other.denominator)
        return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Fraction):
            return Fraction((self.numerator * other.denominator) - (self.denominator * other.numerator),
                            self.denominator * other.denominator)
        elif isinstance(other, int):
            other = Fraction(other, 1)
            return Fraction((self.numerator * other.denominator) - (self.denominator * other.numerator),
                            self.denominator * other.denominator)
        return NotImplemented

    def __rsub__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        return other.__sub__(self)

    def __mul__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)
        elif isinstance(other, int):
            other = Fraction(other, 1)
            return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, Fraction):
            if other.numerator == 0:
                raise ZeroDivisionError("Error: Oops! Division of 0 is not allowed. Can't divide 0.")
            else:
                return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)
        elif isinstance(other, int):
            other = Fraction(other, 1)
            if other.numerator == 0:
                raise ZeroDivisionError("Denominator cannot be Zero.")
            else:
                return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)
        return NotImplemented

    def __rtruediv__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        return other.__truediv__(self)

    def __eq__(self, other):
        if isinstance(other, Fraction):
            return self.numerator * other.denominator == self.denominator * other.numerator
        elif isinstance(other, int):
            other = Fraction(other, 1)
            return self.numerator * other.denominator == self.denominator * other.numerator
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Fraction):
            return self.numerator * other.denominator < self.denominator * other.numerator
        elif isinstance(other, int):
            other = Fraction(other, 1)
            return self.numerator * other.denominator < self.denominator * other.numerator
        return NotImplemented

    def __float__(self):
        return float(self.numerator / self.denominator)

    def __neg__(self):
        return Fraction(-1 * self.numerator, self.denominator)

    def __abs__(self):
        return Fraction(abs(self.numerator), self.denominator)

    def __int__(self):
        return int(self.numerator / self.denominator)


if __name__ == "__main__":
    f1 = Fraction(1, 2)
    f2 = Fraction(1, 3)
    print(f1)
    print(f2)
    print(repr(f1))
    print(repr(f2))
    print(f1 + f2)
    print(f1 - f2)
    print(Fraction(2, 3) * Fraction(3, 4))
    print(Fraction(3, 4) * f1)
    print(f1 + 1)
    print(1 + f1)
    print(Fraction(5, 2) - 2)
    print(3 * Fraction(2, 5))
    print(Fraction(2, 4) == f1)
    print(f2 < f1)
    print(float(Fraction(3, 2)))
    print(int(Fraction(7, 3)))
    print(-f1)
    print(abs(Fraction(-3, 4)))
