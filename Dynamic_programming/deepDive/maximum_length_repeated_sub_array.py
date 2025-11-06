""" 


718. Maximum Length of Repeated Subarray

Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.

 

Example 1:

Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
Output: 3
Explanation: The repeated subarray with maximum length is [3,2,1].
Example 2:

Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
Output: 5
Explanation: The repeated subarray with maximum length is [0,0,0,0,0].
"""


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # my explanation: https://excalidraw.com/#json=JF-5I8g0SI5-IA_A6EnoE,IGfiJIe487NLllcsQOIelA

        m = len(nums1)
        n = len(nums2)
        # add padding row & col of zeros
        dp = [[0] * (n+1) for _ in range(m+1)]
        max_len = 0

        for i in range(1, m+1):
            for j in range(1, n+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    max_len = max(max_len, dp[i][j])

        return max_len
