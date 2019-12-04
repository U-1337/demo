# Списки

def lists():
    """Изменение списков.

    >>> t = [1, 2, 3]
    >>> t[1:3] = [t]
    >>> t.extend(t)
    >>> t
    [1, [...], 1, [...]]

    >>> t = [[1, 2], [3, 4]]
    >>> t[0].append(t[1:2])
    >>> t
    [[1, 2, [[3, 4]]], [3, 4]]
    """

# Работа

class Worker:
    greeting = 'Сэр'
    def __init__(self):
        self.elf = Worker
    def work(self):
        return self.greeting + ', я работаю'
    def __repr__(self):
        return Bourgeoisie.greeting

class Bourgeoisie(Worker):
    greeting = 'Работник'
    def work(self):
        print(Worker.work(self))
        return 'Я богатею'

jack = Worker()
john = Bourgeoisie()
jack.greeting = 'Мэм'

def work():
    """Working.

    >>> Worker().work()
    'Cэр, я работаю'
    >>> jack
    'Работник'
    >>> jack.work()
    'Мэм, я работаю'
    >>> john.work()
    Работник, я работаю
    'Я богатею'
    >>> john.elf.work(john)
    'Работник, я работаю'
    """

# Циклы

def cycle_demo():
    """Связный список может содержать циклы.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.first = 5
    >>> t = s.rest
    >>> t.rest = s
    >>> s.first
    5
    >>> s.rest.rest.rest.rest.rest.first
    2
    """


# Дерево Морзе

abcde = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.'}

def morse(code):
    """Возвращает дерево представляющее код. За исключением корня
    каждый узел (не лист) дерева представляет сигнал, каждый лист —
    закодированную букву (код буквы — путь от корня до листа).

    >>> pretty(morse(abcde))
       None
     /    \
     .    -
    / \   |
    - e   .
    |    /  \
    a    .  -
        / \ |
        . d .
        |   |
        b   c
    """
    whole = Tree(None)
    for letter, signals in sorted(code.items()):
        t = whole
        for s in signals:
            if s in [b.label for b in t.branches]:
                t = [b for b in t.branches if b.label == s][0]
            else:
                b = Tree(s)
                t.branches.append(b)
                t = b
        t.branches.append(Tree(letter))
    return whole

def decode(signals, tree):
    """Раскодирование сигналов в букву с помощью дерева в предположении, что код
    корректный. Формат дерева tree такой же как в функции morse().

    >>> t = morse(abcde)
    >>> [decode(s, t) for s in ['-..', '.', '-.-.', '.-', '-..', '.']]
    ['d', 'e', 'c', 'a', 'd', 'e']
    """
    for signal in signals:
        tree = [b for b in tree.branches if b.label == signal][0]
    leaves = [b for b in tree.branches if b.is_leaf()]
    assert len(leaves) == 1
    return leaves[0].label

# Связный список List и дерево Tree
class Link:
    """Связный список."""
    empty=()
    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest

class Tree:
    """Дерево."""
    def __init__(self, label, branches=()):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(repr(self.label), branch_str)

    def __str__(self):
        return '\n'.join(self.indented())

    def indented(self):
        lines = []
        for b in self.branches:
            for line in b.indented():
                lines.append('  ' + line)
        return [str(self.label)] + lines

    def is_leaf(self):
        return not self.branches

from io import StringIO
# StringIO — это файлоподобный объект, который создаёт строку вместо вывода текста в файл.

def height(tree):
    """Вычисление высоты дерева."""
    if tree.is_leaf():
        return 0
    else:
        return 1 + max([height(b) for b in tree.branches])

def width(tree):
    """Возвращает ширину, которую займет дерево при распечатке."""
    label_width = len(str(tree.label))
    w = max(label_width,
            sum([width(t) for t in tree.branches]) + len(tree.branches) - 1)
    extra = (w - label_width) % 2
    return w + extra

def pretty(tree):
    """Печатает красивое дерево."""

    def gen_levels(tr):
        w = width(tr)
        label = str(tr.label)
        label_pad = " " * ((w - len(label)) // 2)
        yield w
        print(label_pad, file=out, end="")
        print(label, file=out, end="")
        print(label_pad, file=out, end="")
        yield

        if tr.is_leaf():
            pad = " " * w
            while True:
                print(pad, file=out, end="")
                yield
        below = [ gen_levels(b) for b in tr.branches ]
        L = 0
        for g in below:
            if L > 0:
                print(" ", end="", file=out)
                L += 1
            w1 = next(g)
            left = (w1-1) // 2
            right = w1 - left - 1
            mid = L + left
            print(" " * left, end="", file=out)
            if mid*2 + 1 == w:
                print("|", end="", file=out)
            elif mid*2 > w:
                print("\\", end="", file=out)
            else:
                print("/", end="", file=out)
            print(" " * right, end="", file=out)
            L += w1
        print(" " * (w - L), end="", file=out)
        yield
        while True:
            started = False
            for g in below:
                if started:
                    print(" ", end="", file=out)
                next(g);
                started = True
            print(" " * (w - L), end="", file=out)
            yield

    out = StringIO()
    h = height(tree)
    g = gen_levels(tree)
    next(g)
    for i in range(2*h + 1):
        next(g)
        print(file=out)
    print(out.getvalue(), end="")

rus = {
    'а': '.-',
    'б': '-...',
    'в': '.--',
    'г': '--.',
    'д': '-..',
    'е': '.',
    'ж': '...-',
    'з': '--..',
    'и': '..',
    'й': '.----',
    'к': '-.-',
    'л': '.-..',
    'м': '--',
    'н': '-.',
    'о': '---',
    'п': '.--.',
    'р': '.-.',
    'с': '...',
    'т': '-',
    'у': '..-',
    'ф': '..-.',
    'х': '....',
    'ц': '-.-.',
    'ч': '---.',
    'ш': '----',
    'щ': '--.-',
    'ъ': '--.--',
    'ы': '-.--',
    'ь': '-..-',
    'э': '..-..',
    'ю': '..--',
    'я': '.-.-'
    }