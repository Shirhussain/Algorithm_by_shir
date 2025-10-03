# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.
from typing import List 

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        
        max_result = 0 
        
        while left < right:
            current_area = (right - left) * min(height[left], height[right])
            max_result = max(current_area, max_result)
            if height[left] > height[right]:
                right -= 1 
            else:
                left += 1
        return max_result

container = [1,8,6,2,5,4,8,3,7] 
s = Solution()
print(s.maxArea(container))