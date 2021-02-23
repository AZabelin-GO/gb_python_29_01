#!/usr/bin/env python

"""
Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и
метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    _title = ""

    def __init__(self, title="Random thing with ability to draw"):
        self._title = title

    def draw(self):
        print(f"Drawing something with '{self._title}' somewhere")


class Pen(Stationery):
    def __init__(self):
        super().__init__("Pen")

    def draw(self):
        print(f"Drawing ideal rectangle with '{self._title}' in notebook")


class Pencil(Stationery):
    def __init__(self):
        super().__init__("Pencil")

    def draw(self):
        print(f"Drawing strange picture with '{self._title}' in album")


class Marker(Stationery):
    def __init__(self):
        super().__init__("Marker")

    def draw(self):
        print(f"Drawing presentation plan with '{self._title}' on whiteboard")


def main():
    random_thing = Stationery()
    random_thing.draw()

    pen = Pen()
    pen.draw()

    pencil = Pencil()
    pencil.draw()

    marker = Marker()
    marker.draw()


if __name__ == '__main__':
    main()
