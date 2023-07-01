"""
Find the Median of a Number Stream

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.

Example: arr = [2, 3, 4], the median is 3.
Example: arr = [1, -2, 3], the median is 1.
Example: arr = [1, 8, 7, 4, 3, 10], the median is 5.5.

Implement the MedianFinder class:
MedianFinder() initializes the MedianFinder object.
addNum(int num) adds the integer num to the data structure.
findMedian() returns the median of all elements added so far.
Example
Input:
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]

Output:
[null, null, null, 1.5, null, 2.0]

Explanation:
medianFinder = MedianFinder()
medianFinder.addNum(1)    # arr = [1]
medianFinder.addNum(2)    # arr = [1, 2]
medianFinder.findMedian() # return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3)    # arr[1, 2, 3]
medianFinder.findMedian() # return 2.0


Input:
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian"]
[[], [4], [6], [], [2], [], [7], []]

Output:
[null, null, null, 5.0, null, 4.0, null, 6.0]

Explanation:
medianFinder = MedianFinder()
medianFinder.addNum(4)     # arr = [4]
medianFinder.addNum(6)     # arr = [4, 6]
medianFinder.findMedian()  # Output: 5.0
medianFinder.addNum(2)     # arr = [2, 4, 6]
medianFinder.findMedian()  # Output: 4.0
medianFinder.addNum(7)     # arr = [2, 4, 6, 7]
medianFinder.findMedian()  # Output: 5.0

Constraints
- Time: addNum: O(logn)
- Time: findMedian O(1)
- Space: O(n)

By the convention we chose (favoring the lower), if the number of elements is odd, the median is always just the top of the lower


upper = {1000}
lower = {1, 9001}


Need to QUICKLY find middle two elements


INVARIANT: the lower heap is always equal to or greater than the upper in size


class MedianFinder:
  constructor():
    upper = new min heap
    lower = new max heap
    
  addNum(element):
    if lower.size() == 0 or element < lower.max():
      lower.push(element)
    else:
      upper.push(element)

    if lower.size() - upper.size() > 1:
      promoted_value = lower.heappop()
      upper.push(promoted_value)
    elif upper.size() > lower.size():
      demoted_value = upper.heappop()
      lower.push(demoted_value)
      
  findMedian():
    if upper.size() == lower.size(): # even
      return (upper.min() + lower.max())/2
    else:
      return lower.max()

"""

import heapq


class MedianFinder:
    def __init__(self):
        self.upper = []
        self.lower = []

    def addNum(self, element):
        if len(self.lower) == 0 or element < -self.lower[0]:
            heapq.heappush(self.lower, -element)
        else:
            heapq.heappush(self.upper, element)

        if len(self.lower) - len(self.upper) > 1:
            promoted_value = -heapq.heappop(self.lower)
            heapq.heappush(self.upper, promoted_value)
        elif len(self.upper) > len(self.lower):
            demoted_value = heapq.heappop(self.upper)
            heapq.heappush(self.lower, -demoted_value)

    def findMedian(self):
        if len(self.upper) == len(self.lower):  # even
            return (self.upper[0] + -self.lower[0])/2
        else:
            return -self.lower[0]
