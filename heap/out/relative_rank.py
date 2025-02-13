""" 
Relative Ranks

You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.

The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:

    The 1st place athlete's rank is "Gold Medal".
    The 2nd place athlete's rank is "Silver Medal".
    The 3rd place athlete's rank is "Bronze Medal".
    For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").

Return an array answer of size n where answer[i] is the rank of the ith athlete.

 

Example 1:

Input: score = [5,4,3,2,1]
Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
Explanation: The placements are [1st, 2nd, 3rd, 4th, 5th].

Example 2:

Input: score = [10,3,8,9,4]
Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
Explanation: The placements are [1st, 5th, 3rd, 2nd, 4th].

 
"""

from heapq import heappush, heappop


def findRelativeRanks(score):
    """ 
Solution: 
    Put every element and its index as a pair in a max heap. Then keep popping. 
    When popping the ith item as (x,y), convert i to rank and put it at index y.

    Runtime: O(n logn)
    Space: O(n)

    input: [10,3,8,9,4]

            10,0
        /    \
        8,2     9,3
        /  \
        3,2   4,4


    """
    maxHeap = []
    output = [0] * len(score)

    for i, s in enumerate(score):
        # to convert min heap to a max heap just negate date by multiplying with (-1)
        heappush(maxHeap, (-s, i))

    def get_rank(i):
        if i == 0:
            return "Gold Medal"
        if i == 1:
            return "Silver Medal"
        if i == 2:
            return "Bronze Medal"
        return str(i+1)

    for i in range(len(score)):
        x, y = heappop(maxHeap)
        output[y] = get_rank(i)

    return output


score1 = [10, 3, 8, 9, 4]
score2 = [5, 4, 3, 2, 1]
print(findRelativeRanks(score1))
print(findRelativeRanks(score2))
