#!/usr/bin/env python

from abc import ABC, abstractmethod

"""
Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные
классы для основных классов проекта, проверить на практике работу декоратора @property.
"""


class Clothes(ABC):
    @property
    @abstractmethod
    def materials_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def materials_consumption(self):
        return (self.size / 6.5) + 0.5


class Costume(Clothes):
    def __init__(self, height):
        self.height = height

    @property
    def materials_consumption(self):
        return 2 * self.height + 0.3


def main():
    my_coat = Coat(6.5)
    my_costume = Costume(170)

    print(my_coat.materials_consumption)
    print(my_costume.materials_consumption)


if __name__ == '__main__':
    main()
