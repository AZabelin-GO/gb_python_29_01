#!/usr/bin/env python

import argparse

"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения расчета для
конкретных значений необходимо запускать скрипт с параметрами.
"""


def calculate_salary(working_hours, rate, bonus):
    print(f"Calculated salary: {working_hours * rate + bonus}")


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(description="Script for calculating salary for employee", add_help=True)
    arg_parser.add_argument("--hours", type=int, required=True, help="Amount of working hours")
    arg_parser.add_argument("--rate", type=int, required=True, help="Payment per hour")
    arg_parser.add_argument("--bonus", type=int, required=True, help="Bonus for good work")
    args = arg_parser.parse_args()

    calculate_salary(args.hours, args.rate, args.bonus)
