from __future__ import annotations
from typing import List
from .utils import *
from dataclasses import dataclass


@dataclass
class Instruction:
    typ: str
    param: int


class Program:
    def __init__(self, inp):
        self.pos = 0
        self.acc = 0
        self.finished = False
        self.instructions: List[Instruction] = []
        for line in inp:
            typ, param = line.split(" ")
            self.instructions.append(Instruction(typ, int(param)))

    def process_current_instruction(self):
        ci = self.instructions[self.pos]
        if ci.typ == "nop":
            self.pos += 1
            return

        if ci.typ == "acc":
            self.acc += ci.param
            self.pos += 1
            return

        if ci.typ == "jmp":
            self.pos += ci.param
            return

    def run(self) -> Program:
        visited_positions = set()
        while self.pos not in visited_positions:
            if self.pos == len(self.instructions):
                self.finished = True
                return self
            if self.pos < 0:
                return self
            visited_positions.add(self.pos)
            self.process_current_instruction()
        return self


sample = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6""".splitlines()


def run():
    assert Program(sample).run().acc == 5

    info(Program(get_input(8)).run().acc)

    for inp in all_possible_inpts(sample):
        p = Program(inp).run()
        if p.finished:
            assert p.acc == 8

    for inp in all_possible_inpts(get_input(8)):
        p = Program(inp).run()
        if p.finished:
            info(p.acc)
            return


def all_possible_inpts(sample):
    for i, line in enumerate(sample):
        if "nop" in line:
            yield sample[:i] + [line.replace("nop", "jmp")] + sample[i + 1 :]

        if "jmp" in line:
            yield sample[:i] + [line.replace("jmp", "nop")] + sample[i + 1 :]
