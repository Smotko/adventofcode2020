from .utils import *
from collections import defaultdict


def get_number_spoken(inp, cnt):
    inp = [int(i) for i in inp.split(",")]
    last_number = inp[0]
    turns = defaultdict(list)
    for i in range(cnt):
        if i < len(inp):
            last_number = inp[i]
            turns[last_number].append(i)
            continue
        current_turns = turns[last_number]
        if len(current_turns) == 1:
            last_number = 0
            turns[last_number].append(i)
            continue
        # if i % 1000000 == 0:
        #     info(i + 1, last_number, turns[last_number][:2])
        last_number = turns[last_number][-1] - turns[last_number][-2]
        turns[last_number].append(i)

    return last_number


def run():
    assert get_number_spoken("0,3,6", 2020) == 436
    info(get_number_spoken("2,20,0,4,1,17", 2020))

    # assert get_number_spoken("0,3,6", 30000000) == 175594
    # info(get_number_spoken("2,20,0,4,1,17", 30000000))
    warning("p2 skipped due to slowness")
