#!/usr/bin/env python

"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом
премии (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""


def print_info(obj):
    if isinstance(obj, Position):
        msg = f"""
            Full name: {obj.get_full_name()}
            Position: {obj.position}
            Income: {obj.get_total_income()}"""
        print(msg)
    elif isinstance(obj, Worker):
        msg = f"""
            Name: {obj.name}
            Surname: {obj.surname}
            Position: {obj.position}"""
        print(msg)


class Worker:
    name = ""
    surname = ""
    position = ""
    _income = {}

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


def main():
    worker_one = Worker("John", "Smith", "Cleaner", 100, 50)
    position_one = Position("Ann", "Smith", "Nurse", 75, 75)
    print_info(worker_one)
    print_info(position_one)


if __name__ == '__main__':
    main()
