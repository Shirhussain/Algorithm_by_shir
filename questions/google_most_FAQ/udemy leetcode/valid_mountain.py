
# Given an array of integers arr, return true if and only if it is a valid mountain array.

# Recall that arr is a mountain array if and only if:

#     arr.length >= 3
#     There exists some i with 0 < i < arr.length - 1 such that:
#         arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
#         arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

from typing import List 

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        # the role is to be increase then decrease
        if len(arr) < 3:
            return False

        j= 1
        while j < len(arr) and arr[j] > arr[j-1]:
            j += 1
        
        #if j == 1 or reach to the end without decrease j == len(arr) return false
        if j in [1, len(arr)]:
            return False
        while j < len(arr) and arr[j] < arr[j-1]:
            j += 1
            
        # if j reach to the end successfully return True 
        return j == len(arr)


number = [0,3,2,1] 
s = Solution()
result = s.validMountainArray(number)
print(result)
        