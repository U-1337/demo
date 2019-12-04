def assert_false():
    assert False, 'Ложь!'

def errors():
    abs('привет') # TypeError
    hello # NameError
    {}['привет'] # KeyError
    def f(): f()
    f() # RuntimeError

def invert(x):
    """Возвращает 1/x

    >>> invert(2)
    Не напечатается, если x равен 0
    0.5
    """
    result = 1/x  # Поднимает ZeroDivisionError, если x равен 0
    print('Не напечатается, если x равен 0')
    return result

def invert_safe(x):
    """Возвращает 1/x или строку 'division by zero', если x равен 0.

    >>> invert_safe(2)
    Не напечатается, если x равен 0
    0.5
    >>> invert_safe(0)
    'division by zero'
    """
    try:
        return invert(x)
    except ZeroDivisionError as e:
        return str(e)
