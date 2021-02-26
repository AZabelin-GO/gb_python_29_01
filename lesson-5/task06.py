#!/usr/bin/env python

import re

"""
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.

Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

TEXT_FILE = "task06.txt"


def init_file(file_name):
    with open(file_name, "w") as t_file:
        while True:
            var = input("Enter a string (example: 'Информатика: 100(л) 50(пр) 20(лаб)'; leave empty to exit):\n")
            if var:
                print(var, file=t_file)
            else:
                print("Empty string. Stop reading input.")
                break


def calculate_statistic(file_name):
    statistics_dict = {}
    try:
        with open(file_name, "r") as t_file:
            for line in t_file:
                chunks = re.sub("\([^0-9]{1,}\)|([:.,—-])", "", line.strip()).split()
                course_name = chunks[0]
                course_hours = sum([int(chunks[i]) for i in range(1, len(chunks))])
                statistics_dict.update({
                    course_name: course_hours
                })
        print("Statistic for courses:")
        print(statistics_dict)
    except FileNotFoundError:
        print(f"File '{TEXT_FILE}' not found")
        exit(1)


def main():
    init_file(TEXT_FILE)
    calculate_statistic(TEXT_FILE)


if __name__ == '__main__':
    main()
