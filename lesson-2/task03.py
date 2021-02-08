#!/usr/bin/env python

import random

"""
Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года
относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
"""

season_list = [
    "Winter",
    "Winter",
    "Spring",
    "Spring",
    "Spring",
    "Summer",
    "Summer",
    "Summer",
    "Autumn",
    "Autumn",
    "Autumn",
    "Winter"
]

season_dict = {
    "Winter": (1, 2, 12),
    "Spring": (3, 4, 5),
    "Summer": (6, 7, 8),
    "Autumn": (9, 10, 11)
}


def read_month():
    while True:
        var = input("Enter a month number (1-12):\n")
        if not var:
            print("Empty input. Bye.")
            exit(1)
        elif not var.isdigit():
            print(f"{var} is not a number")
            continue
        elif var.isdigit():
            if 1 <= int(var) <= 12:
                return int(var)
            else:
                print(f"Number should be in range [1 - 12], but got {var}")
                continue


def get_season_from_list(month):
    return season_list[month + 1]


def get_season_from_dict(month):
    for k in season_dict.keys():
        if month in season_dict[k]:
            season = k
            break

    return season


def main():
    month = read_month()
    if random.randint(1, 10) % 2 == 0:
        season = get_season_from_list(month)
    else:
        season = get_season_from_dict(month)
    print(f"Month '{month}' belongs to a season '{season}'")


if __name__ == '__main__':
    main()
