from .utils import *
from collections import Counter, defaultdict

example = """sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew""".splitlines()


def move(current_position, direction):
    x, y, z = current_position
    if direction == "e":
        return x + 1, y - 1, z
    if direction == "se":
        return x, y - 1, z + 1
    if direction == "sw":
        return x - 1, y, z + 1
    if direction == "w":
        return x - 1, y + 1, z
    if direction == "nw":
        return x, y + 1, z - 1
    if direction == "ne":
        return x + 1, y, z - 1


def get_neibhours(tile):
    for dr in ("e", "se", "sw", "w", "nw", "ne"):
        yield move(tile, dr)


def flip_tiles(inp):

    visited = []
    tiles = defaultdict(lambda: -1)
    for path in inp:
        prev_dir = None
        current_position = (0, 0, 0)
        for direction in path:
            if direction in ("s", "n"):
                prev_dir = direction
                continue

            if direction in ("e", "w") and prev_dir is None:
                current_position = move(current_position, direction)
                continue

            current_position = move(current_position, prev_dir + direction)
            prev_dir = None
        tiles[current_position] *= -1
        visited.append(current_position)
    flipped = 0

    old_tiles = set()
    for _, cnt in Counter(visited).items():
        if cnt % 2 == 1:
            flipped += 1
            old_tiles.add(_)
    yield flipped

    new_tiles = set()
    wht_neibhrs = defaultdict(int)
    for i in range(100):
        for tile in old_tiles:
            neighbours = get_neibhours(tile)
            blckcntr = 0
            for neighbour in neighbours:
                if neighbour in old_tiles:
                    blckcntr += 1
                else:
                    wht_neibhrs[neighbour] += 1
            if blckcntr == 0 or blckcntr > 2:
                continue
            else:
                new_tiles.add(tile)
        for tile, blckcntr in wht_neibhrs.items():
            if blckcntr == 2:
                new_tiles.add(tile)
        old_tiles = new_tiles.copy()
        new_tiles = set()
        wht_neibhrs = defaultdict(int)
        # info(f"Day {i}: {len(old_tiles)}")

    yield len(old_tiles)


def run():
    frst, scnd = flip_tiles(example)
    assert frst == 10
    assert scnd == 2208

    frst, scnd = flip_tiles(get_input(24))
    info(frst)
    info(scnd)