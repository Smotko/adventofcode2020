from .utils import *

sample = """939
7,13,x,x,59,x,31,19""".splitlines()


def chinese_remainder(n, a):
    """ # https://rosettacode.org/wiki/Chinese_remainder_theorem#Python """
    from functools import reduce

    def mul_inv(a, b):
        b0 = b
        x0, x1 = 0, 1
        if b == 1:
            return 1
        while a > 1:
            q = a // b
            a, b = b, a % b
            x0, x1 = x1 - q * x0, x0
        if x1 < 0:
            x1 += b0
        return x1

    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def get_earliest_time(inp):
    initial_target, times = inp
    initial_target = int(initial_target)
    target = initial_target
    times = [int(t) for t in times.split(",") if t != "x"]
    while True:
        target += 1
        for t in times:
            if target % t == 0:
                return t * (target - initial_target)


def earliest_timestamp(times):
    times = [(i, int(t)) for i, t in enumerate(times.split(",")) if t != "x"]
    dividers = [t for _, t in times]
    remainders = [t - i for i, t in times]
    return chinese_remainder(dividers, remainders)


def run():
    assert get_earliest_time(sample) == 295
    info(get_earliest_time(get_input(13)))
    assert earliest_timestamp("17,x,13,19") == 3417
    assert earliest_timestamp("67,7,59,61") == 754018
    assert earliest_timestamp("67,x,7,59,61") == 779210
    assert earliest_timestamp("67,7,x,59,61") == 1261476
    assert earliest_timestamp("1789,37,47,1889") == 1202161486
    assert earliest_timestamp(sample[1]) == 1068781
    info(earliest_timestamp(get_input(13)[1]))