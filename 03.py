# Операторы
from operator import add, mul
2 + 3
add(2, 3)
2 + 3 * 4 + 5
add(add(2, mul(3, 4)) , 5)
(2 + 3) * (4 + 5)
mul(add(2, 3), add(4, 5))

# Деление
1337 / 10
1337 // 10
1337 % 10
from operator import truediv, floordiv, mod
floordiv(1337, 10)
truediv(1337, 10)
mod(1337, 10)

5 / 3
5 // 3
5 % 3

# Несколько возвращаемых значений
def divide_exact(n, d):
    return n // d, n % d
quotient, remainder = divide_exact(1337, 10)

# Докстринги, доктесты и аргументы по умолчанию
def divide_exact(n, d):
    """Возвращает частное (quotient) и остаток (remainder) от деления n на d.

    >>> quotient, remainder = divide_exact(1337, 10)
    >>> quotient
    133
    >>> remainder
    10
    """
    return floordiv(n, d), mod(n, d)

# Аргументы по умолчанию
def increase(number, by=1):
    return number + by

# Условные выражения
def absolute_value(x):
    """Возвращает модуль значения x.

    >>> absolute_value(-3)
    3
    >>> absolute_value(0)
    0
    >>> absolute_value(3)
    3
    """
    if x < 0:
        return -x
    elif x == 0:
        return 0
    else:
        return x

# Суммирование с помощью while
i, total = 0, 0
while i < 3:
    i = i + 1
    total = total + i
total
