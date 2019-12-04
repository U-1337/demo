##################
# Связные списки #
##################

empty = 'empty'

def is_link(s):
    """s -- это связный список если он пуст или является парой (first, rest)."""
    return s == empty or (type(s) == list and len(s) == 2 and is_link(s[1]))

def link(first, rest):
    """Создает связный список из первого элемента (first) и остальных (rest)."""
    assert is_link(rest), "rest должен быть связным списком."
    return [first, rest]

def first(s):
    """Возвращает первый элемент связного списка s."""
    assert is_link(s), "first применяется только к связным спискам."
    assert s != empty, "пустой связный список не имеет первого элемента."
    return s[0]

def rest(s):
    """Возвращает остальные элементы связного списка s."""
    assert is_link(s), "rest рименяется только к связным спискам."
    assert s != empty, "пустой связный список не имеет первого элемента."
    return s[1]

### +++ === ГРАНИЦА АБСТРАКЦИИ === +++ ###

# Примеры рекурсивных списков

four = link(1, link(2, link(3, link(4, empty))))
march = link(1, link(2, link(1, link(2, empty))))
both = link(march, link(four, empty))

# Какое из этих выражений имеет значение 3?
# first(rest(rest(first(rest(both)))))
# first(rest(first(rest(rest(both)))))
# first(rest(first(rest(first(both)))))
# first(rest(rest(rest(first(both)))))
# first(first(rest(rest(first(both)))))


# Реализация абстракции последовательности

def len_link(s):
    """Возвращает длину связного списка s.

    >>> len_link(four)
    4
    >>> len_link(both)
    2
    """
    length = 0
    while s != empty:
        s, length = rest(s), length + 1
    return length

def getitem_link(s, i):
    """Возвращает i-ый элемент связного списка s.

    >>> getitem_link(march, 3)
    2
    """
    while i > 0:
        s, i = rest(s), i - 1
    return first(s)


# Рекурсивная реализация

def len_link_recursive(s):
    """Возвращает длину связного списка s."""
    if s == empty:
        return 0
    return 1 + len_link_recursive(rest(s))

def getitem_link_recursive(s, i):
    """Возвращает i-ый элемент связного списка s."""
    if i == 0:
        return first(s)
    return getitem_link_recursive(rest(s), i - 1)


# Обработка связных списков

def extend(s, t):
    """Возвращает объединение элементов списков s и t."""
    assert is_link(s) and is_link(t)
    if s == empty:
        return t
    else:
        return link(first(s), extend(rest(s), t))

def reverse(s):
    """Возвращает обращенный s.

    >>> r = link(4, link(3, link(2, link(1, empty))))
    >>> reverse(four) == r
    True
    """
    return reverse_to(s, empty)

def reverse_to(s, result):
    if s == empty:
        return result
    else:
        return reverse_to(rest(s), link(first(s), result))

def apply_to_all_link(f, s):
    """Применяет f к каждому элементу s.

    >>> apply_to_all_link(lambda x: x*x, four)
    [1, [4, [9, [16, 'empty']]]]
    """
    assert is_link(s)
    if s == empty:
        return s
    else:
        return link(f(first(s)), apply_to_all_link(f, rest(s)))


# Разбиения чисел

def partitions(n, m):
    """Возвращает связный список разбиений n на части непревосходящие m.
    Каждое разбиение представляется связным списком.
    """
    if n == 0:
        return link(empty, empty) # Список, содержащий пустое разбиение
    elif n < 0:
        return empty
    elif m == 0:
        return empty
    else:
        # Используется хотя бы одно m?
        yes = partitions(n-m, m)
        no = partitions(n, m-1)
        add_m = lambda s: link(m, s)
        yes = apply_to_all_link(add_m, yes)
        return extend(yes, no)

def join(s, separator):
    """Возвращает строку из всех элементов s, разделенных разделителем separator.

    >>> join(four, ", ")
    '1, 2, 3, 4'
    """
    if s == empty:
        return ""
    elif rest(s) == empty:
        return str(first(s))
    else:
        return str(first(s)) + separator + join(rest(s), separator)

def print_partitions(n, m):
    """Распечатывает список разбиений n, частями непревышающими m.

    >>> print_partitions(6, 4)
    4 + 2
    4 + 1 + 1
    3 + 3
    3 + 2 + 1
    3 + 1 + 1 + 1
    2 + 2 + 2
    2 + 2 + 1 + 1
    2 + 1 + 1 + 1 + 1
    1 + 1 + 1 + 1 + 1 + 1
    """
    lists = partitions(n, m)
    strings = apply_to_all_link(lambda s: join(s, " + "), lists)
    print(join(strings, "\n")) # с новой строки


####################
# Корневые деревья #
####################

def rooted(value, branches):
    for branch in branches:
        assert is_rooted(branch), 'ветви должны быть корневыми деревьями'
    return [value] + list(branches)

def root(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_rooted(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_rooted(branch):
            return False
    return True

### +++ === ГРАНИЦА АБСТРАКЦИИ === +++ ###

def fib_tree(n):
    """Возвращает дерево Фибоначчи.

    >>> fib_tree(5)
    [5, [2, [1], [1, [0], [1]]], [3, [1, [0], [1]], [2, [1], [1, [0], [1]]]]]
    """
    if n == 0 or n == 1:
        return rooted(n, [])
    else:
        left, right = fib_tree(n-2), fib_tree(n-1)
        root_value = root(left) + root(right)
        return rooted(root_value, [left, right])

def partition_tree(n, m):
    """Возвращает дерево разбиений n, используя части непревышающие m.

    >>> partition_tree(2, 2)
    [2, [True], [1, [1, [True], [False]], [False]]]
    """
    if n == 0:
        return rooted(True, [])
    elif n < 0:
        return rooted(False, [])
    elif m == 0:
        return rooted(False, [])
    else:
        left = partition_tree(n-m, m)
        right = partition_tree(n, m-1)
        return rooted(m, [left, right])


def print_parts(tree, partition=empty):
    """Распечатывает разбиения находящиеся в дереве разбиений.

    >>> print_parts(partition_tree(6, 4))
    4 + 2
    4 + 1 + 1
    3 + 3
    3 + 2 + 1
    3 + 1 + 1 + 1
    2 + 2 + 2
    2 + 2 + 1 + 1
    2 + 1 + 1 + 1 + 1
    1 + 1 + 1 + 1 + 1 + 1
    """
    if not branches(tree) and root(tree):
        print(join(reverse(partition), ' + '))
    elif branches(tree):
        left, right = branches(tree)
        m = root(tree)
        print_parts(left, link(m, partition))
        print_parts(right, partition)

def string_encoding_demos():
    hex(ord('A'))
    print('\a')
    print('1\n2\n3')
    from unicodedata import lookup, name
    name('A')
    lookup('WHITE FROWNING FACE')
    lookup('SNOWMAN')
    lookup('SOCCER BALL')
    lookup('BABY')
    s = lookup('SNOWMAN')
    len('A')
    'A'.encode()
    len(frown)
    len(frown.encode())
    dir('')
    "привет".capitalize()
    "привет".upper()

