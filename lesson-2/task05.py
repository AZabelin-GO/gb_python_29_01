#!/usr/bin/env python

"""
Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы
с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
"""

import random


def init_array():
    array = [random.randint(1, 10) for x in range(1, 10)]
    array.sort(reverse=True)
    return array


def main():
    array = init_array()
    while True:
        print(f"Current ratings: {array}")
        var = input("Enter a rating number (leave empty to exit):\n")
        if var:
            if var.isdigit():
                array.append(int(var))
                array.sort(reverse=True)
            else:
                print(f"{var} is not a number")
                continue
        else:
            print("Empty input. Bye.")
            exit(0)


if __name__ == '__main__':
    main()
