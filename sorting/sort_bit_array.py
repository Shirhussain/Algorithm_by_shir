from collections import Counter


def sort_bit_array(arr):
    n = len(arr)
    j = -1
    for i in range(n):
        if arr[i] < 1:
            j += 1
            arr[i], arr[j] = arr[j], arr[i]
    return arr


arr = [0, 1, 1, 1, 0, 0, 0, 1, 1]
print(sort_bit_array(arr))


def sort(arr):
    zeros = arr.count(0)
    j = 0
    while zeros:
        arr[j] = 0
        zeros = zeros - 1
        j += 1
    for i in range(j, len(arr)):
        arr[i] = 1
    return arr


print(sort(arr))


def sorting(arr):
    m = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            arr[i] = 0
            m += 1

    for i in range(m, len(arr)):
        arr[i] = 1
    return arr


print(sorting(arr))


def sort_swap(arr):
    pivot = 1
    j = 0
    for i in range(len(arr)):
        if arr[i] < pivot:
            swap(arr, i, j)
            j += 1
    return arr


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


print(sort_swap(arr))


def sort_pointer(arr):
    l, r = 0, len(arr)-1
    while l <= r:
        if arr[l] == 0:
            l += 1
        elif arr[r] == 1:
            r -= 1
        else:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
    return arr


print(sort_pointer(arr))


def sort_count(arr):
    count_zero = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            count_zero += 1
        else:
            arr[i] = 0
    for i in range(count_zero, len(arr)):
        arr[i] = 1

    return arr


arr = [0, 1, 1, 1, 0, 0, 0, 1, 1]
print(sort_count(arr))


# hallenge 1 : Number of Ones in a Sorted Bit Array
# Given a sorted bit array (values of either 0 or 1), determine the number of 1’s in the array.
# Perform this in O(log(N)) time complexity.
# Input: [0,0,0,1,1,1,1,1,1,1,1]

# Output: 8

arr = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]


def count_one(arr):
    l, r = 0, len(arr)

    while l <= r:
        mid = (l+r)//2
        if arr[mid] == 1 and arr[mid-1] == 0:
            return len(arr) - mid
        elif arr[mid] == 0:
            l = mid + 1
        elif arr[mid] == 1:
            r = mid - 1
        else:
            return -1


print(count_one(arr))
