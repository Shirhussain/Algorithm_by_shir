nums = [2,2,1]

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        shir_set = set()

        while nums:
            current = nums.pop(0)
            if current in shir_set:
                shir_set.remove(current)
            else:
                shir_set.add(current)
        return list(shir_set)[0]
    
s = Solution()
result = s.singleNumber(nums)
print(result)