""" 
# https://leetcode.com/problems/word-break-ii/description/

140. Word Break II

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
 

Constraints:

1 <= s.length <= 20
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 10
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
Input is generated in a way that the length of the answer doesn't exceed 105.


Diagram

answer: ["cat sand dog"]

											catsanddog,""
                                    cat	/						\cats
                            sanddog,"cat"                  anddog
                            sand/
                        dog, "cat sand"
                        dog/
                        "", "cat sand dog"
    
    
    dict: ["a","aa","aaa", "aaaa", ..., "aaaaaaaaaa"]
    
    											    "aaaaaaaaaaaaaaaaaaaa",""
            "a"  "aa" "aaa" .....                       "aaaaaaaaaa"  (10 branches)  
       

Pseudocode

def word_break(s, wordDict):

	create empty answer_list
  
  def helper(s, sentence):
  	if s is empty
    	append copy sentence to answer_list
    for each word in wordDict
    	if word is a prefix of s
      	remove word from front of s, giving s'
        add space (possibly) and word to sentence
        helper(s', sentence)
        remove space and word from sentence
  
  helper(s, "")
  
  return answer_list

"""


from typing import List


def word_break(s, dic):
    result = []

    def prefix(word, _s):
        for i in range(len(s)):
            if _s[:i+1] == word:
                return True
        return False

    def remove_prefix(word, s):
        rest_s = s[len(word):]
        return rest_s

    def dfs(path, s, memo={}):
        if len(s) == 0:
            result.append(path.lstrip())
            return

        for word in dic:
            if prefix(word, s):
                new_s = remove_prefix(word, s)
                dfs(path+" " + word, new_s, memo)

                # or by backtracking

                # curr_path = path+" " + word
                # dfs(curr_path, new_s)

                # curr_path[:(len(curr_path) - len(word))+1]

    dfs("", s)
    return result


s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]

print(word_break(s, wordDict))


def wordBreak_backtrack(s: str, wordDict: List[str]) -> List[str]:
    """ this is a back tracking 
    # good expalnation is here: https://www.youtube.com/watch?v=xIpKiLYN49U

                              catsanddog
                     "cat"  /        "cats" \
                   [sanddog]           [anddog]
                     "sand"|              "and"|
                         [dog]               [dog]
                           "dog"|                 "dog"|


                [cat, sand, dog]            [cats, and, dog ]

    """
    result = []
    sub_str = []

    def backtrack(remaining_s):
        if len(remaining_s) == 0:
            result.append(" ".join(sub_str))
            return

        for word in wordDict:
            if remaining_s.startswith(word):
                sub_str.append(word)
                backtrack(remaining_s[len(word):])
                sub_str.pop()
    backtrack(s)
    return result
