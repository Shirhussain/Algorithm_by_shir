def merge_two_arr(arr1, arr2):
    result = []
    i = 0
    j = 0
    arr_len = len(arr1) + len(arr2)
    while i + j < arr_len:
        if j >= len(arr2) or (arr1[i] < arr2[j] and i < len(arr1)):
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    return result


array1 = [1, 9, 22]
array2 = [0, 2, 4, 6, 8, 19]


print(merge_two_arr(array1, array2))
