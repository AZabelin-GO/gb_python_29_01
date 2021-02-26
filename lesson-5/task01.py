#!/usr/bin/env python

"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""


def main():
    with open("task01.txt", "w") as t_file:
        while True:
            var = input("Enter a string (leave empty to exit):\n")
            if var:
                print(var, file=t_file)
            else:
                print("Bye!")
                break


if __name__ == '__main__':
    main()
