from .utils import *

sample = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.""".splitlines()

sample2 = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.""".splitlines()


def parse_contents(contents: str):
    if contents == "no other .":
        return

    contents = contents.replace(".", "").split(", ")
    for content in contents:
        yield int(content[0]), content[1:].strip()


def get_bags(inp):
    bags = {}

    for i in inp:
        bag, contents = i.replace("bags", "").replace("bag", "").split(" contain ")
        contents = parse_contents(contents)
        bags[bag.strip()] = list(contents)

    return bags


def expand(bag, bags):
    for _, including_bag in bags[bag]:
        yield including_bag
        yield from expand(including_bag, bags)


def expand_with_cnt(cnt, bag, bags):
    for cnt_inner, including_bag in bags[bag]:
        yield cnt_inner * cnt, including_bag
        yield from expand_with_cnt(cnt_inner * cnt, including_bag, bags)


def how_many(inp):
    bags = get_bags(inp)
    expanded = {}
    for bag in bags:
        expanded[bag] = set(expand(bag, bags))

    for i in expanded:
        if "shiny gold" in expanded[i]:
            yield 1


def how_many_2(inp):
    bags = get_bags(inp)
    for cnt, _ in expand_with_cnt(1, "shiny gold", bags):
        yield cnt


def run():
    assert sum(how_many(sample)) == 4
    info(sum(how_many(get_input(7))))

    assert sum(how_many_2(sample2)) == 126
    info(sum(how_many_2(get_input(7))))