from .utils import *

sample = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0""".splitlines()

sample2 = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1""".splitlines()


def compute(lines):
    memory = {}
    or_mask = None
    and_mask = None
    for inp in lines:

        op, val = inp.split(" = ")
        if op == "mask":
            or_mask = int(val.replace("X", "0"), 2)
            and_mask = int(val.replace("X", "1"), 2)
            continue

        mem = int(op.replace("mem[", "").replace("]", ""))
        val = int(val)

        memory[mem] = int(val) & and_mask | or_mask

    return sum(memory.values())


def replace_x(mask):
    if "X" not in mask:
        yield int(mask, 2)
    else:
        yield from replace_x(mask.replace("X", "0", 1))
        yield from replace_x(mask.replace("X", "1", 1))


def compute2(lines):
    memory = {}
    mask = None
    for inp in lines:
        op, val = inp.split(" = ")
        if op == "mask":
            mask = val
            continue

        mem = int(op.replace("mem[", "").replace("]", ""))
        val = int(val)

        mem &= int(mask.replace("0", "1").replace("X", "0"), 2)
        for m in replace_x(mask):
            memory[m | mem] = val
    return sum(memory.values())


def run():
    assert compute(sample) == 165
    info(compute(get_input(14)))

    assert compute2(sample2) == 208
    info(compute2(get_input(14)))