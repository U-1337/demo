# Списки

odds = [41, 43, 47, 49]
len(odds)
odds[1]
odds[0] * odds[3] + len(odds)
odds[odds[3]-odds[2]]

# Контейнеры

digits = [1, 8, 2, 8]
1 in digits
'1' in digits
[1, 8] in digits
[1, 2] in [[1, 2], 3]

# Инструкция for

digits = [1, 8, 2, 8]

def count_while(s, value):
    """Подсчитывает количество вхождений value в последовательность s.

    >>> count_while(digits, 8)
    2
    """
    total, index = 0, 0
    while index < len(s):
        if s[index] == value:
            total = total + 1
        index = index + 1
    return total

def count_for(s, value):
    """Подсчитывает количество вхождений value в последовательность s.

    >>> count_for(digits, 8)
    2
    """
    total = 0
    for elem in s:
        if elem == value:
            total = total + 1
    return total


def count_same(pairs):
    """Возвращает количество пар, содержащих одинаковые элементы.

    >>> pairs = [[1, 2], [2, 2], [2, 3], [4, 4]]
    >>> count_same(pairs)
    2
    """
    same_count = 0
    for x, y in pairs:
        if x == y:
            same_count = same_count + 1
    return same_count


# Диапазоны

list(range(5, 8))
list(range(4))
len(range(4))

def sum_below(n):
    total = 0
    for i in range(n):
        total += i
    return total

def cheer():
    for _ in range(3):
        print('Вперёд!')


# Списковые включения

odds = [1, 3, 5, 7, 9]
[x+1 for x in odds]
[x for x in odds if 25 % x == 0]

def divisors(n):
    """Возвращает список целых, которые делят n нацело.

    >>> divisors(1)
    [1]
    >>> divisors(4)
    [1, 2]
    >>> divisors(12)
    [1, 2, 3, 4, 6]
    >>> [n for n in range(1, 1000) if sum(divisors(n)) == n]
    [1, 6, 28, 496]
    """
    return [1] + [x for x in range(2, n) if n % x == 0]


# Функции высшего порядка

from operator import add, mul

def apply_to_all(map_fn, s):
    """Применяет map_fn к каждому элементу s.

    >>> apply_to_all(lambda x: x*3, range(5))
    [0, 3, 6, 9, 12]
    """
    return [map_fn(x) for x in s]

def keep_if(filter_fn, s):
    """Возвращает список элементов s для которых filter_fn(x) является истиной

    >>> keep_if(lambda x: x>5, range(10))
    [6, 7, 8, 9]
    """
    return [x for x in s if filter_fn(x)]

def reduce(reduce_fn, s, initial):
    """Попарно объединяет элементы s используя reduce_fn, начиная с initial.

    То есть, reduce(mul, [2, 4, 8], 1) эквивалентен mul(mul(mul(1, 2), 4), 8).

    >>> reduce(mul, [2, 4, 8], 1)
    64
    """
    reduced = initial
    for x in s:
        reduced = reduce_fn(reduced, x)
    return reduced

def divisors_of(n):
    divides_n = lambda x: n % x == 0
    return [1] + keep_if(divides_n, range(2, n))

def sum_of_divisors(n):
    return reduce(add, divisors_of(n), 0)

def perfect(n):
    """Проверяет, что n совершенное число.

    >>> keep_if(perfect, range(1, 1000))
    [1, 6, 28, 496]
    """
    return sum_of_divisors(n) == n

# Словари

def dict_demos():
    numerals = {'I': 1.0, 'V': 5, 'X': 10}
    numerals['X']
    numerals.values()
    list(numerals.values())
    sum(numerals.values())
    dict([(3, 9), (4, 16), (5, 25)])
    numerals.get('A', 0)
    numerals.get('V', 0)
    {x: x*x for x in range(3,6)}

    {1: 2, 1: 3}
    {[1]: 2}
    {1: [2]}