#!/usr/bin/env python

"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""

person = {
    "Name": "Jonh",
    "LastName": "Snow",
    "Birthday": "2020.02.02",
    "City": "Wakanda",
    "E-mail": "jsnow@wakanda.gov",
    "Phone": "+7-999-399-02-02"
}


def print_person_oneline(name, lastName, birthday, city, email, phone):
    print(f"Name: {name}; LastName: {lastName}; Birthday: {birthday}; City: {city}; E-mail: {email}; Phone: {phone}")


def main():
    print_person_oneline(
        name=person["Name"],
        lastName=person["LastName"],
        birthday=person["Birthday"],
        city=person["City"],
        email=person["E-mail"],
        phone=person["Phone"])


if __name__ == '__main__':
    main()
