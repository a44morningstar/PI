from pprint import pprint

dict = {"first": "so easy"}


def dict_maker(**kwargs):
    dict.update(**kwargs)


dict_maker(flower="hp", feather="atk", sands="atk%", goblet="cryo dmg", crown="crt dmg")
pprint(dict)
