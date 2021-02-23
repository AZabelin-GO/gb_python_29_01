#!/usr/bin/env python

from functools import reduce

"""
Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. При вызове функции
должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n). Функция отвечает за
получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""


def calculate_factorial(n):
    if n in [0, 1]:
        return 1
    else:
        return reduce(lambda x, y: x * y, list(range(1, n + 1)))


def factorial_generator(n):
    if n > 1:
        for i in range(1, n + 1):
            yield calculate_factorial(i)
    else:
        return calculate_factorial(n)


def main():
    for i, j in enumerate(factorial_generator(6), 1):
        print(f"{i}! = {j}")


if __name__ == '__main__':
    main()
