# Great common divisor
# gcd(48, 18)
# step 1: 48/18 = 2 reminder 12
# step 2: 18/12 = 1 reminder  6
# step 3: 12/6  = 2 reminder  0


def gcd(a, b):
    assert int(a) == a and int(b) == b, "Only positive integer are accpted"
    if a < 0:
        a *= -1
    if b < 0:
        b *= -1
    return a if b==0 else gcd(b, a%b)

print(gcd(48, -18))