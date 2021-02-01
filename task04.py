#!/usr/bin/env python

def main():
    var = int(input('Enter a number:\n'))
    max = var % 10

    while var >= 10:
        digit = var % 10
        max = max if max > digit else digit
        var = var // 10

    max = max if max > var else var

    print(f'Maximum digit: {max}')

# Alternative way
# def main():
#     var = input('Please enter a number:\n')
#
#     if int(var) < 0:
#         print('Number should be greater than 0')
#     else:
#         max = int(var[0])
#         for digit in var:
#             tmp = int(digit)
#             max = tmp if tmp > max else max
#
#     print(f'Maximum digit: {max}')


if __name__ == '__main__':
    main()
