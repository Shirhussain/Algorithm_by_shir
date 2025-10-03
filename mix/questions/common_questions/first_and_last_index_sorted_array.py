arr = [2, 3, 4, 5, 5, 5, 5, 7, 9, 9]
target = 5


def first_and_last_index(array, target):
    result = []
    for i in range(len(array)):
        if array[i] == target:
            result.append(i)
    return result[0], result[-1]


print(first_and_last_index(arr, target))

# or


def first_and_last_index(array, target):
    for i in range(len(array)):
        if array[i] == target:
            start = i
            while i < len(array) and array[i+1] == target:
                i += 1
            return [start, i]
    return [-1, -1]


print(first_and_last_index(arr, target))
