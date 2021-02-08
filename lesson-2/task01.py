#!/usr/bin/env python

"""
Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого
элемента. Использовать функцию ​type() для проверки типа. Элементы списка можно не запрашивать у пользователя,
а указать явно, в программе.
"""

array = [
    1,
    1.0,
    complex(1, 2),
    "string",
    [1, 2, 3, 4, 5],
    {"a": 1, "b": 2, "c": 3},
    (1, 2, 3, 4, 5),
    set("12345"),
    frozenset("12345"),
    True,
    bytes("bytes", encoding="utf-8"),
    bytearray(b"bytearray"),
    None,
    Exception("My exception")
]


def main():
    for var in array:
        print(f"Element: {var}; Element_type: {type(var)}")


if __name__ == '__main__':
    main()
