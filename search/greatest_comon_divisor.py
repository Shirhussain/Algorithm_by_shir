def greatest_common(a, b):
    if a < 0:
        a *= -1
    if b < 0:
        b *= -1

    # swap input if a < b
    if a < b:
        a, b = b, a

    # use modulo to reduce the larger value until one number is zero
    while b > 0:
        temp = b
        b = a % b
        a = temp

    return a


print(greatest_common(52, 78))


def greatest_com(x, y):
    if x < 0:
        x *= -1
    if y < 0:
        y *= -1

    # swap
    if x < y:
        x, y = y, x

    while y > 0:
        x, y = y, x % y
    return x


print(greatest_com(75, 25))
