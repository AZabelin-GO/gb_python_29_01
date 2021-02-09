#!/usr/bin/env python

"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом
и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
ранее сумме и после этого завершить программу.
"""


def read_numbers():
    sum = 0
    while True:
        print(f"Current sum = {sum}")
        str = input("Enter numbers (use 'q/Q' to exit):\n")
        if str:
            for n in str.split():
                try:
                    sum += int(n)
                except ValueError:
                    if n in ["q", "Q"]:
                        print(f"Current sum = {sum}")
                        exit(1)
                    else:
                        print(f"Failed to convert {n} to number")
                        continue
        else:
            print(f"Current sum = {sum}")
            exit(0)


def main():
    read_numbers()


if __name__ == '__main__':
    main()
