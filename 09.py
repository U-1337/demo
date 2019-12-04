# Численные типы данных

type(2)
type(1.5)
type(1+1j)
True + True
type(-True)
1/3 == 0.333333333333333300000  # Опасайся аппроксимаций
from math import pi, tan
tan(pi/4)


# Даты

from datetime import date
today = date(2019, 9, 30)
freedom = date(2019, 12, 31)
str(freedom - today)
today.year
today.strftime('%A, %B %d')
type(today)


# Рациональная арифметика

def add_rational(x, y):
    """Складывает рациональные числа x и y."""
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return rational(nx * dy + ny * dx, dx * dy)

def mul_rational(x, y):
    """Перемножает рациональные числа x и y."""
    return rational(numer(x) * numer(y), denom(x) * denom(y))

def rationals_are_equal(x, y):
    """Проверяет равенство между рациональными числами x и y."""
    return numer(x) * denom(y) == numer(y) * denom(x)

def print_rational(x):
    """Печатает рациональное число x."""
    print(numer(x), "/", denom(x))


# Конструктор и селекторы

def rational(n, d):
    """Создает рациональное число, представляющее n/d."""
    return [n, d]

def numer(x):
    """Возвращает числитель рационального числа x."""
    return x[0]

def denom(x):
    """Возвращает знаменатель рационального числа x."""
    return x[1]


# Улучшеный конструктор

from fractions import gcd
def rational(n, d):
    """Создает рациональное число, представляющее n/d с минимальными числителем и знаменателем"""
    g = gcd(n, d)
    return [n//g, d//g]


# Функциональная реализация

def rational(n, d):
    def select(name):
        if name == 'n':
            return n
        elif name == 'd':
            return d
    return select

def numer(x):
    return x('n')

def denom(x):
    return x('d')

x = rational(3,8)
numer(x)