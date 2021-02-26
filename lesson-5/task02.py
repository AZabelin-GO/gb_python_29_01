#!/usr/bin/env python

"""
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""

TEXT_FILE = "task01.txt"


def main():
    try:
        with open(TEXT_FILE, "r") as t_file:
            print(f"File '{TEXT_FILE}':")
            for i, line in enumerate(t_file, 1):
                print(f"In line #{i} '{len(line.split())}' word(s)")
            print(f"Total lines: {i}")
    except FileNotFoundError:
        print(f"File '{TEXT_FILE}' not found")
        exit(1)


if __name__ == '__main__':
    main()
