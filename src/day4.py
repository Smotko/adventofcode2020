import re

from utils import get_input, info


passports = """pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719""".splitlines()


def parse_passports():
    passports = get_input(4)
    passport = {}
    for line in passports:

        if line == "":
            yield passport
            passport = {}
            continue

        for prop in line.split(" "):
            key, value = prop.split(":")
            passport[key] = value
    yield passport


def simple_verify(passports):
    for passport in passports:
        if len(passport) == 8:
            yield passport
        if len(passport) == 7 and "cid" not in passport.keys():
            yield passport


def verify_passports(passports):
    for passport in passports:
        byr = int(passport.get("byr", 0))
        if byr < 1920 or byr > 2002:
            continue

        iyr = int(passport.get("iyr", 0))
        if iyr < 2010 or iyr > 2020:
            continue

        eyr = int(passport.get("eyr", 0))
        if eyr < 2020 or eyr > 2030:
            continue

        hgt = int(passport.get("hgt", "0cm").replace("cm", "").replace("in", ""))
        hgtt = passport.get("hgt", "0cm")[-2:]
        if hgtt not in ("cm", "in"):
            continue
        if hgtt == "cm" and (hgt < 150 or hgt > 193):
            continue
        if hgtt == "in" and (hgt < 59 or hgt > 76):
            continue
        hcl = passport.get("hcl", "")

        if not re.match(r"^\#[0-9|a-f]{6}$", hcl):
            continue

        ecl = passport.get("ecl", "")
        if ecl not in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
            continue

        pid = passport.get("pid", "")
        if not re.match(r"^[0-9]{9}$", pid):
            continue

        yield passport


def run():
    info(len(list(simple_verify(parse_passports()))))
    info(len(list(verify_passports(parse_passports()))))