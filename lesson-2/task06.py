#!/usr/bin/env python

"""
Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два
элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество,
единица измерения). Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]

Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
например название, а значение — список значений-характеристик, например список названий товаров.

Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
"""

products = []
product_params = [
    {"name": "name", "type": "str"},
    {"name": "price", "type": "int"},
    {"name": "currency", "type": "str"},
    {"name": "count", "type": "int"},
    {"name": "count_type", "type": "str"}
]

analytic_dict = {}


def add_product(product):
    products.append(
        (
            len(products) + 1,
            product
        ))


def read_product_param(param_name, param_type):
    if param_type not in ["str", "int"]:
        raise Exception(f"unknown param_type '{param_type}'")

    while True:
        var = input(f"Enter product {param_name}({param_type}):\n")
        if var:
            if param_type == "str" and not var.isdigit():
                return var
            elif param_type == "int" and var.isdigit():
                return int(var)
            else:
                print(f"{var} should have type {param_type}")
                continue
        else:
            return None


def read_products():
    while True:
        product = {}
        for param in product_params:
            var = read_product_param(param["name"], param["type"])
            if var is None:
                return
            else:
                product.update({param["name"]: var})
        add_product(product)


def analyze_products():
    for product_param in product_params:
        analytic_dict.update({
            product_param["name"]: []
        })
    for product in products:
        tmp = product[1]
        for product_param in product_params:
            if tmp[product_param["name"]] not in analytic_dict[product_param["name"]]:
                analytic_dict[product_param["name"]].append(tmp[product_param["name"]])


def main():
    read_products()
    print("Products:")
    print(products)
    print("Analytic:")
    analyze_products()
    print(analytic_dict)


if __name__ == '__main__':
    main()
