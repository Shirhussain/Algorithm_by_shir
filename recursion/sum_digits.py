# def sum_of_digits(n):
#     assert n >= 0 and int(n) == n, "The number has to be only positive integer"
#     if n == 0:
#         return 0
#     else:
#         return int(n%10) + sum_of_digits(int(n//10))

# print(sum_of_digits(-2))

# def product(*array):
#     ar = list(array)
#     le = len(ar)
#     result = 1
#     for i in range(le):
#         result = result * ar[i]
#     return result
# print(product(1,2,3,4))

# def recersive_product(*ar):
#     if len(ar) == 0:
#         return 1
#     else
#         return ar[0] * recersive_product(ar[1:])
# print(recersive_product(1,2,3,4))


# def recursiveRange(num):
#     if num == 0:
#         return 0
#     else:
#         return num + recursiveRange(num-1)

# print(recursiveRange(4))

