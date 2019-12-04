# Функции в роли аргументов

def apply_twice(f, x):
    """Возвращает f(f(x))

    >>> apply_twice(square, 2)
    16
    >>> from math import sqrt
    >>> apply_twice(sqrt, 16)
    2.0
    """
    return f(f(x))

def square(x):
    return x * x

result = apply_twice(square, 2)

# Функции в качестве возвращаемых значений

def make_adder(n):
    """Возвражает функцию, принимающую один аргумент k и возвращающую k + n.

    >>> add_three = make_adder(3)
    >>> add_three(4)
    7
    """
    def adder(k):
        return k + n
    return adder

# Каррирование

def curry2(f):
    """Возвращает функцию g, такую что g(x)(y) возвращает результат f(x, y).

    >>> from operator import add
    >>> add_three = curry2(add)(3)
    >>> add_three(4)
    7
    """
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g

# Область видимости и возвращение функций

def f(x, y):
    return g(x)

def g(a):
    return a + y

# Это выражение приведет к ошибке, поскольку y не определено во фрейме g.
# f(1, 2)

# Композиция

def compose1(f, g):
    """Возвращает композицию f и g.

    f, g -- функции одного аргумента
    """
    def h(x):
        return f(g(x))
    return h

def triple(x):
    return 3 * x

squiple = compose1(square, triple)
tripare = compose1(triple, square)
squadder = compose1(square, make_adder(2))

