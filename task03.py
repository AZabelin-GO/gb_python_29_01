#!/usr/bin/env python

"""
Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
Считаем 3 + 33 + 333 = 369.
"""


def main():
    var = input('Enter a number:\n')
    sum = int(var) + int(var * 2) + int(var * 3)
    print(f'{var} + {var * 2} + {var * 3} = {sum}')


if __name__ == '__main__':
    main()
