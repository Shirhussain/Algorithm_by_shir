'''
Longest Substring Without Repeating Characters
Given a string s, find the longest substring without repeating characters.

Input: String
Output: String
Example
Input: abcabcbb      =>	Output: abc
Input: bbbbb	 	=>	Output: b
Input: pwwkew		=>	Output: wke

Whiteboarding
---
Understand
- Time and space complexity constraints?
  Optimal
- Capitalization?
  Yes
- Length of string?
  Assume it fits in memory
- Should i handle validation?
  Yes
- Empty input?
  Return empty
- If there are 2 or more substrings of equal length, which one should I return?
  Return any

Diagram
--
Phases of sliding window
Hunting
Catch-up

{k,e,w}
best_c = 3
best_h = 5

pwwkew
      h
   c
string[best_c:best_h] => "wke"

Pseudocode
---
TEMPLATE
--
def sliding_window(...):
  [], {}, ... # window state
  ans # return

  l, r

  # Hunting
  for r in range(len(string))
    # Hunting logic goes here
    r += 1

    # Catch-Up
    while (# catch-up conditional goes here)
      # catch-up logic goes here
      l += 1

  return ans
  

pwwkew
    r
  l

l = 2
r = 4
best_l = 2
best_r = 4
repeated_chars = 0
chars = {p->0, w->1, k->1}


def longest(s):
  l, r = 0, 0
  best_l, best_r = 0, 0
  chars = {}
  repeated_chars = 0
  
  while r < len(s):
    # hunting / expanding
    if repeated_chars == 0:
      if r - l > best_r - best_l:
        best_l, best_r = l, r

      chars[s[r]] = chars.get(s[r], 0) + 1

      if chars[s[r]] > 1:
        repeated_chars += 1

      r += 1

    while repeated_chars > 0:
      chars[s[l]] = chars.get(s[l], 0) - 1

      if chars[s[l]] == 1:
        repeated_chars -= 1

      l += 1

  return s[best_l:best_r]

    

Code

'''


def longest(s):
    l, r = 0, 0
    best_l, best_r = 0, 0
    chars = {}
    repeated_chars = 0

    while r < len(s):
        # hunting / expanding
        if repeated_chars == 0:
            if r - l > best_r - best_l:
                best_l, best_r = l, r

            chars[s[r]] = chars.get(s[r], 0) + 1

            if chars[s[r]] > 1:
                repeated_chars += 1

            r += 1

        while repeated_chars > 0:
            chars[s[l]] = chars.get(s[l], 0) - 1

            if chars[s[l]] == 1:
                repeated_chars -= 1

            l += 1

    return s[best_l:best_r]


print(longest("pwwkew"))

'''
Time complexity: O(n)
Space complexity: O(k) k = length of your alphabet/character set
'''
