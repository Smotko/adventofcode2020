import logging
from utils import get_int_input


def run():
    expenses = set(get_int_input(1))
    for e in expenses:
        search = 2020 - e
        if search in expenses:
            logging.info(e * search)
            break

    for a in expenses:
        for b in expenses:
            c = 2020 - a - b
            if c in expenses:
                logging.info(a * b * c)
                return