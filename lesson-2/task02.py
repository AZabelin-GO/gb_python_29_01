#!/usr/bin/env python

"""
Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы
с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""


def fill_array():
    array = []

    while True:
        var = input("Enter a number (leave empty to stop):\n")
        if not var:
            print(f"Array: {array}")
            break
        if var.isdigit():
            array.append(int(var))
        else:
            print(f"{var} is not number")

    return array


def swap_array_elements(array):
    array_swapped = []

    if len(array) % 2 == 0:
        max_array_index = len(array)
    else:
        max_array_index = len(array) - 1

    for i in range(0, max_array_index, 2):
        array_swapped.append(array[i + 1])
        array_swapped.append(array[i])

    try:
        array_swapped.append(array[max_array_index])
    except IndexError:
        pass

    return array_swapped


def main():
    array_original = fill_array()
    array_swapped = swap_array_elements(array_original)
    print(f"Swapped array: {array_swapped}")


if __name__ == '__main__':
    main()
