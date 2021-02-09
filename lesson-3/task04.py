#!/usr/bin/env python

"""
Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""


def read_numbers():
    a = input("Enter a number:\n")
    try:
        # Used int()
        a = int(a)
        if a <= 0:
            print(f"Expecting positive number; got {a}")
            exit(1)
    except ValueError:
        print(f"Failed to convert '{a}' to a number")
        exit(1)

    b = input("Enter a negative number:\n")
    try:
        b = int(b)
        if b >= 0:
            print(f"Expecting a negative number; got '{b}'")
            exit(1)
    except ValueError:
        print(f"Failed to convert '{b}' to a number")
        exit(1)

    return a, b


def my_func_1(x, y):
    return x ** y


def my_func_2(x, y):
    return pow(x, y)


def my_func_3(x, y):
    res = x
    print(f"res={res}")
    for i in range(1, abs(y)):
        res = res * x

    return 1 / res


def main():
    numbers = read_numbers()
    print(f"{numbers[0]} ** {numbers[1]} = {my_func_1(numbers[0], numbers[1])}")
    print(f"pow({numbers[0]}, {numbers[1]}) = {my_func_2(numbers[0], numbers[1])}")
    print(f"1 / ({numbers[0]} ** {numbers[1]}) [using loop] = {my_func_3(numbers[0], numbers[1])}")


if __name__ == '__main__':
    main()
