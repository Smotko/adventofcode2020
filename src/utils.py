import requests
import percache
import os
import logging

cache = percache.Cache(".cache")


def error(*args):
    logging.error(args if len(args) > 1 else args[0])


def warning(*args):
    logging.warning(args if len(args) > 1 else args[0])


def info(*args):
    logging.info(args if len(args) > 1 else args[0])


@cache
def get_input(day):
    assert os.getenv(
        "AOC_SESSION"
    ), "Set the session cookie environment variable (export AOC_SESSION='your session cookie')"
    print("Fetching from server")
    result = requests.get(
        f"https://adventofcode.com/2020/day/{day}/input",
        cookies={"session": os.getenv("AOC_SESSION")},
    )
    return result.text.splitlines()


def get_int_input(day):
    res = get_input(day)
    return [int(r) for r in res]