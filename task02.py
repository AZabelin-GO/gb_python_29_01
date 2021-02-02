#!/usr/bin/env python

"""
Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""


def main():
    var = int(input('Enter current time in seconds:\n'))
    hours, tmp = var // 3600, var % 3600
    minutes, seconds = tmp // 60, tmp % 60

    print(f'{hours:02d}:{minutes:02d}:{seconds:02d}')


if __name__ == '__main__':
    main()
