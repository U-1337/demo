#   Разработка, основанная на тестировании

from ucb import trace, interact

def gcd(m, n):
    """Возвращает наибольший общий делитель для m и n.

    Аргументы:
        m, n: положительные целые числа.

    >>> gcd(12, 8)
    4
    >>> gcd(16, 12)
    4
    >>> gcd(16, 8)
    8
    >>> gcd(2, 16)
    2
    >>> gcd(24, 42)
    6
    >>> gcd(5, 5)
    5
    """
    if m == n:
        return m
    elif m < n:
        return gcd(n, m)
    else:
        return gcd(m-n, n)

# Декораторы

def trace1(fn):
    """Возвращает функцию эквивалентную fn, которая в дополнение выводит отладочную информацию.

    Аргументы:
        fn: функция одного аргумента.
    """
    def traced(x):
        print('Вызываем', fn, 'с аргументом', x)
        return fn(x)
    return traced

@trace1
def square(x):
    return x*x

@trace1
def sum_squares_up_to(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + square(k), k + 1
    return total