from operator import itemgetter


def search(sequance, expected, finder):
    for elem in sequance:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"could not find the element you expected")


frinds = [
    {"name": "shir danishyar", "age": 25},
    {"name": "gulnar Noori", "age": 20},
    {"name": "amirkhan", "age": 35}
]


def get_frind(friend):
    return friend["name"]


print(search(frinds, "shir danishyar", get_frind))

# or

print(search(frinds, "gulnar Noori", itemgetter("name")))


help(itemgetter)

