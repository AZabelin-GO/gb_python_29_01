#!/usr/bin/env python

"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения
двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, data):
        rows_length = [len(x) for x in data]

        if rows_length.count(rows_length[0]) == len(rows_length):
            self.data = data
        else:
            raise ValueError("Invalid data for matrix")

    def __str__(self):
        result = ""
        for row in self.data:
            result += f"{row}\n"
        return result

    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return False
        else:
            return (len(self.data), len(self.data[0])) == (len(other.data), len(other.data[0]))

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError
        elif self.get_size() == other.get_size():
            result = []
            for i in range(len(self.data)):
                result.append([sum(x) for x in zip(self.data[i], other.data[i])])

            return Matrix(result)

    def get_size(self):
        return len(self.data), len(self.data[0])


def main():
    matrix = Matrix([[1, 2, 3], [2, 3, 1], [3, 1, 2]])
    matrix2 = Matrix([[1, 2, 3], [2, 3, 1], [3, 1, 2]])
    print(matrix)
    print(matrix2)
    print(matrix + matrix2)


if __name__ == '__main__':
    main()
