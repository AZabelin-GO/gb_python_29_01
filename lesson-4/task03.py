#!/usr/bin/env python

import random

"""
Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и генератор.
"""

numbers = [random.randint(20, 240) for i in range(10)]


def main():
    print(f"Original list: {numbers}")
    filtered_numbers = [x for x in numbers if (x % 20 == 0) or (x % 21 == 0)]
    print(f"Filtered list: {filtered_numbers}")


if __name__ == '__main__':
    main()
