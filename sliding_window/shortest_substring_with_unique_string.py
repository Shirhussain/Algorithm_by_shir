'''
Shortest Substring With 3 Unique Characters
Given a string, return the shortest substring that has at least 3 unique characters, or false if there is no such string

Input: String
Output: String or Boolean
Example
Input: aabaca => Output: bac
Input: abaacc => Output: baac
Input: abc => Output: abc
Input: aabb => Output: False

abaacc
  l
    r

num_unique = 2
l = 1
r = 4
{b->0, a->2, c->1}


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

abaacc
     r
  l

r = 4
l = 1
best_r = 4
best_l = 1

char = {a->2, b->0, c->2}
num_unique = 2

Pseudocode

aabb
l
   r

r = 3
l = 0
best_r = inf
best_l = 0
char = {a->2, b->2}
num_unique = 2


def shortestWith3(s):
  l, r = 0, 0
  best_l = 0
  best_r = float('inf')
  chars = {}
  num_unique = 0

  for r in range(len(s)):
    # hunting
    if num_unique < 3:
      char_count = chars.get(s[r], 0)
      if char_count == 0:
        num_unique += 1

      chars[s[r]] = char_count + 1

      r += 1


    # catchup
    while num_unique >= 3:
      if r - l < best_r - best_l:
        best_l, best_r = l, r

      char_count = chars.get(s[l], 0)
      chars[s[l]] = char_count - 1
      if char_count == 1:
        num_unique -= 1

      l += 1

  if best_r != float('inf'):
    return s[best_l:best_r]
  else:
    return False

Code
'''


def shortestWith3(s):
    l, r = 0, 0
    best_l = 0
    best_r = float('inf')
    chars = {}
    num_unique = 0

    for r in range(len(s)):
        # hunting
        if num_unique < 3:
            char_count = chars.get(s[r], 0)
            if char_count == 0:
                num_unique += 1

            chars[s[r]] = char_count + 1

            r += 1

        # catchup
        while num_unique >= 3:
            if r - l < best_r - best_l:
                best_l, best_r = l, r

            char_count = chars.get(s[l], 0)
            chars[s[l]] = char_count - 1
            if char_count == 1:
                num_unique -= 1

            l += 1

    if best_r != float('inf'):
        return s[best_l:best_r]
    else:
        return False


print(shortestWith3(""))

'''
Time: O(n)
Space: O(1)

Time: Length of Array * Time spent per Window
    : How many times are you looking at each array element with l + ... r

Space: Window State Size
'''
