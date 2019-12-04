# Суммирование цифр

def split(n):
    """Выделяет из n последнюю цифру и то, что осталось."""
    return n // 10, n % 10

def sum_digits(n):
    """Возвращает сумму всех цифр положительного целого n.

    >>> sum_digits(9)
    9
    >>> sum_digits(18117)
    18
    >>> sum_digits(9437184)
    36
    >>> sum_digits(11408855402054064613470328848384)
    126
    """
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return sum_digits(all_but_last) + last

# Сравнение итерация и рекурсии

def fact_iter(n):
    total, k = 1, 1
    while k <= n:
        total, k = total * k, k + 1
    return total

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

# Алгоритм Луна --  взаимная рекурсия

def luhn_sum(n):
    """Возвращает сумму цифр n, вычисленную по алгоритму Луна.

    >>> luhn_sum(2)
    2
    >>> luhn_sum(12)
    4
    >>> luhn_sum(42)
    10
    >>> luhn_sum(138743)
    30
    >>> luhn_sum(5105105105105100) # например Mastercard
    20
    >>> luhn_sum(4012888888881881) # например Visa
    90
    >>> luhn_sum(79927398713) # из википедии
    70
    """
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return luhn_sum_double(all_but_last) + last

def luhn_sum_double(n):
    """Возвращает сумму Луна для n, удваивая последнюю цифру."""
    all_but_last, last = split(n)
    luhn_digit = sum_digits(2 * last)
    if n < 10:
        return luhn_digit
    else:
        return luhn_sum(all_but_last) + luhn_digit

# Перевод итерации в рекурсию

def sum_digits_iter(n):
    """Итеративное сложение цифр.

    >>> sum_digits_iter(11408855402054064613470328848384)
    126
    """
    digit_sum = 0
    while n > 0:
        n, last = split(n)
        digit_sum = digit_sum + last
    return digit_sum

def sum_digits_rec(n, digit_sum):
    """Сложение цифр n с использованием рекурсии, базируется на итеративной версии.

    >>> sum_digits_rec(11408855402054064613470328848384, 0)
    126
    """
    if n == 0:
        return digit_sum
    else:
        n, last = split(n)
        return sum_digits_rec(n, digit_sum + last)