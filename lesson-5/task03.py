#!/usr/bin/env python

"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

TEXT_FILE = "task03.txt"
WORKERS = []


def read_file(file_name):
    try:
        with open(file_name, "r") as t_file:
            for line in t_file:
                t = line.split(",")
                worker = {
                    "Last name": t[0],
                    "Salary": int(t[1])
                }
                WORKERS.append(worker)
    except FileNotFoundError:
        print(f"File '{TEXT_FILE}' not found")
        exit(1)


def calculate_statistic(workers):
    low_payed_workers = []
    avg_salary = 0
    for worker in workers:
        avg_salary += worker["Salary"]
        if worker["Salary"] < 20000:
            low_payed_workers.append(worker["Last name"])

    avg_salary = avg_salary / len(workers)

    print(f"Average salary: {avg_salary}")
    print(f"Worker with salary less than 20k: {low_payed_workers}")


def main():
    read_file(TEXT_FILE)
    calculate_statistic(WORKERS)


if __name__ == '__main__':
    main()
