from .utils import *

sample = "389125467"


class Cup:
    def __init__(self, val, left, right):
        self.val = val
        self.right = right

    def __repr__(self):
        return f"{self.val}, ({self.right.val})"


def cup_game(inp, moves):
    cups = list(map(int, list(inp))) + (
        list(range(10, 1_000_000 + 1)) if moves > 1000 else []
    )
    cups = [
        Cup(
            cup,
            cups[i - 1] if i > 0 else None,
            cups[i + 1] if i < (len(cups) - 1) else None,
        )
        for i, cup in enumerate(cups)
    ]

    cups_dict = {cup.val: cup for cup in cups}
    for cup in cups:
        if not cup.right:
            cup.right = cups[0]
            continue
        cup.right = cups_dict[cup.right]
    cups_dict = {cup.val: cup for cup in cups}
    current_cup = cups[0]
    for i in range(moves):
        take = [
            current_cup.right,
            current_cup.right.right,
            current_cup.right.right.right,
        ]
        current_cup.right = take[-1].right
        n = current_cup.val - 1
        if n == 0:
            n = len(cups)
        while n not in range(1, len(cups) + 1) or any(node.val == n for node in take):
            n -= 1
            if n == 0:
                n = len(cups)
        dest = cups_dict[n]
        take[2].right = dest.right
        dest.right = take[0]
        current_cup = current_cup.right
    if moves < 1000:

        cup = cups_dict[1]
        seen = set([cup])
        out = [cup]
        while cup.right not in seen:
            seen.add(cup.right)
            out.append(cup.right)
        error(out)
        return int("".join([str(cup.val) for cup in out]))
    return cups_dict[1].right.val * cups_dict[1].right.right.val


def run():
    # assert cup_game(sample, moves=10) == 92658374
    # assert cup_game(sample, moves=100) == 67384529
    # info(cup_game("418976235", moves=100))
    info(cup_game("418976235", moves=10_000_000))