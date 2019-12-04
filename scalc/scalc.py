"""Интерпретатор языка Calculator

Интерпретатор языка calculator, использующий синтаксис Scheme.
Выражения оператора должны быть символами.  Выражения операндов разделяются
пробелами.

Примеры:
    > (* 1 2 3)
    6
    > (+)
    0
    > (+ 2 (/ 4 8))
    2.5
    > (+ 2 2) (* 3 3)
    4
    9
    > (+ 1
         (- 23)
         (* 4 2.5))
    -12
    > )
    SyntaxError: неожиданный токен: )
    > 2.3.4
    ValueError: неправильное число: 2.3.4
    > +
    TypeError: + не является числом или вызывающим выражением
    > (/ 5)
    TypeError: / требует в точности 2 аргумента
    > (/ 1 0)
    ZeroDivisionError: division by zero
"""

#from ucb import trace, main, interact
from operator import add, sub, mul, truediv
from scheme_reader import Pair, nil, scheme_read, buffer_input


# Вычисление & применение

def calc_eval(exp):
    """Вычисление выражения.

    >>> calc_eval(as_scheme_list('+', 2, as_scheme_list('*', 4, 6)))
    26
    >>> calc_eval(as_scheme_list('+', 2, as_scheme_list('/', 40, 5)))
    10
    """
    if type(exp) in (int, float):
        return simplify(exp)
    elif isinstance(exp, Pair):
        arguments = exp.second.map(calc_eval)
        return simplify(calc_apply(exp.first, arguments))
    else:
        raise TypeError(str(exp) + ' не является числом или вызывающим выражением')

def calc_apply(operator, args):
    """Применяет именованный оператор к списку аргументов.

    >>> calc_apply('+', as_scheme_list(1, 2, 3))
    6
    >>> calc_apply('-', as_scheme_list(10, 1, 2, 3))
    4
    >>> calc_apply('-', as_scheme_list(10))
    -10
    >>> calc_apply('*', nil)
    1
    >>> calc_apply('*', as_scheme_list(1, 2, 3, 4, 5))
    120
    >>> calc_apply('/', as_scheme_list(40, 5))
    8.0
    >>> calc_apply('/', as_scheme_list(10))
    0.1
    """
    if not isinstance(operator, str):
        raise TypeError(str(operator) + ' не символ')
    if operator == '+':
        return reduce(add, args, 0)
    elif operator == '-':
        if len(args) == 0:
            raise TypeError(operator + ' требует хотя бы 1 аргумент')
        elif len(args) == 1:
            return -args.first
        else:
            return reduce(sub, args.second, args.first)
    elif operator == '*':
        return reduce(mul, args, 1)
    elif operator == '/':
        if len(args) == 0:
            raise TypeError(operator + ' требует хотя бы 1 аргумент')
        elif len(args) == 1:
            return 1/args.first
        else:
            return reduce(truediv, args.second, args.first)
    else:
        raise TypeError(operator + ' неизвестный оператор')

def simplify(value):
    """Если возможно приводит значение к типу int.

    >>> simplify(8.0)
    8
    >>> simplify(2.3)
    2.3
    >>> simplify('+')
    '+'
    """
    if isinstance(value, float) and int(value) == value:
        return int(value)
    return value

def reduce(fn, scheme_list, start):
    """Свертывает рекурсивный список пар, используя fn и начальное значение.

    >>> reduce(add, as_scheme_list(1, 2, 3), 0)
    6
    """
    if scheme_list is nil:
        return start
    return reduce(fn, scheme_list.second, fn(start, scheme_list.first))

def as_scheme_list(*args):
    """Возвращает рекурсивный список пар, содержащий элементы аргументов.

    >>> as_scheme_list(1, 2, 3)
    Pair(1, Pair(2, Pair(3, nil)))
    """
    if len(args) == 0:
        return nil
    return Pair(args[0], as_scheme_list(*args[1:]))

def read_eval_print_loop():
    """Запускает интерактивный цикл Calculator."""
    while True:
        try:
            src = buffer_input()
            while src.more_on_line:
                expression = scheme_read(src)
                print(calc_eval(expression))
        except (SyntaxError, TypeError, ValueError, ZeroDivisionError) as err:
            print(type(err).__name__ + ':', err)
        except (KeyboardInterrupt, EOFError):  # <Control>-D, и т.д.
            print('Вычисление завершено.')
            return

if __name__ == "__main__":
    read_eval_print_loop()