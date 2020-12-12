import math
from .utils import *

sample = """F10
N3
F7
R90
F11""".splitlines()


class WaypointShip:
    def __init__(self, path):
        self.position = (0, 0)
        self.waypoint_pos = (1, 10)
        self.direction = "E"
        self.path = [(p[0], int(p[1:])) for p in path]

    def add_pos(self, ns, ew):
        cns, cew = self.position
        self.position = (cns + ns, cew + ew)

    def add_waypoint_pos(self, ns, ew):
        cns, cew = self.waypoint_pos
        self.waypoint_pos = (cns + ns, cew + ew)

    def turn(self, dr, amnt):

        ns, ew = self.waypoint_pos
        val = math.radians(amnt * dr)
        nns = int(ns * math.cos(val)) - int(ew * math.sin(val))
        new = int(ns * math.sin(val)) + int(ew * math.cos(val))

        self.waypoint_pos = (nns, new)

    def move(self, step):
        cmd, amnt = step
        if cmd == "N":
            self.add_waypoint_pos(amnt, 0)
        elif cmd == "S":
            self.add_waypoint_pos(-amnt, 0)
        elif cmd == "E":
            self.add_waypoint_pos(0, amnt)
        elif cmd == "W":
            self.add_waypoint_pos(0, -amnt)
        elif cmd == "F":
            self.frwd(amnt)
        elif cmd == "R":
            self.turn(1, amnt)
        elif cmd == "L":
            self.turn(-1, amnt)

    def frwd(self, amnt):
        self.add_pos(self.waypoint_pos[0] * amnt, self.waypoint_pos[1] * amnt)

    def go(self):
        for step in self.path:
            self.move(step)
        return abs(self.position[0]) + abs(self.position[1])


class Ship:
    def __init__(self, path):
        self.position = (0, 0)
        self.direction = "E"
        self.path = [(p[0], int(p[1:])) for p in path]

    def add_pos(self, ns, ew):
        cns, cew = self.position
        self.position = (cns + ns, cew + ew)

    def turn(self, dr, amnt):
        if amnt not in (90, 180, 270):
            raise Exception(amnt)

        if amnt == 270:
            amnt = 90
            dr = dr * -1

        if amnt == 180:
            if self.direction == "N":
                self.direction = "S"
            elif self.direction == "E":
                self.direction = "W"
            elif self.direction == "S":
                self.direction = "N"
            elif self.direction == "W":
                self.direction = "E"

        if amnt == 90 and dr == 1:
            if self.direction == "N":
                self.direction = "E"
            elif self.direction == "E":
                self.direction = "S"
            elif self.direction == "S":
                self.direction = "W"
            elif self.direction == "W":
                self.direction = "N"

        if amnt == 90 and dr == -1:
            if self.direction == "N":
                self.direction = "W"
            elif self.direction == "W":
                self.direction = "S"
            elif self.direction == "S":
                self.direction = "E"
            elif self.direction == "E":
                self.direction = "N"

    def move(self, step):
        cmd, amnt = step
        if cmd == "N":
            self.add_pos(amnt, 0)
        elif cmd == "S":
            self.add_pos(-amnt, 0)
        elif cmd == "E":
            self.add_pos(0, amnt)
        elif cmd == "W":
            self.add_pos(0, -amnt)
        elif cmd == "F":
            self.move((self.direction, amnt))
        elif cmd == "R":
            self.turn(1, amnt)
        elif cmd == "L":
            self.turn(-1, amnt)

    def go(self):
        for step in self.path:
            self.move(step)
        return abs(self.position[0]) + abs(self.position[1])


def run():
    assert Ship(sample).go() == 25
    info(Ship(get_input(12)).go())

    assert WaypointShip(sample).go() == 286
    info(WaypointShip(get_input(12)).go())