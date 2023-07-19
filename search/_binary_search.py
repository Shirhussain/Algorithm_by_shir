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
