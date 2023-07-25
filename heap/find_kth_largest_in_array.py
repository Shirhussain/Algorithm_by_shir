import heapq


def find_kth_largest(nums, k):
    if not nums:
        return
    result = []
    for num in nums:
        heapq.heappush(result, num)
        # check if the lenght of result is greater than k
        # then I have to remove the smallest element
        if len(result) > k:
            heapq.heappop(result)
    # return the kth largest which is the minimum of the result list
    return heapq.heappop(result)


l = [3, 1, 6, 4, 5, 2]
print(find_kth_largest(l, 3))


def find_kth_smallest(nums, k):
    if not nums:
        return
    result = []
    for num in nums:
        heapq.heappush(result, -num)
        if len(result) > k:
            heapq.heappop(result)
    return -1 * heapq.heappop(result)


print(find_kth_smallest(l, 3))
