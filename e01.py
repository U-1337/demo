# Прямая реализация интерактивного улучшения

def square_root(a):
    """Возвращает квадратный корень из a.

    >>> square_root(9)
    3.0
    """
    x = 1
    while x * x != a:
        x = square_root_update(x, a)
    return x

def square_root_update(x, a):
    return (x + a/x) / 2

def cube_root(a):
    """Возвращает кубический корень из a.

    >>> cube_root(27)
    3.0
    """
    x = 1
    while pow(x, 3) != a:
        x = cube_root_update(x, a)
    return x

def cube_root_update(x, a):
    return (2*x + a/(x*x)) / 3

# Обобщение итеративного улучшения

def improve(update, close, guess=1):
    """Итеративно улучшает guess с помощью update, пока close(guess) является ложью."""
    while not close(guess):
        guess = update(guess)
    return guess

def improve(update, close, guess=1, max_updates=100):
    """Итеративно улучшает guess с помощью update, пока close(guess) является ложью или
    количество итераций меньше max_updates."""
    k = 0
    while not close(guess) and k < max_updates:
        guess = update(guess)
        k = k + 1
    return guess

def approx_eq(x, y, tolerance=1e-15):
    return abs(x - y) < tolerance

def square_root_improve(a):
    """Возвращает квадратный корень из a.

    >>> square_root_improve(9)
    3.0
    """
    def update(x):
        return square_root_update(x, a)
    def close(x):
        return approx_eq(x * x, a)
    return improve(update, close)

def cube_root_improve(a):
    """Возвращает кубический корень из a.

    >>> cube_root_improve(27)
    3.0
    """
    return improve(lambda x: cube_root_update(x, a),
                   lambda x: approx_eq(x*x*x, a))

# Метод Ньютона

def find_zero(f, df):
    """Возвращает нули функции f, имеющую производную df."""
    def near_zero(x):
        return approx_eq(f(x), 0)
    return improve(newton_update(f, df), near_zero)

def newton_update(f, df):
    """Возвращает функцию update для функции f, имеющей производную df, используя
    метод Ньютона."""
    def update(x):
        return x - f(x) / df(x)
    return update

def square_root_newton(a):
    """Возвращает квадратный корень из a.

    >>> square_root_newton(9)
    3.0
    """
    def f(x):
        return x*x - a
    def df(x):
        return 2*x
    return find_zero(f, df)

def cube_root_newton(a):
    """Возвращает кубический корень из a.

    >>> cube_root_newton(27)
    3.0
    """
    return find_zero(lambda x: x*x*x - a, lambda x: 3*x*x)

def power(x, n):
    """Возвращает x * x * x * ... * x для x повторенного n раз."""
    product, k = 1, 0
    while k < n:
        product, k = product * x, k + 1
    return product

def nth_root_of_a(n, a):
    """Возвращает корень n-ой степени из a.

    >>> nth_root_of_a(2, 64)
    8.0
    >>> nth_root_of_a(3, 64)
    4.0
    >>> nth_root_of_a(6, 64)
    2.0
    """
    def f(x):
        return power(x, n) - a
    def df(x):
        return n * power(x, n-1)
    return find_zero(f, df)
