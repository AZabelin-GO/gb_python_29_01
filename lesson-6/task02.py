#!/usr/bin/env python

"""
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * число см толщины полотна. Проверить работу метода.

Например: 20м * 5000м * 25кг * 5см = 12500 т
"""


class Road:
    _length = 0
    _width = 0

    def __init__(self, length=0, width=0):
        self._length = length
        self._width = width

    def get_length(self):
        return self._length

    def get_width(self):
        return self._width

    def calculate_materials(self, asphalt_usage, thickness):
        return (self._width * self._length * asphalt_usage * thickness) / 1000


def main():
    assert Road(5000, 20).calculate_materials(25, 5) == 12500, \
        "Formula for calculating materials for Road class is not correct"
    my_road = Road(50, 10)
    mass = my_road.calculate_materials(100, 5)
    print(f"You need '{mass}' tons of asphalt to build road with:\n" +
          f"* length = '{my_road.get_length()}'\n" +
          f"* width = '{my_road.get_width()}'")


if __name__ == '__main__':
    main()
