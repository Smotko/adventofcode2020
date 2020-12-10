from .utils import *

sample = """16
10
15
5
1
11
7
19
6
12
4""".splitlines()

sample_2 = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3""".splitlines()


def chain_jolt(adapters):
    adapters = sorted([int(ad) for ad in adapters])
    from collections import Counter

    prev = 0
    cnt = Counter()
    for ad in adapters:
        cnt.update([ad - prev])
        prev = ad
    return (cnt[3] + 1) * cnt[1]


def combinations(adapters):
    adapters = sorted([int(ad) for ad in adapters])
    adapters.append(adapters[-1] + 3)
    adapters.insert(0, 0)

    ways = [0 for _ in adapters]

    for i, a in enumerate(adapters):
        if i == 0:
            ways[i] = 1
            continue
        for j in range(1, max(4, i)):
            if a - adapters[i - j] <= 3:
                ways[i] += ways[i - j]

    return ways.pop()


def run():
    assert chain_jolt(sample) == 7 * 5
    info(chain_jolt(get_input(10)))

    assert combinations(sample) == 8
    assert combinations(sample_2) == 19208
    info(combinations(get_input(10)))