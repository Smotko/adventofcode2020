from .utils import *

sample = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL""".splitlines()

directions = [
    (0, -1),
    (-1, 0),
    (0, 1),
    (1, 0),
    (1, 1),
    (1, -1),
    (-1, 1),
    (-1, -1),
]


def add_t(t1, t2):
    return t1[0] + t2[0], t1[1] + t2[1]


def prnt_field(field):
    row = ""
    prev = 0
    for f in field:
        # warning(f[0], prev)
        if f[1] > prev:
            info(row)
            row = ""
            prev = f[1]
        row += field[f]
    info(row)
    info("")


def fxd_field(field):
    row = ""
    prev = 0
    for f in field:
        # warning(f[0], prev)
        if f[1] > prev:
            row += "\n"
            prev = f[1]
        row += field[f]
    return row


def simulate(rows):
    field = {}
    for j, row in enumerate(rows):
        for i, column in enumerate(row):
            field[(i, j)] = column

    cnt = 0
    seen = set([fxd_field(field)])
    while True:
        # prnt_field(field)
        next_field = {}
        for f in field:
            full_cnt = 0
            if field[f] == ".":
                next_field[f] = "."
                continue
            for direction in directions:
                if field.get(add_t(f, direction), None) == "#":
                    full_cnt += 1
            if full_cnt == 0:
                next_field[f] = "#"
            elif full_cnt >= 4:
                next_field[f] = "L"
            else:
                next_field[f] = field[f]

        field = next_field
        fxd = fxd_field(field)
        if fxd in seen:
            c = 0
            for f in field:
                if field[f] == "#":
                    c += 1
            return c
        seen.add(fxd)
        cnt += 1


def simulate2(rows):
    field = {}
    for j, row in enumerate(rows):
        for i, column in enumerate(row):
            field[(i, j)] = column

    cnt = 0
    seen = set([fxd_field(field)])
    while True:
        next_field = {}
        for f in field:
            full_cnt = 0
            if field[f] == ".":
                next_field[f] = "."
                continue
            for direction in directions:
                current = add_t(f, direction)
                while field.get(current) is not None:
                    if field.get(current) == "#":
                        full_cnt += 1
                        break
                    if field.get(current) == "L":
                        break
                    current = add_t(current, direction)
            if full_cnt == 0:
                next_field[f] = "#"
            elif full_cnt >= 5:
                next_field[f] = "L"
            else:
                next_field[f] = field[f]

        field = next_field
        fxd = fxd_field(field)
        if fxd in seen:
            c = 0
            for f in field:
                if field[f] == "#":
                    c += 1
            return c
        seen.add(fxd)
        cnt += 1


def run():

    assert simulate(sample) == 37
    info(simulate(get_input(11)))

    assert simulate2(sample) == 26
    info(simulate2(get_input(11)))