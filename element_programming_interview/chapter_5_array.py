def even_odd(arr):
    next_even, next_odd = 0, len(arr)-1
    while next_even < next_odd:
        if arr[next_even] % 2 == 0:
            next_even += 1
        else:
            arr[next_even], arr[next_odd] = arr[next_odd], arr[next_even]
            arr[next_odd] -= 1
    return (next_even, next_odd)


array = [1011, 22, 23, 40, 5, 6, 7, 8, 90, 10, 11, 12, 13, 14, 15]

print(even_odd(array))


def pivot_arr(arr, number):
    new_array = []
    for i in arr:
        if i >= number:
            new_array.append(i)
        else:
            new_array.insert(0, i)
    return new_array


my_list = [1011, 22, 23, 40, 5, 6, 7, 8, 90, 10, 11, 12, 13, 14, 15]
print(pivot_arr(array, 20))
