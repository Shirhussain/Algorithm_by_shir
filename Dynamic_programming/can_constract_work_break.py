"""
    Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

    Note that the same word in the dictionary may be reused multiple times in the segmentation.

    

    Example 1:

    Input: s = "leetcode", wordDict = ["leet","code"]
    Output: true
    Explanation: Return true because "leetcode" can be segmented as "leet code".

    Example 2:

    Input: s = "applepenapple", wordDict = ["apple","pen"]
    Output: true
    Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
    Note that you are allowed to reuse a dictionary word.

    Example 3:

    Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
    Output: false

    

    Constraints:

        1 <= s.length <= 300
        1 <= wordDict.length <= 1000
        1 <= wordDict[i].length <= 20
        s and wordDict[i] consist of only lowercase English letters.
        All the strings of wordDict are unique.



solution is: 
    input: s = "abcd" wordDict = ["a", "b", "c", "ab", "bc", "abc"]


                                            "abcd" 
                                -a /    ab|    abc|     abcd\
                                "bcd"    "cd"     "d"       "" 
                            b/  bc| bcd\  c/ cd\   d|   
                        "cd"   "d"   ""   "d"  ""   ""  
                    c/   cd|    d|         d| 
                    "d"   ""     ""         "" 
                    
                    
                    #or 
                    
                    
                                            "abcdef"
                                        ab/    abc|    abcd\
                                    cdef         def        ef 
                                     cd|         def|       
                                       ef           ""
"""


def can_construct(target, word_bank):
    if target == "":
        return True

    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word):]
            if can_construct(suffix, word_bank):
                return True
    return False


print(can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(can_construct("skateboard", [
      "bo", "rd", "ate", "t", "ska", "skk", "board"]))

# print(can_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeT", [
#       "e", "ee", "eee", "ef"]))


def can_construct_memo(target, word_banks, memo={}):
    if target in memo:
        return memo[target]

    if target == "":
        return True
    for word in word_banks:
        if target.startswith(word):
            suffix = target[len(word):]
            if can_construct_memo(suffix, word_banks, memo):
                memo[target] = True
                return True
    memo[target] = False
    return False


print(can_construct_memo("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(can_construct_memo("skateboard", [
      "bo", "rd", "ate", "t", "ska", "skk", "board"]))

print(can_construct_memo("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeT", [
      "e", "ee", "eee", "ef"]))
