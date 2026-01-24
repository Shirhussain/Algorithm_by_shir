""" 
Triplet Sum

Given an array of integers, return all triplets [a, b, c] such that a + b + c = 0 . The solution must not contain duplicate triplets (e.g., [1, 2, 3] and [2, 3, 1] are considered duplicates). If no such triplets are found, return an empty array.

Each triplet can be arranged in any order, and the output can be returned in any order.

Example:
Input: nums = [0, -1, 2, -3, 1]
Output: [[-3, 1, 2], [-1, 0, 1]]


                                    [][0,-1,2,-3,1]
                                    /              \
                        [0][-1,2,-3,1]              [][-1,2,-3,1]
                        /            \               /            \
            [0,-1][2,-3,1]      [0][2,-3,1]    [-1][2,-3,1]    [][2,-3,1]
            /          \         /        \       /        \      /        \
    [0,-1,2][-3,1] [0,-1][2,-3,1] [0,2][-3,1] [0][2,-3,1] [-1,2][-3,1] [-1][2,-3,1] [2][-3,1] [][2,-3,1]
         ✗            /      \      /      \       ✗         /      \       /     \      /    \      /    \
    (sum=1)  [0,-1,-3][1] [0,-1][1] [0,2,-3][1] [0,2][1]  [-1,2,-3][1] [-1,2][1] [-1,-3][1] [-1][1] [2,-3][1] [2][1]
                  ✗           ✗        ✓          ✗            ✗          ✓         ✗        ✗       ✗       ✗
              (sum=-4)    (sum=0)  (sum=-1)   (sum=3)      (sum=-2)   (sum=2)   (sum=-5)            (sum=0)
                                  **VALID**                           **VALID**
                                [-3,1,2]→                            [-1,0,1]→
                                [-3,0,2]                             [-1,2,1]
                                (sorted)                             (sorted)



"""
from typing import List 

def triplet_sum_backTrack(nums: List[int]) -> List[List[int]]:
    output_set = set() 
    result = []

    def helper(index, path):
        if len(path) == 3: 
            if sum(path) == 0:
                sorted_path = tuple(sorted(path))
                if not sorted_path in output_set:
                    output_set.add(sorted_path)
                    result.append(list(sorted_path))
        
            return 
    
        # base case 
        if index >= len(nums):
            return 
        
        # optimize if we can't form an array of 3
        if (len(nums) - index) + len(path) < 3:
            return 
        
        # pick the number back tracking
        path.append(nums[index])
        helper(index+1, path)
        path.pop()
        
        # not pick up
        helper(index+1, path)
    helper(0, [])
    
    return result   


nums = [0, -1, 2, -3, 1]
print(triplet_sum_backTrack(nums))



# ============================================
# APPROACH 2: PURE RECURSION
# ============================================


def triplet_sum_pur_recursion(nums):
    result = []
    output_set = set() 
    
    def helper(index, path):
        if len(path) == 3:
            if sum(path) == 0:
                sorted_path = tuple(sorted(path))
                if sorted_path not in output_set:
                    output_set.add(sorted_path)
                    result.append(list(sorted_path))
            return
        
        if index >= len(nums) or len(path) + (len(nums) - index) < 3:
            return
        
        # Pick current number - CREATE NEW list
        helper(index + 1, path + [nums[index]])
        
        # Don't pick current number - PASS SAME list
        helper(index + 1, path)
    
    helper(0, [])
    return result

print(triplet_sum_pur_recursion(nums))




# ============================================
# APPROACH 3: PURE RECURSION (Functional Style)
# ============================================
def triplet_sum_functional(nums: List[int]) -> List[List[int]]:
    """
    Purely functional: Returns results instead of using outer variables
    No side effects, completely pure recursion
    """
    def helper(index, path):
        # Base case: valid triplet found
        if len(path) == 3:
            if sum(path) == 0:
                return [tuple(sorted(path))]
            return []
        
        # Base case: can't form valid triplet
        if index >= len(nums) or len(path) + (len(nums) - index) < 3:
            return []
        
        # Combine results from both choices
        pick = helper(index + 1, path + [nums[index]])
        skip = helper(index + 1, path)
        
        return pick + skip
    
    # Get all triplets (may have duplicates as tuples)
    all_triplets = helper(0, [])
    
    # Remove duplicates and convert back to lists
    unique_triplets = list(set(all_triplets))
    return [list(triplet) for triplet in unique_triplets]


print(triplet_sum_functional(nums))



class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()

        def helper(index, path):
            if len(path) == 3:
                if sum(path) == 0:
                    result.add(tuple(sorted(path)))
                return 

            if index == len(nums):
                return 
            
            # pick
            helper(index+1, path+[nums[index]])
                    
            # not pick
            helper(index+1, path)
        
        helper(0,[])

        return [list(t) for t in result]
s = Solution()

print("leetcode : ", s.threeSum(nums))




def brut_force_three_sum(nums):
    result = set()
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if nums[i]+nums[j] + nums[k] == 0:
                    curr_sol = [nums[i], nums[j], nums[k]]
                    result.add(tuple(sorted(curr_sol)))
    return result

print("brute force: ", brut_force_three_sum(nums))



class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        a + b + c = 0
        Notice if we fix one of the number then 
        problem reduced to two number and led this: b + c = -a
        
        now first sort and then take one fix as negative "-target" and the rest 
        will fallow tow pointer approach.  [-4, -1, -1, 0, 1, 2]
        """
        
        nums.sort()
        result = []

        def pair_sum(arr, target):
            l = 0 
            r = len(arr) -1
            sol = []
            while l < r:
                sum_pair = arr[l] + arr[r]
                if  sum_pair == target:
                    sol.append([arr[l], arr[r]])
                    l += 1
                    #l To avoid duplicate '[b, c]• pairs, s kip 'b' if it •s the same as the previous number.
                    while l < r and arr[l] == arr[l-1]:
                        l +=1 
                elif arr[l] + arr[r] < target:
                    l += 1
                elif arr[l] + arr[r] > target:
                    r -= 1
            return sol


        for i, num in enumerate(nums):
            # To avoid duplicate , skip •a' if it's the same as the previous number.
            if i > 0 and num == nums[i-1]:
                continue
            
            # I Find all pairs that sum to a target of '-a ' ( - nums [ i 1)
            pairs = pair_sum(nums[i+1:], -num)
            for pair in pairs:
                result.append([num] + pair)

        return result

s = Solution()
print("O(n^2) solution: ", s.threeSum(nums))

