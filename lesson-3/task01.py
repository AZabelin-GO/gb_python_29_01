#!/usr/bin/env python

"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def read_number():
    while True:
        var = input("Enter a number:\n")
        if var:
            if var.isdigit():
                return int(var)
            else:
                print(f"{var} is not a number")
                continue
        else:
            print("Empty input")
            return None


def division(a, b):
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: division by zero")
    return result


def main():
    var_a = read_number()
    if var_a is None:
        exit(0)

    var_b = read_number()
    if var_b is None:
        exit(0)

    res = division(var_a, var_b)
    if res is not None:
        print(f"{var_a} / {var_b} = {res}")


if __name__ == '__main__':
    main()
