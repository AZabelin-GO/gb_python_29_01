#!/usr/bin/env python

"""
Спортсмен занимается ежедневными пробежками. В первый день его результат составил ​a километров.
Каждый день спортсмен увеличивал результат на 10% относительно предыдущего.
Требуется определить номер дня, на который результат спортсмена составит не менее ​b километров.
Программа должна принимать значения параметров ​a ​и ​b ​и выводить одно натуральное число ​—​ номер дня.
Например: a = 2, b = 3. Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22
Ответ: на шестой день спортсмен достиг результата ​—​ не менее 3 км.
"""


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
