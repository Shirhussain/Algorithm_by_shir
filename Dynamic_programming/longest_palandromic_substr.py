'''
Given a string of lowercase characters (a-z), return the length of the longest palindromic subsequence.

Subsequence: a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

For example, the sequence ⟨A, B, D⟩ is a subsequence of ⟨A, B, C, D, E, F⟩ obtained after removal of elements C, E, and F.

"racecar"

Input:  "vtvvv"
Output: 4

Longest palindromic subsequence here is "vvvv"


Input:  "pwnnb"
Output: 2

Longest palindromic subsequence here is "nn"


Input:  "ttbtctcbt"
Output: 7

Longest palindromic subsequence here is "tbtctbt"

Understand
Diagram
Pseudocode
Code

"pwnnb"
   ^^

                      ""
            "{p}"            "{b}"
      "{p}"        "{n}"    "{b}"     "{w}"
  "{p}"    "i{n}" "{w}" "{n}" 
                        "nn"

"vtvvv"
   ^^
 result = 2
                      "vv"
              "v{t}v"        "v{v}v"    
              "v{t}{v}v"     "vvvv"

# Memo template
def outer(...):
  cache = {}
  def left(...):
    key = ...

    if key in cache:
      return cache[key]

    // Base case(s)

    // Recursive case(s)
    if (....):
      cache[key] = ...
      return cache[key]
    


def longestPalindromicSubstring(string):
  cache = {}
  
  def find(left, right):
    key = str(left) + "_" + str(right)

    if key in cache:
      return cache[key]
      
    if left == right
      return 1
    elif left == right - 1 and string[left] == string[right]
      return 2
      
    elif string[left] == string[right]
      cache[key] = 2 + find(left + 1, right - 1)
      return cache[key]

    cache[key] = max(find(left + 1, right), find(left, right - 1))
    return cache[key]

  return find(0, len(string) - 1)
'''

def longestPalindromicSubstring(string):
  if string == "":
    return 0

  count = 0
    
  def find(left, right):
    nonlocal count
    count = count + 1
    if left == right:
      return 1
    elif left == right - 1 and string[left] == string[right]:
      return 2
    elif string[left] == string[right]:
      return 2 + find(left + 1, right - 1)

    return max(find(left + 1, right), find(left, right - 1))

  
  result = find(0, len(string) - 1)
  print(count)
  return result

'''
Time: O(2**n)
Space: O(n)
'''


def cachedLongestPalindromicSubstring(string):
  cache = {}

  count = 0
  
  def find(left, right):
    
    key = str(left) + "_" + str(right)

    if key in cache:
      return cache[key]

    nonlocal count
    count = count + 1
    
    if left == right:
      return 1
    elif left == right - 1 and string[left] == string[right]:
      return 2
      
    elif string[left] == string[right]:
      cache[key] = 2 + find(left + 1, right - 1)
      return cache[key]

    cache[key] = max(find(left + 1, right), find(left, right - 1))
    return cache[key]

  result = find(0, len(string) - 1)
  print(count)
  return result

print(cachedLongestPalindromicSubstring("pwnnb"))

'''
Time: O(n**2)
Space: O(n**2)
'''

'''
Count all the possible paths from the top left to the bottom right of a M X N matrix with the constraints that from each cell you can either move only to the right or down

  . .
  . .


  
'''