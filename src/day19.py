from .utils import *


sample = """0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb""".splitlines()


class Ruler:
    def __init__(self, sample):

        sample = iter(sample)
        self.rules = {}
        while rule := next(sample):
            if rule == "":
                break
            rid, patterns = rule.split(": ")

            self.rules[rid] = patterns.replace('"', "")
        self.msgs = []
        try:
            while message := next(sample):
                self.msgs.append(message)
        except StopIteration:
            pass

    def expand_rule(self, rule):
        rule = self.rules[rule]
        if rule in ("a", "b"):
            return [rule]
        else:
            result = []
            for r in rule.split(" | "):
                inxs = r.split(" ")
                res = self.expand_rule(inxs[0])
                for i in inxs[1:]:
                    parts = self.expand_rule(i)
                    res = [r + p for r in res for p in parts]
                result += res
        return result

    def num_matches(self, rule):
        options = set(self.expand_rule(rule))
        return len([msg for msg in self.msgs if msg in options])


def run():
    assert Ruler(sample).num_matches("0") == 2
    info(Ruler(get_input(19)).num_matches("0"))