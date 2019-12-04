"""Модуль scheme_tokens предоставляет функции tokenize_line и tokenize_lines
для преобразования строк в спискитокенов. Токен может быть:

  * Числом (представленным типами int или float)
  * Булевой величиной (представленной типом bool)
  * Символом (представленным типом string)
  * Разделителем (скобки, точки и одиночные кавычки)
"""

import string
import sys

_SYMBOL_STARTS = set('!$%&*/:<=>?@^_~') | set(string.ascii_lowercase)
_SYMBOL_INNERS = _SYMBOL_STARTS | set(string.digits) | set('+-.')
_NUMERAL_STARTS = set(string.digits) | set('+-.')
_WHITESPACE = set(' \t\n\r')
_SINGLE_CHAR_TOKENS = set("()'")
_TOKEN_END = _WHITESPACE | _SINGLE_CHAR_TOKENS
DELIMITERS = _SINGLE_CHAR_TOKENS | {'.'}

def valid_symbol(s):
    """Проверяет, что s правильный символ."""
    if len(s) == 0 or s[0] not in _SYMBOL_STARTS:
        return False
    for c in s[1:]:
        if c not in _SYMBOL_INNERS:
            return False
    return True

def next_candidate_token(line, k):
    """Тапл (tok, k'), где tok следующая подстрока строки в позиции k, которая
    может быть токеном (предполагая, что она проходит проверку), а k' --
    это позиция в строке следующая за токеном.  Возвращает
    (None, len(line)), если токенов больше не осталось."""
    while k < len(line):
        c = line[k]
        if c == ';':
            return None, len(line)
        elif c in _WHITESPACE:
            k += 1
        elif c in _SINGLE_CHAR_TOKENS:
            return c, k+1
        elif c == '#':  # Булевы величины #t и #f
            return line[k:k+2], min(k+2, len(line))
        else:
            j = k
            while j < len(line) and line[j] not in _TOKEN_END:
                j += 1
            return line[k:j], min(j, len(line))
    return None, len(line)

def tokenize_line(line):
    """Scheme-список токенов в строке.  Исключает комментарии и пробелы."""
    result = []
    text, i = next_candidate_token(line, 0)
    while text is not None:
        if text in DELIMITERS:
            result.append(text)
        elif text == '+' or text == '-':
            result.append(text)
        elif text == '#t' or text.lower() == 'true':
            result.append(True)
        elif text == '#f' or text.lower() == 'false':
            result.append(False)
        elif text == 'nil':
            result.append(text)
        elif text[0] in _NUMERAL_STARTS:
            try:
                result.append(int(text))
            except ValueError:
                try:
                    result.append(float(text))
                except ValueError:
                    raise ValueError("неправильное числительное: {0}".format(text))
        elif text[0] in _SYMBOL_STARTS and valid_symbol(text):
            result.append(text)
        else:
            print("предупреждение: неправильный токен: {0}".format(text), file=sys.stderr)
            print("    ", line, file=sys.stderr)
            print(" " * (i+3), "^", file=sys.stderr)
        text, i = next_candidate_token(line, i)
    return result

def tokenize_lines(input):
    """Итератор по списку токенов; один результат для каждой строки
    итерируемой входной последовательности."""
    return map(tokenize_line, input)
