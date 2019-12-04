def date_demos():
    from datetime import date
    today = date(2019, 10, 7)
    freedom = date(2015, 13, 12)
    str(freedom - today)
    today.year
    today.strftime('%A, %B %d')
    type(today)

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

def list_demos():
    suits = ['монеты', 'шнурки', 'мириады', 'десятки']  # Список строк
    original_suits = suits
    suits.pop()             # Выталкивает последний элемент
    suits.pop()
    suits.remove('шнурки')  # Удаляет первый элемент равный аргументу
    suits.append('кубки')              # Добавляет элемент в конец
    suits.extend(['мечи', 'трефы'])    # Добавляет все элементы в конец
    suits[2] = 'пики'  # Заменяет элемент
    suits
    suits[0:2] = ['червы', 'бубны']  # Заменяет срез
    [suit.upper() for suit in suits]
    [suit[1:4] for suit in suits if len(suit) == 5]

def dict_demos():
    numerals = {'I': 1.0, 'V': 5, 'X': 10}
    numerals['X']
    numerals['I'] = 1
    numerals['L'] = 50
    numerals
    sum(numerals.values())
    dict([(3, 9), (4, 16), (5, 25)])
    numerals.get('A', 0)
    numerals.get('V', 0)

def tuple_demos():
    (3, 4, 5, 6)
    3, 4, 5, 6
    ()
    tuple()
    tuple([1, 2, 3])
    # tuple(2)
    (2,)
    (3, 4) + (5, 6)
    (3, 4, 5) * 2
    5 in (3, 4, 5)

    # {[1]: 2}
    {1: [2]}
    {(1, 2): 3}
    # {([1], 2): 3}
    {tuple([1, 2]): 3}

def divide_exact(n, d):
    return n // d, n % d

def identity_demos():
    a = [10]
    b = a
    a == b
    a is b
    a.extend([20, 30])
    a == b
    a is b
    
    a = [10]
    b = [10]
    a == b
    a is not b
    a.append(20)
    a != b