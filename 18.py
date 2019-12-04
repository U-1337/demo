def fib(n):
    """Вычисляет n-ое число Фибоначчи.

    >>> fib(20)
    6765
    """
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-2) + fib(n-1)

# Время

def count(f):
    """Обёртывает функцию f счетчиком количества вызовов call_count.

    >>> def fib(n):
    ...     if n == 0 or n == 1:
    ...         return n
    ...     else:
    ...         return fib(n-2) + fib(n-1)
    >>> fib = count(fib)
    >>> fib(20)
    6765
    >>> fib.call_count
    21891
    """
    def counted(*args):
        counted.call_count += 1
        return f(*args)
    counted.call_count = 0
    return counted

# Запоминание
def memo(f):
    """Кэширование f.

    >>> def fib(n):
    ...     if n == 0 or n == 1:
    ...         return n
    ...     else:
    ...         return fib(n-2) + fib(n-1)
    >>> fib = count(fib)
    >>> fib(20)
    6765
    >>> fib.call_count
    21891
    >>> counted_fib = count(fib)
    >>> fib  = memo(counted_fib)
    >>> fib(20)
    6765
    >>> counted_fib.call_count
    21
    >>> fib(35)
    9227465
    >>> counted_fib.call_count
    36
    """
    cache = {}
    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memoized

# Пространство

def count_frames(f):
    """Возвращает версию f, подсчитывающую количество вызовов max_count.

    >>> def fib(n):
    ...     if n == 0 or n == 1:
    ...         return n
    ...     else:
    ...         return fib(n-2) + fib(n-1)
    >>> fib = count_frames(fib)
    >>> fib(20)
    6765
    >>> fib.open_count
    0
    >>> fib.max_count
    20
    >>> fib(25)
    75025
    >>> fib.max_count
    25
    """
    def counted(n):
        counted.open_count += 1
        counted.max_count = max(counted.max_count, counted.open_count)
        result = f(n)
        counted.open_count -= 1
        return result
    counted.open_count = 0
    counted.max_count = 0
    return counted

# Порядки роста

from math import sqrt

def divides(k, n):
    """Возвращает результат того, что k нацело делит n."""
    return n % k == 0

def factors(n):
    """Подсчитывает положительные целые, которые делят нацело n.

    >>> factors(576)
    21
    """
    total = 0
    for k in range(1, n+1):
        if divides(k, n):
            total += 1
    return total

def factors_fast(n):
    """Подсчитывает положительные целые, которые делят нацело n.

    >>> factors_fast(576)
    21
    """
    sqrt_n = sqrt(n)
    k, total = 1, 0
    while k < sqrt_n:
        if divides(k, n):
            total += 2
        k += 1
    if k * k == n:
        total += 1
    return total
            
# Пространство

def count_frames(f):
    """Обёртывает функцию f счетчиком количества фреймов max_count.

    >>> def fib(n):
    ...     if n == 0 or n == 1:
    ...         return n
    ...     else:
    ...         return fib(n-2) + fib(n-1)
    >>> fib = count_frames(fib)
    >>> fib(20)
    6765
    >>> fib.open_count
    0
    >>> fib.max_count
    20
    >>> fib(25)
    75025
    >>> fib.max_count
    25
    """
    def counted(n):
        counted.open_count += 1
        counted.max_count = max(counted.max_count, counted.open_count)
        result = f(n)
        counted.open_count -= 1
        return result
    counted.open_count = 0
    counted.max_count = 0
    return counted

def fib(n):
    """Возвращает n-ое число Фибоначчи.

    >>> fib(20)
    6765
    """
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-2) + fib(n-1)

# Возведение в степень

def exp(b, n):
    """Возвращает b в степени n.

    >>> exp(2, 10)
    1024
    """
    if n == 0:
        return 1
    else:
        return b * exp(b, n-1)

def square(x):
    return x*x

def exp_fast(b, n):
    """Возвращает b в степени n.

    >>> exp_fast(2, 10)
    1024
    """
    if n == 0:
        return 1
    elif n % 2 == 0:
        return square(exp_fast(b, n//2))
    else:
        return b * exp_fast(b, n-1)

# Пересечение

def overlap(a, b):
    """Подсчитывает количество элементов входящих как в a, так и в b.

    >>> overlap([1, 3, 2, 2, 5, 1], [5, 4, 2])
    3
    """
    count = 0
    for item in a:
        if item in b:
            count += 1
    return count
