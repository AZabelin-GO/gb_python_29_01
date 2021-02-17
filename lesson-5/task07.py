#!/usr/bin/env python

import json

"""
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
форма собственности, выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
убытки, в расчет средней прибыли ее не включать.

Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.

Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""

TEXT_FILE = "task07.txt"
NEW_FILE = "task07_stat.json"


def init_file(file_name):
    with open(file_name, "w") as t_file:
        while True:
            var = input("Enter a string (example: 'firm_1 ООО 10000 5000.'; leave empty to exit):\n")
            if var:
                print(var, file=t_file)
            else:
                print("Empty string. Stop reading input.")
                break


def read_file(file_name):
    data = []
    try:
        with open(file_name, "r") as t_file:
            for line in t_file:
                chunks = line.strip(".").split()
                company_name = chunks[0]
                try:
                    revenue = int(chunks[2])
                    costs = int(chunks[3])
                    profit = revenue - costs
                except ValueError:
                    print(f"Failed to parse data from string '{line}'")
                    continue
                data.append({
                    "Company name": company_name,
                    "Profit": profit
                })
    except FileNotFoundError:
        print(f"File '{TEXT_FILE}' not found")
        exit(1)

    return data


def calculate_statistic(data):
    avg_profit = 0
    statistic = [{}]
    for x in data:
        statistic[0].update({
            x['Company name']: x['Profit']
        })
        if x["Profit"] > 0:
            avg_profit += x["Profit"]
        else:
            print(f"Company \'{x['Company name']}\' is not profitable (loss \'{x['Profit']}\')")

    avg_profit = avg_profit / len(data)
    statistic.append({"average_profit": avg_profit})

    return statistic


def print_statistic(statistic):
    print("Statistic:")
    print("[")
    for i in range(len(statistic) - 1):
        print(f"    {statistic[i]},")
    print(f"    {statistic[-1]}")
    print("]")


def save_statistic(file_name, statistic):
    with open(file_name, "w") as file:
        print(json.dumps(statistic, indent=2), file=file)


def main():
    init_file(TEXT_FILE)
    data = read_file(TEXT_FILE)
    statistic = calculate_statistic(data)
    print_statistic(statistic)
    save_statistic(NEW_FILE, statistic)


if __name__ == '__main__':
    main()
