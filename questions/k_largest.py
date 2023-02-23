# k largest(or smallest) elements in an array

import re


my_arr = [1, 23, 12, 9, 30, 2, 50]

def k_largest(arr, k):
    arr.sort(reverse=True)
    for i in range(k):
        print(arr[i])
    
k_largest(my_arr, 3)

print("\n================================")



