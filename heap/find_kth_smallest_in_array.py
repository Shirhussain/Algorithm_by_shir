import heapq
l = [3, 1, 6, 4, 5, 2]


def find_kth_smallest(arr, k):
    if not arr:
        return
    result = []
    for num in arr:
        # to do max heap,  I only need to negate the min heap then it will become max heap
        # to change min heap to max heap I'm adding negative sign
        heapq.heappush(result, -num)
        if len(result) > k:
            heapq.heappop(result)
    return -1 * heapq.heappop(result)


print(find_kth_smallest(l, 4))


def find_k_smallest(nums, k):
    if not nums:
        return
    arr = [-x for x in nums]
    # heapify will create max heap then with negation I'll create mean heap
    heapq.heapify(arr)
    i = 0
    while i < k:
        heapq.heappop(arr)
        i += 1

    return -1 * heapq.heappop(arr)


l = [3, 7, 4, 10, 20, 15]
print(find_k_smallest(l, 3))
