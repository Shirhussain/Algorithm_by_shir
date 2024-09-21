# brute force approach

arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4


def max_sum_brute_force(arr, k):
    if len(arr) < k:
        return -1

    n = len(arr)

    global_sum = float('-inf')

    for i in range(n-k+1):
        current_sum = 0
        for j in range(k):
            current_sum += arr[i+j]
        global_sum = max(global_sum, current_sum)
    return global_sum


print(max_sum_brute_force(arr, k))


nums = [5, 7, 2, 8, 10, 3]
window_size = 3


def optimize_max_sum(arr, k):
    if len(arr) < k:
        return -1

    window_sum = sum(arr[:k])

    global_sum = window_sum

    for i in range(k, len(arr)):
        window_sum = window_sum + arr[i] - arr[i-k]
        global_sum = max(global_sum, window_sum)
    return global_sum


print(optimize_max_sum(arr, k))


def maximum_sum(nums, window_size):
    window_sum = 0

    for i in range(window_size):
        window_sum += nums[i]

    max_sum = window_sum

    for i in range(window_size, len(nums)):
        window_sum += nums[i] - nums[i - window_size]
        max_sum = max(max_sum, window_sum)
    return maximum_sum


result = maximum_sum(nums, window_size)
print(result)  # Output would be 20 (sum of subarray [8, 10, 2])
