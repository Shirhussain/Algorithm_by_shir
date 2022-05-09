from operator import le
from pyparsing import empty
import numpy as np

my_arrray = np.array([1,20,30,44,14,15,17,99,100,73,11])
# my_arrray.sort()
# print(my_arrray)

# print(type(my_arrray))

# def maximum_product_of_two(lst):
#     new_lst = lst[-2:]
#     print(new_lst[0], new_lst[1])
#     return new_lst[0]*new_lst[1]
# print(maximum_product_of_two(my_arrray))



def max_product_two(lst):
    max_product = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] * lst[j] > max_product:
                max_product = lst[i]*lst[j]
                pairs = str(lst[i]) +"*"+ str(lst[j])
    print(pairs)
    print(max_product)
    
max_product_two(my_arrray)
