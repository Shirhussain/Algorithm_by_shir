def add_nums(num1, num2):
    while num2 != 0:
        data = num1 & num2
        num1 = num1 ^ num2
        num2 = data << 1
    return num1


print(add_nums(2, 10))


def add(x,y):
    for _ in range(1, y):
        x += y
    return x
