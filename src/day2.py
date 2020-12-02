import logging

from collections import Counter

from utils import get_input


def validate_pass():
    passwords = get_input(2)
    for p in passwords:
        times, letter, password = p.split(" ")
        letter = letter[0]
        counts = Counter(password)
        low, high = times.split("-")
        if counts[letter] >= int(low) and counts[letter] <= int(high):
            yield password


def validate_pass_2():
    passwords = get_input(2)
    for p in passwords:
        pos, letter, password = p.split(" ")
        letter = letter[0]
        low, high = pos.split("-")
        first, second = password[int(low) - 1], password[int(high) - 1]
        if letter in (first, second) and first != second:
            yield password


def run():
    logging.info(len(list(validate_pass())))
    logging.info(len(list(validate_pass_2())))