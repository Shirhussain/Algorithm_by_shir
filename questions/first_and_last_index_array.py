arr = [1, 3, 4, 6, 6, 6, 6, 12, 0, -1]


def find_first_and_last_index(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            start = i
            while arr[i+1] < len(arr) and arr[i] == target:
                i += 1
            return [start, i]
    return [-1, -1]


print(find_first_and_last_index(arr, 6))


# solution with binary search

def find_first(arr, target):
    if arr[0] == target:
        return 0
    left, right = 0, len(arr)-1
    while left < right:
        mid = (left + right)//2
        if arr[mid] == target and arr[mid-1] < target:
            return mid
        elif arr[mid-1] < target:
            left = mid+1
        else:
            right = mid - 1
    return -1


def find_end(arr, target):
    if arr[-1] == target:
        return 0
    left, right = 0, len(arr)-1
    while left < right:
        mid = (left + right)//2
        if arr[mid] == target and arr[mid+1] > target:
            return mid
        elif arr[mid+1] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def find_first_and_last(arr, target):
    if len(arr) == 0 or arr[0] > target or arr[-1] < target:
        return [-1, -1]
    start = find_first(arr, target)
    end = find_end(arr, target)


print(find_first_and_last_index(arr, 6))
