""" 
Find All Anagrams in a String

Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

 

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

"""

from collections import defaultdict


class Solution:
    def find_anagram(self, s: str, p: str):
        p_dict = defaultdict(int)
        s_dict = defaultdict(int)
        result = []

        for c in p:
            p_dict[c] = p_dict.get(c, 0)+1

        l = 0
        for r in range(len(s)):
            s_dict[s[r]] += 1

            if r - l + 1 > len(p):
                s_dict[s[l]] -= 1
                if s_dict[s[l]] == 0:
                    del s_dict[s[l]]
                l += 1

            if r - l + 1 == len(p) and s_dict == p_dict:
                result.append(l)
        return result


print("#####\nTest Case 1\n#####")
s = "cbaebabacd"
p = "abc"
solution = Solution()
print(solution.find_anagram(s, p))

print("#####\nTest Case 2\n#####")
s = "abab"
p = "ab"
solution = Solution()
print(solution.find_anagram(s, p))
