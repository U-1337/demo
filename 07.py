# Порядок вызовов

def cascade(n):
    """Печатает каскад префиксов n.

    >>> cascade(1234)
    1234
    123
    12
    1
    12
    123
    1234
    """
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n//10)
        print(n)

def cascade2(n):
    """Печатает каскад префиксов n."""
    print(n)
    if n >= 10:
        cascade(n//10)
        print(n)

def inverse_cascade(n):
    """Печатает обратный каскад префиксов n.
    
    >>> inverse_cascade(1234)
    1
    12
    123
    1234
    123
    12
    1
    """
    grow(n)
    print(n)
    shrink(n)

def f_then_g(f, g, n):
    if n:
        f(n)
        g(n)

grow = lambda n: f_then_g(grow, print, n//10)
shrink = lambda n: f_then_g(print, shrink, n//10)

# Древовидная рекурсия

def fib(n):
    """Вычисляет n-ное число Фибоначчи.

    >>> fib(8)
    21
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)

def count_partitions(n, m):
    """Подсчет разбиений n на не превосходящие m части.

    >>> count_partitions(6, 4)
    9
    >>> count_partitions(10, 10)
    42
    """
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        with_m = count_partitions(n-m, m)
        without_m = count_partitions(n, m-1)
        return with_m + without_m
