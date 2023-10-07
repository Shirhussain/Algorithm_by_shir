"""
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.
"""

"""

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 
"""

"""
Constraints:

m == s.length
n == t.length
1 <= m, n <= 10^5
s and t consist of uppercase and lowercase English letters.
 
"""

'''
Monotonic condition: do not have all of the characters in t

hash: keys are characters of t, values are counts of characters 
num_uncovered_ts: 

Diagram 

s="EBBBANC", t = "ABBC"

EBBBANC
  l
      r

hash: {A:0, B:1, C:0}
num_uncovered_ts: 1

sliding_window(input sequence)
  # initialize state related to window
  hash = {A:1, B:2, C:1}
  num_uncovered_ts = length of t
  
  initialize left to 0

  for right in range 0 to length of input

    # update window state for expansion
    if char at r is in hash then
      decrement the char in the hash
      if value of char in hash non-negative 
        decrement num_uncovered_ts <= 0
      
    # while monotonic condition is not met
    while num_uncovered_ts == 0
      # update window state for contraction
      if char at l is in the hash
        increment value of the character in the hash
        if value is positive
          increment num_uncovered_ts
      # capture the output
      if num_uncovered_ts > 0
        ...
      increment left
      
'''
