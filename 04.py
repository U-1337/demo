# Итерация

def fib(n):
    """Вычисляет n-ное число Фибоначчи, для n >= 2.

    >>> fib(8)
    21
    """
    pred, curr = 0, 1   # 0-ое и 1-ое числа Фибоначчи
    k = 1               # Номер текущего числа Фибоначчи
    while k < n:
        pred, curr = curr, pred + curr
        k = k + 1
    return curr

def pyramid(n):
    """Суммирование увеличивающейся и уменьшающейся последовательностей.
    
    >>> pyramid(10)
    100
    """
    a, b, total = 0, n, 0
    while b:
        a, b = a+1, b-1
        total = total + a + b
    return total

# Приёмы обобщения с помощью аргументов

from math import pi, sqrt

def area_square(r):
    """Возвращает площадь квадрата с длиной стороны r."""
    return r * r

def area_circle(r):
    """Возвращает площадь круга, радиусом r."""
    return r * r * pi

def area_hexagon(r):
    """Возвращает площадь правильного шестиугольника с длиной стороны r."""
    return r * r * 3 * sqrt(3) / 2

def area(r, shape_constant):
    """Возвращает площадь фигуры в зависимости от некоторой длины r."""
    assert r > 0, 'Длина должна быть положительной'
    return r * r * shape_constant

def area_square(r):
    return area(r, 1)

def area_circle(r):
    return area(r, pi)

def area_hexagon(r):
    return area(r, 3 * sqrt(3) / 2)

# Фуккции в качестве аргументов

def sum_naturals(n):
    """Сумма первых n натуральных чисел.

    >>> sum_naturals(5)
    15
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + k, k + 1
    return total

def sum_cubes(n):
    """Сумма первых n кубов натуральных чисел.

    >>> sum_cubes(5)
    225
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + pow(k, 3), k + 1
    return total

def identity(k):
    return k

def cube(k):
    return pow(k, 3)

def summation(n, term):
    """Сумма первых n членов (terms) последовательности.

    >>> summation(5, cube)
    225
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total

from operator import mul

def pi_term(k):
    return 8 / mul(k * 4 - 3, k * 4 - 1)

summation(10000, pi_term)


# Локальное задание функций; возвращение функций

def make_adder(n):
    """Возвращает функцию, принимающую один аргумент k и возвращающую k + n.

    >>> add_three = make_adder(3)
    >>> add_three(4)
    7
    """
    def adder(k):
        return k + n
    return adder

make_adder(1300)(37)