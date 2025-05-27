'''
Consecutive Subarray Sum
Given an array of positive integers and a target value, return true if there is a subarray of consecutive elements that sum up to this target value.

Input: Array of integers, target value
Output: Boolean
'''

'''
Example
Input: [6,12,1,7,5,2,3], 14      	=>	Output: true (7+5+2)
Input: [8,3,7,9,10,1,13], 50		=>	Output: false
'''

'''
Constraints
Time Complexity: O(N)
Auxiliary Space Complexity: O(1)
All elements are positive.
The target is positive.
Values can be duplicated.
The subarray can contain a single value.
An empty array is a legal input.
'''

'''
"Quadratic" solution:
for i from 0 thru n-1
  for j from i thru n-1
    compute the sum of elements i through j
    if sum equals the target, return True
return false
'''

'''

state of the window: 
  sum of elements within the window

Monotonic condition (invariant):
  if state of window (sum) < target, we can continue to grow the window
  if sum > target, we need to shrink the window
  if sum equals the target, we're done
  
Diagram:

target: 14
array:
6,12,1,7,5,2,3
l
r

sum: 0
'''

'''
Pseudocode:

sequence_sum(list, target):

  initialize state related to window: set sum to 0
  initialize left to 0
  
  for r in range 0 to length of input
  
    update window state for expansion: 
       add list[r] to sum

    # while monotonic condition is not met
    while sum > target
      update window state for contraction:
        subtract list[left] from sum
      increment left
    if sum equals target return true
    
  return false
'''

def sequence_sum(list, target):
  sum = 0
  left = 0
  
  for r in range(len(list)):
  
    # update window state for expansion: 
    sum += list[r]
  
    # while monotonic condition is not met
    while sum > target:
      # update window state for contraction:
      sum -= list[left]
      left += 1
    if sum == target:
      return True
  
  return False

print(sequence_sum([8,3,7,9,10,1,13], 50))

