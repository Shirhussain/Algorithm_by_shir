'''
Longest Substring Without Repeating Characters
Given a string s, find the longest substring without repeating characters.
Repeated characters are those with the same numeric character values.
Length of up to 10^6 characters.

Input: String
Output: String
'''

'''
Example
Input: abcabcbb      =>	Output: abc
Input: bbbbb	 	=>	Output: b
Input: pwwkew		=>	Output: wke
'''

'''
Constraints
N ~ Length of input string
K ~ Number of unique characters in input string

Time Complexity: O(N)
Auxiliary Space Complexity: O(K)
s consists of English letters, digits, symbols and spaces.
'''

'''
Quadratic solution

ans = ""
for i from 0 through length of the string
  create memory as an empty set
  for j from i through end of the string
    if input[j] not in memory
      add input[j] to memory
    else
      if j-i > len(ans)
        copy input[i:j] to ans
      break
  (also need to check the string if j reached the end)
return ans
'''
'''

result will be indices of the maximal substring

State:
  characters within the window + count for each

Monotonic condition is: 

  count of every character in state is at most 1

Diagram:

bacabcbb
 l
  r

state: {a:0, b:1, c:0}
l_best: 0
r_best: 3

Pseudocode:

initialize state related to window: create empty hash
initialize left to 0

for r in range 0 to length of input

    state[input[r]] += 1 // might need to code carefully
    
  if r-left > r_best-l_best then
    l_best, r_best = left, r
  while state[input[r]] == 2
    state[input[left]] -= 1
    increment left
    
if n-left > r_best-l_best then
  l_best, r_best = left, r

return input[l_best:r_best]

'''
'''
sliding_window(input)


'''
