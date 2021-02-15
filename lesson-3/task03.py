#!/usr/bin/env python

"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""

import random


def print_sum_of_two_max(a, b, c):
    t = [a, b, c]
    print(f"Numbers: {t}")
    t.sort(reverse=True)
    print(f"{t[0]} + {t[1]} = {t[0] + t[1]}")


def main():
    print_sum_of_two_max(random.randint(1, 10), random.randint(1, 10), random.randint(1, 10))


if __name__ == '__main__':
    main()
