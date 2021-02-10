#!/usr/bin/env python

"""
Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должн
начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().
"""


def int_func(word):
    return word.capitalize()


def read_input():
    english_chars = set("abcdefghijklmnopqrstuvwxyz")
    s = input("Enter a word or string:\n").lower()
    if set(s.replace(" ", "")).issubset(english_chars):
        return s
    else:
        print(f"Input contains non english characters: {set(s.replace(' ', '')) - english_chars}")
        exit(1)


def main():
    string = read_input()
    print("Result:")
    for s in string.split():
        print(int_func(s), end=' ')
    print()
    print("Alternative way:")
    print(string.title())


if __name__ == '__main__':
    main()
