#!/usr/bin/env python

from functools import reduce

"""
Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти четные
числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов списка.

Подсказка: использовать функцию reduce().
"""

numbers = [x for x in range(100, 1001) if x % 2 == 0]


def main():
    print(f"Original list: {numbers}")
    multiply_result = reduce(lambda x, y: x * y, numbers)
    print(f"Result: {multiply_result}")


if __name__ == '__main__':
    main()
