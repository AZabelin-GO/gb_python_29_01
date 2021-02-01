#!/usr/bin/env python

def main():
    first_result = int(input('Enter runner result of first day:\n'))
    target_result = int(input('Enter runner target result:\n'))
    tmp = first_result * 1.1
    day_number = 2
    while tmp < target_result:
        tmp = tmp * 1.1
        day_number += 1

    print(f'Target result will be achieved on {day_number} day')


if __name__ == '__main__':
    main()
