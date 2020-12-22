from .utils import *
import copy

sample = """Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10"""


def play_cards(decks):
    frst, scnd = decks.split("\n\n")
    deck1 = []
    deck2 = []

    for card in frst.splitlines()[1:]:
        deck1.append(int(card))

    for card in scnd.splitlines()[1:]:
        deck2.append(int(card))

    while deck1 and deck2:
        c1 = deck1.pop(0)
        c2 = deck2.pop(0)
        if c1 > c2:
            deck1.append(c1)
            deck1.append(c2)
        else:
            deck2.append(c2)
            deck2.append(c1)

    winner = deck1 if deck1 else deck2
    return sum(c * (len(winner) - (i)) for i, c in enumerate(winner))


def subgame(deck1, deck2):
    seen_1 = set()
    seen_2 = set()
    while deck1 and deck2:
        curr_1 = "".join(map(str, deck1))
        curr_2 = "".join(map(str, deck2))
        if curr_1 in seen_1 or curr_2 in seen_2:
            return True, False
        seen_1.add(curr_1)
        seen_2.add(curr_2)

        c1 = deck1.pop(0)
        c2 = deck2.pop(0)

        if len(deck1) >= c1 and len(deck2) >= c2:
            d1, _ = subgame(deck1[: c1 + 1], deck2[: c2 + 1])
            if d1:
                deck1.append(c1)
                deck1.append(c2)
            else:
                deck2.append(c2)
                deck2.append(c1)
            continue
        if c1 > c2:
            deck1.append(c1)
            deck1.append(c2)
        else:
            deck2.append(c2)
            deck2.append(c1)
    return deck1, deck2


def play_recursive_cards(decks):
    frst, scnd = decks.split("\n\n")
    deck1 = []
    deck2 = []

    for card in frst.splitlines()[1:]:
        deck1.append(int(card))

    for card in scnd.splitlines()[1:]:
        deck2.append(int(card))

    deck1, deck2 = subgame(deck1, deck2)
    winner = deck1 if deck1 else deck2
    return sum(c * (len(winner) - (i)) for i, c in enumerate(winner))


def run():
    assert play_cards(sample) == 306
    info(play_cards(get_input(22, True)))

    assert play_recursive_cards(sample) == 291
    info(play_recursive_cards(get_input(22, True)))