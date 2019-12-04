from scheme_tokens import tokenize_lines, DELIMITERS
from buffer import Buffer, InputReader

# Пары и списки Scheme

class Pair(object):
    """Экземпляр пары имеет два атрибута: first (первый) и second (второй).
    Чтобы пара была форматным списком требуется, чтобы second был либо форматным
    списком, либо nil. Некоторые методы работают только с форматными списками.

    >>> s = Pair(1, Pair(2, nil))
    >>> s
    Pair(1, Pair(2, nil))
    >>> print(s)
    (1 2)
    >>> len(s)
    2
    >>> s[1]
    2
    >>> print(s.map(lambda x: x+4))
    (5 6)
    """
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __repr__(self):
        return "Pair({0}, {1})".format(repr(self.first), repr(self.second))

    def __str__(self):
        s = "(" + str(self.first)
        second = self.second
        while isinstance(second, Pair):
            s += " " + str(second.first)
            second = second.second
        if second is not nil:
            s += " . " + str(second)
        return s + ")"

    def __len__(self):
        n, second = 1, self.second
        while isinstance(second, Pair):
            n += 1
            second = second.second
        if second is not nil:
            raise TypeError("попытка вычислить длину неправильного списка")
        return n

    def __getitem__(self, k):
        if k < 0:
            raise IndexError("отрицательный индекс")
        y = self
        for _ in range(k):
            if y.second is nil:
                raise IndexError("индекс за пределами списка")
            elif not isinstance(y.second, Pair):
                raise TypeError("неправильный список")
            y = y.second
        return y.first

    def map(self, fn):
        """Возвращает список Scheme, содержащий результат fn(x) для каждого своего
        элемента x.
        """
        mapped = fn(self.first)
        if self.second is nil or isinstance(self.second, Pair):
            return Pair(mapped, self.second.map(fn))
        else:
            raise TypeError("неправильный список")

class nil(object):
    """Пустой список"""

    def __repr__(self):
        return "nil"

    def __str__(self):
        return "()"

    def __len__(self):
        return 0

    def __getitem__(self, k):
        if k < 0:
            raise IndexError("отрицательный индекс")
        raise IndexError("индекс за пределами списка")

    def map(self, fn):
        return self

nil = nil() # присвоение прячет класс nil; доступен только экземпляр


# Парсер Scheme-списков, без кавычек или неправильных списков.

def scheme_read(src):
    """Считывает следующее выражение из src (буфера токенов Buffer).

    >>> lines = ['(+ 1 ', '(+ 23 4)) (']
    >>> src = Buffer(tokenize_lines(lines))
    >>> print(scheme_read(src))
    (+ 1 (+ 23 4))
    """
    if src.current() is None:
        raise EOFError
    val = src.pop()
    if val == 'nil':
        return nil
    elif val not in DELIMITERS:  # ( ) ' .
        return val
    elif val == "(":
        return read_tail(src)
    else:
        raise SyntaxError("неожиданный токен: {0}".format(val))

def read_tail(src):
    """Возвращает остаток списка в src,
    начиная с элемента или со ).

    >>> read_tail(Buffer(tokenize_lines([')'])))
    nil
    >>> read_tail(Buffer(tokenize_lines(['2 3)'])))
    Pair(2, Pair(3, nil))
    >>> read_tail(Buffer(tokenize_lines(['2 (3 4))'])))
    Pair(2, Pair(Pair(3, Pair(4, nil)), nil))
    """
    if src.current() is None:
        raise SyntaxError("неожиданный конец файла")
    if src.current() == ")":
        src.pop()
        return nil
    first = scheme_read(src)
    rest = read_tail(src)
    return Pair(first, rest)


# Интерактивный цикл

def buffer_input():
    return Buffer(tokenize_lines(InputReader('> ')))

def read_print_loop():
    """Запускает интерактивный режим ввода выражений Scheme."""
    while True:
        try:
            src = buffer_input()
            while src.more_on_line:
                expression = scheme_read(src)
                print('Scheme:', expression)
                print('Python:', repr(expression))
        except (SyntaxError, ValueError) as err:
            print(type(err).__name__ + ':', err)
        except (KeyboardInterrupt, EOFError):  # <Control>-D, и т.д.
            return

if __name__ == "__main__":
    read_print_loop()

