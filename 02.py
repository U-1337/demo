# Импорт
from math import pi
pi * 71 / 223
from math import sin
sin(pi/2)

# Присвоение
radius = 10
2 * radius
area, circ = pi * radius * radius, 2 * pi * radius

# Значения функций
max
max(3, 4)
f = max
f
f(3, 4)
max = 7
f(3, 4)
f(3, max)
f = 2
# f(3, 4)

# Пользовательские функции
from operator import add, mul
add(2, 3)
mul(2, 3)

def square(x):
    return mul(x, x)

square(21)
square(add(2, 5))
square(square(3))

def sum_squares(x, y):
    return add(square(x), square(y))
sum_squares(3, 4)
sum_squares(5, 12)

# Конфликты имен
def square(square):
    return mul(square, square)
square(4)

# Функция Print (вывод в консоль)
-2
print(-2)
'ну всё!'
print('ну всё!')
print(1, 2, 3)
None
print(None)
x = -2
x
x = print(-2)
x
print(print(1), print(2))