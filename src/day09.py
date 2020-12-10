import pytest
from .utils import *

sample = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576""".splitlines()


def is_sum_of_previous(previous, sm):
    for i in previous:
        if (sm - i) in previous:
            return True
    return False


def preamble(cnt, sample):
    sample = [int(i) for i in sample]
    for indx, i in enumerate(sample[cnt:]):
        options = set(sample[indx : cnt + indx])
        if not is_sum_of_previous(options, i):
            return i


def contiguous_set(inp, goal):
    inp = [int(i) for i in inp]
    for i in range(0, len(inp)):
        for cnt, _ in enumerate(inp[i:]):
            rng = inp[i : cnt + i]
            smm = sum(rng)
            if smm == goal:
                return max(rng) + min(rng)


@pytest.mark.skip("A bit slow")
def run():
    assert preamble(5, sample) == 127
    nmbr = preamble(25, get_input(9))
    info(nmbr)

    assert contiguous_set(sample, 127) == 62
    info(contiguous_set(get_input(9), nmbr))