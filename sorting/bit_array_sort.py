def bit_sort(arr):
    l, r = 0, len(arr)-1

    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


nums = [1, 2, 30, 12, 40, -2, 11]

print(bit_sort(nums))


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less_than = [num for num in arr if num < pivot]
    middle = [num for num in arr if num == pivot]
    grater_than = [num for num in arr if num > pivot]

    return quick_sort(less_than) + middle + quick_sort(grater_than)


print(quick_sort(nums))
