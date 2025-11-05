import random


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # make it max heap by negating a heap
        # result = [-x for x in nums]
        # heapq.heapify(result)

        # for i in range(k-1):
        #     heapq.heappop(result)

        # return result[0]*-1

        # or quick select

        def quick_select(nums, k):
            pivote = random.choice(nums)

            # this work for Kth smallest
            # left = [x for x in nums if x < pivote]
            # mid  = [x for x in nums if x == pivote]
            # right= [x for x in nums if x > pivote]

            # revers it for kth largest
            left = [x for x in nums if x > pivote]
            mid = [x for x in nums if x == pivote]
            right = [x for x in nums if x < pivote]

            if k <= len(left):
                return quick_select(left, k)
            elif k <= len(left) + len(mid):
                return pivote
            else:
                return quick_select(right, k - len(left) - len(mid))
        return quick_select(nums, k)

        # or heap

        # min_heap = []
        # # with min heap you always mentain the heap of (k) length
        # for num in nums:
        #     heapq.heappush(min_heap, num)
        #     if len(min_heap) > k:
        #         heapq.heappop(min_heap)
        # return min_heap[0]
