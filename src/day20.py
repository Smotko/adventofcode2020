from .utils import *

sample = """Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###..."""


class Image:
    def __init__(self, image):
        image = image.splitlines()
        self.id = int(image[0][5:-1])
        self.image = image[1:]
        self.borders = set(
            [
                self.image[0],
                self.image[-1],
                "".join([i[0] for i in self.image]),
                "".join([i[-1] for i in self.image]),
            ]
        )
        self.flipped_boarders = set(
            "".join(reversed(border)) for border in self.borders
        )
        self.all_posibilites = self.borders | self.flipped_boarders

        self.neighbours = []

    def rotate(self):
        new_image = []
        for i, _ in enumerate(self.image):
            new_image.append([])
            for j, _ in enumerate(self.image):
                new_image[i].append(self.image[j][len(self.image) - i - 1])
        new_image = ["".join(ni) for ni in new_image]

        info(new_image)
        self.image = new_image

    def __repr__(self):
        return str(self.id)


def construct_image(current: Image):
    for neibhour in current.neighbours:
        pass


def get_borders(images):
    images = [Image(i) for i in images.split("\n\n") if i]
    for image1 in images:
        for image2 in images:
            if image2.id == image1.id:
                continue
            if image1.borders.intersection(image2.all_posibilites):
                image1.neighbours.append(image2)
    prd = 1
    corner = None
    for image in images:
        if len(image.neighbours) == 2:
            prd *= image.id
            corner = image

    construct_image(corner)

    return prd


def run():
    assert get_borders(sample) == 20899048083289
    info(get_borders(get_input(20, True)))