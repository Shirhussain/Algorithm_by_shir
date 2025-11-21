""" 
Jump Game

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105



https://docs.google.com/document/d/1sUbgsggdXtTx4a-yuvcWGwnkexBkICT8f7Fd94beAtE/edit?usp=sharing
"""

from typing import List 
from collections import cache 

class Solution:
    # https://docs.google.com/document/d/1sUbgsggdXtTx4a-yuvcWGwnkexBkICT8f7Fd94beAtE/edit?usp=sharing
    def canJump(self, nums: List[int]) -> bool:
        """

            for example start at index 0 then the number is 2 and we have up to 2 branches 
            F(0) ----> can I reach to the last item if I'm at index K 
            1/ 2\
        F(1)   F(2)
        


            for example start at index 1 then the number is 3 and we have up to 3 branches 
            F(1) ----> can I reach to the last item if I'm at index K 
            1/ 2\ \3
        F(2)   F(3) F(4)
        


        """
        n = len(nums)

        @cache
        def dfs(k): # can I reach to the last item if I'm at index K 
            if k == n-1:
                return True
            
            max_jump = nums[k]

            for i in range(1, max_jump+1):
                next_index = k +i 
                # we need to discord those jump which is gos beyond the last index
                if next_index < n and dfs(next_index):
                    return True 
            return False 

        return dfs(0) # start from first index


