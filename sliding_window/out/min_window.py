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




from collections import Counter
def minWindow(s: str, t: str) -> str:
    if t == "":
        return ""
    countT, window = {}, {}
    for c in t:
        countT[c] = 1 + countT.get(c, 0)
    have, need = 0, len(countT)
    # this is a default value for result it's a pointer like [l,r]
    # but i give a -1 as defualt also for eresult too
    result, len_result = [-1, -1], float("infinity")
    l = 0
    for r in range(len(s)):
        c = s[r]
        window[c] = 1 + window.get(c, 0)
        if c in countT and window[c] == countT[c]:
            have += 1
        while have == need:
            # update our result
            # update window < len_result
            if (r-l + 1) < len_result:
                result = [l, r]
                len_result = (r-l+1)

            # pop from left of the window
            window[s[l]] -= 1
            if s[l] in countT and window[s[l]] < countT[s[l]]:
                have -= 1
            l += 1
    l, r = result
    return s[l: r+1] if len_result != float("infinity") else ""


# def minimum_window_sub_str(s, t):
#     if len(s) < len(t):
#         return ""
#     if s == t:
#         return s
#     result = []
#     for i in range(len(s)):
#         for j in range(i, len(s)):
#             count = Counter(t)
#             for n in t:

#                 if n in s[i:j+1]:
#                     count[n] -= 1
#                     print(count, s[i:j+1])

#             if count.most_common()[0][1] == 0:

#                 result.append(s[i:j+1])
#             # if count >= len(t) and len(s[i:j+1]) >= len(t):
#             #     result.append(s[i:j+1])
#     print(result)
#     if result:
#         return min(result, key=len)
#     return ""


s = "ADOBECODEBANC"
t = "ABC"
print(minWindow(s, t))
# print(minimum_window_sub_str(s, t))
