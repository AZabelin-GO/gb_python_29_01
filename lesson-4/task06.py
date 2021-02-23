#!/usr/bin/env python

import random
from helpers import task06_lib

"""
Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.

Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не должен
быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл. Во втором также
необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""


def learn_limited_generator(start_number):
    print(f"Learning limited generators with start value '{start_number}'")
    my_limited_generator = task06_lib.integer_generator_limited(start_number)
    for i in range(10):
        try:
            print(f"Generator value: {next(my_limited_generator)}")
        except StopIteration:
            print("Generator reached the limit")
            break


def learn_cycle_generator(max_loops):
    print(f"Learning cycled generator with maximum cycles '{max_loops}'")
    my_cycle_generator = task06_lib.integer_generator_cycled(max_loops)
    while True:
        try:
            print(f"Generator value: {next(my_cycle_generator)}")
        except StopIteration:
            print("Cycled generator reached maximum loops")
            break


def main():
    learn_limited_generator(random.randint(1, 10))
    learn_cycle_generator(random.randint(1, 10))


if __name__ == '__main__':
    main()
