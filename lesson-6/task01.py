#!/usr/bin/env python

from time import sleep

"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора
в режимы: красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться
только в указанном порядке (красный, желтый, зеленый). Проверить работу примера,
создав экземпляр и вызвав описанный метод.

Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить
соответствующее сообщение и завершать скрипт.
"""


def print_progress(total_seconds):
    for i in range(total_seconds):
        print(".", end="")
        sleep(1)
    print()


class TrafficLight:
    states = [("Red", 7), ("Yellow", 2), ("Green", 15)]
    __current_state = ""

    def __init__(self):
        self.__current_state = TrafficLight.states[0]

    def running(self):
        while True:
            print(f"Current state: {self.__current_state[0]}")
            self.__switch_state()

    def __switch_state(self):
        if self.__current_state == TrafficLight.states[0]:
            print_progress(self.__current_state[1])
            self.__current_state = TrafficLight.states[1]
        elif self.__current_state == TrafficLight.states[1]:
            print_progress(self.__current_state[1])
            self.__current_state = TrafficLight.states[2]
        elif self.__current_state == TrafficLight.states[2]:
            print_progress(self.__current_state[1])
            self.__current_state = TrafficLight.states[0]


def main():
    t_light = TrafficLight()
    t_light.running()


if __name__ == '__main__':
    main()
