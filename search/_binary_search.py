def find(arr, value):
    l, r = 0, len(arr)
    while l < r:
        mid = (l+r) // 2
        if arr[mid] == value:
            return mid
        elif value > arr[mid]:
            l = mid + 1
        elif value < arr[mid]:
            r = mid - 1
        else:
            return -1


arr = [1, 3, 4, 5, 6, 7, 8, 10, 11, 13, 15, 17, 20, 22]
value = 17
print(find(arr, value))


def binary_search(arr, target):
    l, r = 0, len(arr) - 1

    while l <= r:
        mid = (l+r) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        elif arr[mid] > target:
            r = mid - 1
    return -1


print(binary_search(arr, value))


def binary_search_recursive(arr, target):
    l, r = 0, len(arr) - 1

    def helper(arr, left, right, target):
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            return helper(arr, mid + 1, right, target)
        elif arr[mid] > target:
            return helper(arr, left, mid-1, target)
        return -1
    return helper(arr, l, r, target)


print(binary_search_recursive(arr, value))
