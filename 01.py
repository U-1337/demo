# Численные выражения
2019
2000 + 19
0 + 1 // 2 + 3 + 4 * ((5 // 6) + 7 * 8 * 9)

# Вызывающие выражения
max(7.5, 9.5)
pow(100, 2)
pow(2, 100)
max(1, -2, 3, -4)
max(min(1, -2), min(pow(3, 5), -4))

# Импорт и вызывающие выражения арифметических операторов
# Нельзя же выполнить +(1, 2)
from operator import add, mul
add(2, 3)
mul(2, 3)
mul(add(2, mul(4, 6)), add(3, 5))

from math import sqrt
sqrt(169)

# Объекты
# Указание: Скачай текст из http://composingprograms.com/shakespeare.txt
shakes = open('shakespeare.txt')
text = shakes.read().split()
text[:25]
len(text)
text.count('the')
text.count('you')
text.count(',')
text.count(',') / len(text)

# Множества
words = set(text)
'the' in words
len(words)
max(words)
max(words, key=len)

# Комбинации
'draw'[::-1]
{w for w in words if w == w[::-1] and len(w)>4}
{w for w in words if w[::-1] in words and len(w) == 4}
{w for w in words if w[::-1] in words and len(w) > 6}

max(words, key=lambda x: sum([1 for w in x if w in 'aeiou']))
max(words, key=lambda x: x.count('e'))
max(words, key=lambda x: x.count('x'))
max([[max(words, key=lambda x: x.count(i))] for i in 'abcdefghijklmnopqrstuvvwxyzABCDEFGHIJKLMNOPQRSTUV'], key=len)

max(words, key=lambda x: x.count('a'))