""" 
Word Break II

Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]

Example 2:

Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.

Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []


"""


""" 
this is a back tracking 
        # good expalnation is here: https://www.youtube.com/watch?v=xIpKiLYN49U
        # inspired by this as well: https://www.youtube.com/watch?v=gFm1lEfnzUQ&list=PLKYEe2WisBTEY7eJBW7W-jbxlXCGb928P&index=4&t=559s
        
                                  catsanddog
                         "cat"  /        "cats" \
                       [sanddog]           [anddog]
                         "sand"|              "and"|
                             [dog]               [dog]
                               "dog"|                 "dog"|
                               
                
                    [cat, sand, dog]            [cats, and, dog ]

"""
from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        result, sub_set = [], []

        def backtrack(remaining_s):
            if len(remaining_s) == 0:
                result.append(" ".join(sub_set))
                return

            for word in wordDict:
                if remaining_s.startswith(word):
                    sub_set.append(word)
                    backtrack(remaining_s[len(word):])
                    sub_set.pop()

        backtrack(s)
        return result


sol = Solution()
print(sol.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
