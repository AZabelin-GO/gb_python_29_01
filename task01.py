#!/usr/bin/env python

variables_types = {
    'int_var': 1,
    'float_var': 2.0,
    'str_var': 'str_var',
    'bool_var': True,
    'list_var': [1, 2, 3],
    'tuple_var': (1, 2, 3),
    'dict_var': {'a': 1, 'b': 2}
}


def main():
    for key in variables_types.keys():
        print(f'Variable name: {key}')
        print(f'Variable type: {type(variables_types[key])}')
        print(f'Variable value: {variables_types[key]}')
        print()


if __name__ == '__main__':
    main()
