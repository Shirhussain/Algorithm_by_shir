# 85. Write a program to check and return the pairs of a given array A whose sum value is equal to a target value N.
from hashlib import new


arr = [1, 2, 40, 3, 9, 4]
N = 3


def two_sums(array, target):

    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] + array[j] == target:
                return i, j


print(two_sums(arr, N))




def print_pairs(arr, N):
    # hash set
    hash_set = set()

    for i in range(len(arr)):
        val = N-arr[i]
        if (val in hash_set):  # check if N-x is there in set, print the pair
            print(f"Pairs {str(arr[i])}, {str(val)}")
        hash_set.add(arr[i])


print_pairs(arr, N)
