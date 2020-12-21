from .utils import *
from collections import Counter

sample = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)""".splitlines()


def parse_ingredients(inp):
    possible_alergens = {}
    all_ingredients = []

    for line in inp:
        ingredients, alergens = line.split(" (contains ")
        ingredients = ingredients.split()
        all_ingredients += ingredients
        ingredients = set(ingredients)

        alergens = set(alergens.replace(")", "").split(", "))

        for alg in alergens:
            if alg not in possible_alergens:
                possible_alergens[alg] = ingredients.copy()
            else:
                possible_alergens[alg] &= ingredients
    choices = {i for v in possible_alergens.values() for i in v}
    cnt = 0
    for ing in all_ingredients:
        if ing not in choices:
            cnt += 1

    allergens = {alg: list(ing) for alg, ing in possible_alergens.items()}
    while any(True for ing in allergens.values() if isinstance(ing, list)):
        for a, ing in allergens.items():
            if isinstance(ing, list) and len(ing) == 1:
                allergens[a] = ing[0]
                for ing2 in allergens.values():
                    if isinstance(ing2, list) and ing[0] in ing2:
                        ing2.remove(ing[0])

    ans = sorted(allergens.keys())
    return cnt, ",".join([allergens[i] for i in ans])


def run():
    frst, scnd = parse_ingredients(sample)
    assert frst == 5
    assert scnd == "mxmxvkd,sqjhc,fvjkl"

    frst, scnd = parse_ingredients(get_input(21))
    info(frst)
    info(scnd)