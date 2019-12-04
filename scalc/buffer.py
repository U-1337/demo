"""Модуль buffer помогает при итерировании по строкам и токенам."""

import math

class Buffer(object):
    """Класс Buffer предоставляет способ доступа к последовательностям токенов в строках.

    Его конструктор принимает итератор, называемый "source", который при запросе
    выдаёт следующую строку токенов в виде списка или None (индикация конца данных).

    Класс Buffer соединяет последовательности, полученные из source
    и выдает элементы из них (по очереди, один за раз) с помощью метода pop(),
    загружая последовательности из source по мере необходимости.

    В дополнение, Buffer предоставляет метод для получения
    следующего элемента без запроса всей последовательности.

    Метод __str__ выводит все токены считаные до текущего момента (до конца текущей)
    строки, помечая текущий токен с помощью >>.

    >>> buf = Buffer(iter([['(', '+'], [15], [12, ')']]))
    >>> buf.pop()
    '('
    >>> buf.pop()
    '+'
    >>> buf.current()
    15
    >>> print(buf)
    1: ( +
    2:  >> 15
    >>> buf.pop()
    15
    >>> buf.current()
    12
    >>> buf.pop()
    12
    >>> print(buf)
    1: ( +
    2: 15
    3: 12 >> )
    >>> buf.pop()
    ')'
    >>> print(buf)
    1: ( +
    2: 15
    3: 12 ) >>
    >>> buf.pop()  # возвращает None
    """
    def __init__(self, source):
        self.index = 0
        self.lines = []
        self.source = source
        self.current_line = ()
        self.current()

    def pop(self):
        """Удаляет следующий элемент и возвращает его.
        Если достигнут конец, возвращает None.
        """
        current = self.current()
        self.index += 1
        return current

    @property
    def more_on_line(self):
        return self.index < len(self.current_line)

    def current(self):
        """Возвращает текущий элемент или None (если конец)."""
        while not self.more_on_line:
            self.index = 0
            try:
                self.current_line = next(self.source)
                self.lines.append(self.current_line)
            except StopIteration:
                self.current_line = ()
                return None
        return self.current_line[self.index]

    def __str__(self):
        """Возвращает считанное; текущий элемент помечает с помощью >>."""
        # Форматирование строки для выравнивания номеров строк
        n = len(self.lines)
        msg = '{0:>' + str(math.floor(math.log10(n))+1) + "}: "

        # До трёх предыдущих строк + текущая строка
        s = ''
        for i in range(max(0, n-4), n-1):
            s += msg.format(i+1) + ' '.join(map(str, self.lines[i])) + '\n'
        s += msg.format(n)
        s += ' '.join(map(str, self.current_line[:self.index]))
        s += ' >> '
        s += ' '.join(map(str, self.current_line[self.index:]))
        return s.strip()

# Попытка импорта readline для интерактивной истории ввода
try:
    import readline
except:
    pass

class InputReader(object):
    """Класс InputReader -- итерируемый ввод пользователя."""
    def __init__(self, prompt):
        self.prompt = prompt

    def __iter__(self):
        while True:
            yield input(self.prompt)
            self.prompt = ' ' * len(self.prompt)
