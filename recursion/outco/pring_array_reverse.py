l = [1, 2, 4, 6]


def recursive(l):
    if len(l) == 0:
        return []  # base case
    else:
        return [l.pop()] + recursive(l)  # recusrive case


print(recursive(l))
