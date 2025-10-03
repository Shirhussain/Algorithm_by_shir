# Write a Program to add two integers >0 without using the plus operator.

def add_nums(num1, num2):
    while num2 != 0:
        data = num1 & num2
        print("data: ", data)
        num1 = num1 ^ num2
        print("num1: ", num1)
        num2 = data << 1
        print("num2: ", num2)
    print("return num1: ", num1)
    return num1


print(add_nums(2, 10))
