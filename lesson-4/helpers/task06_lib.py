from itertools import count, cycle, repeat

NUMBERS = [25, 85, 92, 96, 87, 22, 99, 100, 16, 609]


def integer_generator_limited(start_num):
    for x in count(start_num):
        if x > start_num * 2:
            break
        else:
            yield x


def integer_generator_cycled(max_loops):
    for i, x in enumerate(cycle(NUMBERS)):
        if i // len(NUMBERS) < max_loops:
            yield x
        else:
            break
