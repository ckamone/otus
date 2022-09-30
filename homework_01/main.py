"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return list(map(lambda x: x ** 2, args))


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(num):
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            return False
    return num >= 2


def filter_numbers(seq, method):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if method == ODD:
        return list(filter(lambda x: x % 2 != 0, seq))
    elif method == EVEN:
        return list(filter(lambda x: x % 2 == 0, seq))
    elif method == PRIME:
        return list(filter(is_prime, seq))