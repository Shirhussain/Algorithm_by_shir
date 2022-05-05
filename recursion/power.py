from cmath import exp


def power(base, expo):
    assert expo >= 0 and int(expo) == expo, "The number has to be only positive"
    if expo == 0:
        return 1
    elif expo == 1:
        return base
    return base*power(base,expo-1)



print(power(2,33))