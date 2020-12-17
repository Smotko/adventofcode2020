from .utils import *

sample = """.#.
..#
###""".splitlines()


class Conway4D:
    def __init__(self, inp):
        self.field = {}
        for j, row in enumerate(["." * len(inp)] + inp + ["." * len(inp)]):
            for i, itm in enumerate(row):
                self.field[(i, j, 0, 0)] = itm
                for k in [-1, 1, 0]:
                    for l in [-1, 1, 0]:
                        if (i, j, k, l) == (i, j, 0, 0):
                            continue
                        self.field[(i, j, k, l)] = "."
                        self.field[(i, j, k, l)] = "."

    def simulate(self, num_times):

        for _ in range(num_times):
            new_field = {}
            for (i, j, k, l) in self.field:
                full = 0
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        for z in range(-1, 2):
                            for w in range(-1, 2):
                                if (x, y, z, w) == (0, 0, 0, 0):
                                    continue
                                neibghor = ((x + i), (y + j), (z + k), (w + l))
                                if neibghor not in self.field:
                                    new_field[neibghor] = "."
                                if self.field.get(neibghor, ".") == "#":
                                    full += 1
                if self.field[(i, j, k, l)] == "#" and full not in (2, 3):
                    new_field[(i, j, k, l)] = "."
                elif self.field[(i, j, k, l)] == "." and full == 3:
                    new_field[(i, j, k, l)] = "#"
                else:
                    new_field[(i, j, k, l)] = self.field[(i, j, k, l)]
            self.field = new_field
        return sum([1 for p in self.field.values() if p == "#"])


class Conway:
    def __init__(self, inp):
        self.field = {}
        for j, row in enumerate(["." * len(inp)] + inp + ["." * len(inp)]):
            for i, itm in enumerate(row):
                self.field[(i, j, 0)] = itm
                self.field[(i, j, -1)] = "."
                self.field[(i, j, 1)] = "."

    def simulate(self, num_times):

        for _ in range(num_times):
            new_field = {}
            for (i, j, k) in self.field:
                full = 0
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        for z in range(-1, 2):
                            if (x, y, z) == (0, 0, 0):
                                continue
                            neibghor = ((x + i), (y + j), (z + k))
                            if neibghor not in self.field:
                                new_field[neibghor] = "."
                            if self.field.get(neibghor, ".") == "#":
                                full += 1
                if self.field[(i, j, k)] == "#" and full not in (2, 3):
                    new_field[(i, j, k)] = "."
                elif self.field[(i, j, k)] == "." and full == 3:
                    new_field[(i, j, k)] = "#"
                else:
                    new_field[(i, j, k)] = self.field[(i, j, k)]
            self.field = new_field
        return sum([1 for p in self.field.values() if p == "#"])


def run():

    assert Conway(sample).simulate(6) == 112
    info(Conway(get_input(17)).simulate(6))

    # assert Conway4D(sample).simulate(6) == 848
    # info(Conway4D(get_input(17)).simulate(6))
    warning("p2 skipped due to slowness")