#!/usr/bin/env python

"""
Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма.
Например, прибыль ​— выручка больше издержек, или убыток ​—​ издержки больше выручки.
Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки.
Это отношение прибыли к выручке. Далее запросите численность сотрудников фирмы и определите прибыль фирмы
в расчёте на одного сотрудника.
"""


def main():
    profit = int(input('Enter profit:\n'))
    costs = int(input('Enter costs:\n'))

    total = profit - costs

    if total > 0:
        print(f'Your company is profitable, it earned: {total}')
        print(f'Profitability: {total / costs * 100}%')
        workers_count = int(input('Enter number of workers in company:\n'))
        print(f'Profitability per worker: {total / workers_count}')
    elif total == 0:
        print(f'Your company is balanced, it didn\'t earned or spent anything')
    else:
        print(f'Your company is NOT profitable, it spent: {total}')


if __name__ == '__main__':
    main()
