#!/usr/bin/env python

"""
Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
"""


def read_array():
    str = input("Enter a string with words:\n")
    return str.strip().split()


def print_string_array(array):
    for k, v in enumerate(array, 1):
        print(f"{k}) {v:.10}")


def main():
    array = read_array()
    print_string_array(array)


if __name__ == '__main__':
    main()
