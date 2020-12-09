from .utils import *

sample = """abc

a
b
c

ab
ac

a
a
a
a

b""".splitlines()


def yes_answers(responses):
    group = set()
    for response in responses:
        if response == "":
            yield len(group)
            group = set()
            continue
        group = set(response).union(group)
    yield len(group)


def yes_answers_2(responses):
    group = set(responses[0])
    for i, response in enumerate(responses):
        if response == "":
            yield len(group)
            group = set(responses[i + 1])
            continue
        group = set(response).intersection(group)
    yield len(group)


def run():
    assert sum(yes_answers(sample)) == 11
    info(sum(yes_answers(get_input(6))))
    assert sum(yes_answers_2(sample)) == 6
    info(sum(yes_answers_2(get_input(6))))
