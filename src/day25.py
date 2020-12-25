from .utils import *


def get_loop_size(values):
    for i in values:
        subject_number = 7
        loop_size = 0
        value = 1
        while True:
            loop_size += 1
            value *= subject_number
            value %= 20201227
            if value == i:
                yield loop_size
                break


def get_transform(loop_size, subject_number):
    value = 1
    for _ in range(loop_size):
        loop_size += 1
        value *= subject_number
        value %= 20201227
    return value


def run():
    x, y = get_loop_size([5764801, 17807724])
    assert get_transform(x, 17807724) == 14897079
    assert get_transform(y, 5764801) == 14897079

    i, j = get_int_input(25)
    x, y = get_loop_size([i, j])
    info(get_transform(x, j))
    info(get_transform(y, i))
