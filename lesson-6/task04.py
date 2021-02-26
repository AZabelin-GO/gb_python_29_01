#!/usr/bin/env python

from enum import Enum
from random import randint

"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Colors(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"
    BLACK = "black"
    YELLOW = "yellow"
    WHITE = "white"


class Directions(Enum):
    LEFT = "left"
    RIGHT = "right"


class Car:
    _name = ""
    _color = ""
    _speed = 0
    _is_police = False

    def __init__(self, name, color, speed=0, is_police=False):
        self._name = name
        self._color = color
        self._speed = speed
        self._is_police = is_police

    def set_speed(self, speed):
        self._speed = speed

    def get_speed(self):
        return self._speed

    def show_speed(self):
        print(f"{self._name}, current speed: {self._speed}")

    def go(self):
        self.set_speed(randint(1, 280))
        print(f"Car '{self._name}' started to move")

    def stop(self):
        self.set_speed(0)
        print(f"Car '{self._name}' stopped")

    def turn(self, direction):
        print(f"Car '{self._name}' turned '{direction.value}'")


class TownCar(Car):
    def __init__(self, name, color=Colors.WHITE):
        super().__init__(name, color=color, is_police=False)

    def show_speed(self):
        print(f"{self._name}, current speed: {self._speed}")
        if self.get_speed() > 60:
            print("Car is moving too fast. I am calling the police!")


class SportCar(Car):
    def __init__(self, name, color=Colors.RED):
        super().__init__(name, color=color, is_police=False)


class WorkCar(Car):
    def __init__(self, name, color=Colors.YELLOW):
        super().__init__(name, color=color, is_police=False)

    def show_speed(self):
        print(f"{self._name}, current speed: {self._speed}")
        if self.get_speed() > 40:
            print("Car is moving too fast. I am calling to your Boss!")


class PoliceCar(Car):
    def __init__(self, name, color=Colors.BLUE):
        super().__init__(name, color=color, is_police=True)


def main():
    # Random car
    random_car = Car("Volvo", Colors.BLACK)
    random_car.go()
    random_car.turn(Directions.LEFT)
    random_car.show_speed()
    random_car.stop()

    # Town car
    t_car = TownCar("Suzuki")
    t_car.go()
    t_car.turn(Directions.RIGHT)
    t_car.show_speed()
    t_car.stop()

    # Sport car
    s_car = SportCar("Ferrari")
    s_car.go()
    s_car.turn(Directions.LEFT)
    s_car.show_speed()
    s_car.stop()

    # Work car
    w_car = WorkCar("Reno")
    w_car.go()
    w_car.turn(Directions.RIGHT)
    w_car.show_speed()
    w_car.stop()

    # Police car
    p_car = PoliceCar("Lada", Colors.BLACK)
    p_car.go()
    p_car.turn(Directions.RIGHT)
    p_car.show_speed()
    p_car.stop()


if __name__ == '__main__':
    main()
