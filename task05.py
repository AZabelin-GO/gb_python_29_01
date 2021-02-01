#!/usr/bin/env python

def main():
    profit = int(input('Enter profit:\n'))
    costs = int(input('Enter costs:\n'))

    total = profit - costs

    if total > 0:
        print(f'Your company is profitable, it earned: {total}')
        print(f'Profitability: {profit / costs * 100}%')
        workers_count = int(input('Enter number of workers in company:\n'))
        print(f'Profitability per worker: {total / workers_count}')
    elif total == 0:
        print(f'Your company is balanced, it didn\'t earned anything')
    else:
        print(f'Your company is NOT profitable, it spent: {total}')


if __name__ == '__main__':
    main()
