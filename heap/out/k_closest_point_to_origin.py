""" 
 K Closest Points to Origin

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

 

Example 1:


Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.
 

Constraints:

1 <= k <= points.length <= 104
-104 <= xi, yi <= 104
"""

from heapq import heappush, heappushpop


def kClosest(points, k):
    """ 
    it's controversial advice that if you need K closest or minium then use Max heap 
    if you need Kth maximum then use Min heap

    Solution:

    Use a max heap of size k. Push (distance, points) to the heap and maintain the size to stay at k.


    As we push, if the size is greater than k, we compare the new item with the top, if it was better than the top
    we remove the top and add this one otherwise, we ignore it.
    """

    maxHeap = []

    def distance(p):
        return p[0] * p[0] + p[1] * p[1]

    for point in points:
        if len(maxHeap) < k:
            heappush(maxHeap, (-distance(point), point))
        else:
            # We could remove this if statement too!
            if distance(point) < -maxHeap[0][0]:
                heappushpop(maxHeap, (-distance(point), point))
    return [point[1] for point in maxHeap]


points = [[3, 3], [5, -1], [-2, 4]]
k = 2

points2 = [[1, 3], [-2, 2]]
k1 = 1
print(kClosest(points, k))
print(kClosest(points2, k1))
