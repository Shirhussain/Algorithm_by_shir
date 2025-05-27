# https://excalidraw.com/#room=2cc3f9e3752af4d35142,8FuH1lk3YYNBpdbYuo-sPA

"""
    Given an integer array nums and an integer k, return the kth largest element in the array.

    Note that it is the kth largest element in the sorted order, not the kth distinct element.

    Can you solve it without sorting?

    

    Example 1:

    Input: nums = [3,2,1,5,6,4], k = 2
    Output: 5

    Example 2:

    Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
    Output: 4
"""
import heapq


def find_kth_largest_element(nums, k):
    result = []
    for num in nums:
        heapq.heappush(result, num)

        if len(result) > k:
            heapq.heappop(result)
    return heapq.heappop(result)


nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
print(find_kth_largest_element(nums, 4))


def kthl(arr, k):
    minh = []
    for i in range(k):
        heapq.heappush(minh, arr[i])

    for i in range(k, len(arr)):
        if arr[i] > minh[0]:
            heapq.heappop(minh)
            heapq.heappush(minh, arr[i])
    return minh[0]


nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
print(kthl(nums, k))
