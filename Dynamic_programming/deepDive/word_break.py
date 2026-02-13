"""
Word Break

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



graph TB
    ROOT["dfs(0)<br/>remaining: <b>catsanddog</b><br/>try all prefixes from index 0"]

    ROOT -->|"s[0:3] = 'cat' ✅ in dict"| D3A["dfs(3)<br/>remaining: <b>sanddog</b>"]
    ROOT -->|"s[0:4] = 'cats' ✅ in dict"| D4["dfs(4)<br/>remaining: <b>anddog</b>"]

    D3A -->|"s[3:7] = 'sand' ✅ in dict"| D7A["dfs(7)<br/>remaining: <b>dog</b>"]

    D7A -->|"s[7:8] = 'd' ✅ in dict"| D8A["dfs(8)<br/>remaining: <b>og</b>"]
    D7A -->|"s[7:10] = 'dog' ✅ in dict"| D10A["dfs(10) 🟢<br/>i == len(s)<br/>return True"]

    D8A -->|"s[8:9]='o' ❌<br/>s[8:10]='og' ❌<br/>no match"| F8A["return False 🔴"]

    D4 -->|"s[4:6] = 'an' ✅ in dict"| D6["dfs(6)<br/>remaining: <b>ddog</b>"]
    D4 -->|"s[4:7] = 'and' ✅ in dict"| D7B["dfs(7)<br/>remaining: <b>dog</b><br/>⚠️ DUPLICATE of dfs(7) above"]

    D6 -->|"s[6:7] = 'd' ✅ in dict"| D7C["dfs(7)<br/>remaining: <b>dog</b><br/>⚠️ DUPLICATE of dfs(7) above"]

    D7B -->|"s[7:8] = 'd' ✅"| D8B["dfs(8)<br/>remaining: <b>og</b><br/>⚠️ DUPLICATE"]
    D7B -->|"s[7:10] = 'dog' ✅"| D10B["dfs(10) 🟢<br/>return True"]

    D8B -->|"no match"| F8B["return False 🔴"]

    D7C -->|"s[7:8] = 'd' ✅"| D8C["dfs(8)<br/>remaining: <b>og</b><br/>⚠️ DUPLICATE"]
    D7C -->|"s[7:10] = 'dog' ✅"| D10C["dfs(10) 🟢<br/>return True"]

    D8C -->|"no match"| F8C["return False 🔴"]

    style ROOT fill:#e94560,stroke:#fff,color:#fff
    style D10A fill:#2d6a4f,stroke:#95d5b2,color:#fff
    style D10B fill:#2d6a4f,stroke:#95d5b2,color:#fff
    style D10C fill:#2d6a4f,stroke:#95d5b2,color:#fff
    style F8A fill:#922,stroke:#f66,color:#fff
    style F8B fill:#922,stroke:#f66,color:#fff
    style F8C fill:#922,stroke:#f66,color:#fff
    style D7B fill:#533483,stroke:#e94560,color:#fff
    style D7C fill:#533483,stroke:#e94560,color:#fff
    style D8B fill:#533483,stroke:#e94560,color:#fff
    style D8C fill:#533483,stroke:#e94560,color:#fff
"""

from typing import List 
from functools import cache

def wordBreak(s: str, wordDict: List[str]) -> bool:

    @cache
    def dfs(i):
        if i == len(s):
            return True 
        
        for end in range(i+1, len(s)+1):
            prefix = s[i:end]
            if prefix in wordDict:
                if dfs(end):
                    return True 
        return False 
    return dfs(0)



s = "applepenapple"
wordDict = ["apple","pen"]


print(wordBreak(s, wordDict))


