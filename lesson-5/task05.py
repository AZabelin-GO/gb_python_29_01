#!/usr/bin/env python

import random
from functools import reduce

"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

TEXT_FILE = "task05.txt"


def init_file(file_name):
    print(f"Creating file '{file_name}' with numbers...")
    print()
    lines_count = random.randint(1, 10)
    with open(file_name, "w") as t_file:
        for i in range(lines_count):
            numbers = [str(random.randint(1, 100)) for x in range(random.randint(1, 10))]
            print(" ".join(numbers), file=t_file)


def calculate_sum_in_file(file_name):
    try:
        with open(file_name, "r") as t_file:
            total_sum = 0
            for i, line in enumerate(t_file, 1):
                sum_in_line = sum([int(x) for x in line.strip().split()])
                total_sum += sum_in_line
                print(f"Line No {i}: '{line.strip()}'; sum '{sum_in_line}'")
            print()
            print(f"Total sum of numbers in file '{file_name}': {total_sum}")

    except FileNotFoundError:
        print(f"File '{TEXT_FILE}' not found")
        exit(1)


def main():
    init_file(TEXT_FILE)
    calculate_sum_in_file(TEXT_FILE)


if __name__ == '__main__':
    main()
