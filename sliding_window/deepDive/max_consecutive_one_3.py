""" 
1004. Max Consecutive Ones III


Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Solution 1:
    Sliding window:
    We create a sliding window.
    - Expand as long as k >= 0. Flip 0's and decrement k to enlarge the window.
    - Contract when once k<0. If we drop a 0 out, increment k.
    - Once k becomes non-negative again, we update the result to the max window size seen so far

"""

nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3

def longestOnes(nums,k):
    l = 0
    result = 0
    
    for r in range(len(nums)):
        if nums[r] == 0:
            k -= 1
        
        while k < 0:
            if nums[l] == 0:
                k += 1
            l += 1
        result = max(result, r-l +1)
    return result


print(longestOnes(nums,))
        


# We flip at most k zeros
# When k<0, it means we flipped too many, so we shrink the window
# While shirnking: if the left most number was a flipped 0, we increment k

# As a rule of thumb in sliding window:
# - When we minimize, usually we update the result inside the while loop
# - When we maximize, usually we update the result after the while loop
