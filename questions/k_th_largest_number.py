import heapq
arr = [1, 23, 17, 5, 0, 10]
k = 4


def k_th_largest_number(arr, k):
    for _ in range(k-1):
        arr.remove(max(arr))
    return max(arr)


print(k_th_largest_number(arr, k))


# or

arr = [1, 23, 17, 5, 0, 10]
k = 4


def k_th_largest_number_sorted(arr, k):
    new_arr = sorted(arr)
    return new_arr[len(new_arr) - k]
    # return new_arr[-k]


print(k_th_largest_number_sorted(arr, k))


def k_th_largest_number_with_heapq(arr, k):
    arr = [-num for num in arr]
    heapq.heapify(arr)
    for _ in range(k-1):
        heapq.heappop(arr)
    return -heapq.heappop(arr)


print(k_th_largest_number_with_heapq(arr, k))
