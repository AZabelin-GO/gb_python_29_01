#!/usr/bin/env python

import random

"""
Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.

Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].

Результат: [12, 44, 4, 10, 78, 123].
"""

numbers = [random.randint(1, 10) for x in range(10)]


def main():
    print(f"Original list: {numbers}")
    filtered_numbers = [numbers[i + 1] for i in range(len(numbers) - 1) if numbers[i] < numbers[i + 1]]
    print(f"Filtered list: {filtered_numbers}")


if __name__ == '__main__':
    main()
