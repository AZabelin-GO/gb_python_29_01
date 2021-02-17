#!/usr/bin/env python

"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый
текстовый файл.
"""

TEXT_FILE = "task04.txt"
NEW_FILE = "task04_tr.txt"

ENG_RUS_VOCABULARY = {
    "One": "Один",
    "Two": "Два",
    "Three": "Три",
    "Four": "Четыре",
}


def translate_into_russian(s):
    for k, v in ENG_RUS_VOCABULARY.items():
        s = s.replace(k, v)
    return s


def main():
    try:
        with open(TEXT_FILE, "r") as in_file, open(NEW_FILE, "w") as out_file:
            for line in in_file:
                s = translate_into_russian(line.strip())
                print(s, file=out_file)
    except FileNotFoundError:
        print(f"File '{TEXT_FILE}' not found")
        exit(1)


if __name__ == '__main__':
    main()
