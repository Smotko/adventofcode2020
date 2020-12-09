import logging
import math
from collections import Counter

from .utils import get_input


grid = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#""".splitlines()


def slope(step, down):
    grid = get_input(3)
    j = 0
    for i, row in enumerate(grid):
        if i % down == 1:
            continue
        if row[j] == "#":
            yield 1
        j = j + step
        j = j % len(row)


def run():
    logging.info(sum((slope(3, 1))))
    logging.info(
        math.prod(
            [sum(slope(s, d)) for s, d in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]]
        )
    )