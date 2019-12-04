def str_repr_demos():
    from fractions import Fraction
    half = Fraction(1, 2)
    half
    print(half)
    str(half)
    repr(half)

    s = 'hello world'
    str(s)
    repr(s)
    "'hello world'"
    repr(repr(repr(s)))
    eval(eval(eval(repr(repr(repr(s))))))
    # Errors: eval('hello world')

# Реализация базовых строковых функций

class Bear:
    """Медведь"""
    def __init__(self):
        self.__repr__ = lambda: 'винни пух'
        self.__str__ = lambda: 'медведь винни пух'

    def __repr__(self):
        return 'Bear()'

    def __str__(self):
        return 'медведь'

def print_bear():
    winnie = Bear()
    print(winnie)
    print(str(winnie))
    print(repr(winnie))
    print(winnie.__repr__())
    print(winnie.__str__())

def repr(x):
    s = type(x).__repr__(x)
    if not isinstance(s, str):
        raise TypeError
    return s

def str(x):
    s = type(x).__str__(x)
    if not isinstance(s, str):
        raise TypeError
    return s

# Рациональные числа
from fractions import gcd

class Ratio:
    """Изменяемая дробь.

    >>> f = Ratio(9, 15)
    >>> f
    Ratio(9, 15)
    >>> print(f)
    9/15

    >>> Ratio(1, 3) + Ratio(1, 6)
    Ratio(1, 2)
    >>> f + 1
    Ratio(8, 5)
    >>> 1 + f
    Ratio(8, 5)
    >>> 1.4 + f
    2.0
    """
    def __init__(self, n, d):
        self.numer = n
        self.denom = d

    def __repr__(self):
        return 'Ratio({0}, {1})'.format(self.numer, self.denom)

    def __str__(self):
        return '{0}/{1}'.format(self.numer, self.denom)

    def __add__(self, other):
        if isinstance(other, Ratio):
            n = self.numer * other.denom + self.denom * other.numer
            d = self.denom * other.denom
        elif isinstance(other, int):
            n = self.numer + self.denom * other
            d = self.denom
        else:
            return float(self) + other
        g = gcd(n, d)
        r = Ratio(n // g, d // g)
        return r

    __radd__ = __add__

    @property
    def float_value(self):
        return self.numer/self.denom

    def __float__(self):
        return self.float_value

# Комплексные числа

from math import atan2, sin, cos, pi

class Complex:
    def add(self, other):
        return ComplexRI(self.real + other.real, 
                         self.imag + other.imag)

    def mul(self, other):
        return ComplexMA(self.magnitude * other.magnitude, 
                         self.angle + other.angle)

    def __add__(self, other):
        return self.add(other)

    def __mul__(self, other):
        return self.mul(other)
        

class ComplexRI(Complex):
    """Декартово представление комплексного числа.

    >>> from math import pi
    >>> ComplexRI(1, 2).add(ComplexMA(2, pi/2))
    ComplexRI(1.0000000000000002, 4.0)
    >>> ComplexRI(0, 1).mul(ComplexRI(0, 1))
    ComplexMA(1.0, 3.141592653589793)
    >>> ComplexRI(1, 2) + ComplexMA(2, 0)
    ComplexRI(3.0, 2.0)
    >>> ComplexRI(0, 1) * ComplexRI(0, 1)
    ComplexMA(1.0, 3.141592653589793)
    """
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    @property
    def magnitude(self):
        return (self.real ** 2 + self.imag ** 2) ** 0.5

    @property
    def angle(self):
        return atan2(self.imag, self.real)

    def __repr__(self):
        return 'ComplexRI({0}, {1})'.format(self.real,
                                            self.imag)

class ComplexMA(Complex):
    """Полярное представление комплексного числа."""
    def __init__(self, magnitude, angle):
        self.magnitude = magnitude
        self.angle = angle

    @property
    def real(self):
        return self.magnitude * cos(self.angle)

    @property
    def imag(self):
        return self.magnitude * sin(self.angle)

    def __repr__(self):
        return 'ComplexMA({0}, {1})'.format(self.magnitude,
                                            self.angle)