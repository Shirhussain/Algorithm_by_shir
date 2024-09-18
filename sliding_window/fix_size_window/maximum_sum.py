nums = [5, 7, 2, 8, 10, 3]
window_size = 3


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
