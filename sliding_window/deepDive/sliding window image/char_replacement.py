"""
The problem means after perfroming at most k changes, 
the entire substring should consist of only one reptead character.

Solution: Sliding window

- Note that the property is monotonic: as the size of the string increases,
the length of the potential substring with repeated charatcters either doesn't change or increases.

- Window state: a dictionary that holds the frequency of each character.
 l
"ABAXYZBBBBBBBBBBBBBBC"
           r

Min number of changes we need = (window size) - max_freq
    Keep the one with max freq, and change everything else


                l
Input: s = "AABABBA", k = 1
                  r

d:{a:1, b:2}
max_f = 2
r - l + 1 - max_frequency = 1

result = 4

"""

from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        d = defaultdict(int)
        result = 0
        max_frequency = 0

        for r in range(len(s)):
            # Update window state:
            d[s[r]] += 1
            max_frequency = max(max_frequency, d[s[r]])

            # If the cost of replacement is higher than what we are given
            # we can contract.
            while r - l + 1 - max_frequency > k:
                d[s[l]] -= 1
                l += 1

            result = max(result, r - l + 1)

        return result


# or
class Solution_2:
    def characterReplacement(self, s: str, k: int) -> int:
        # Input: s = "AABABBA", k = 1
        # new_dict = {1: "AA", 2: "B", 3: "A", 4:"BB", 5: "A"}

        # dic = {}
        # p0,maxs,maxcount = 0,0,0
        # for p1 in range(len(s)):
        #     print(p0, p1, maxs, maxcount)
        #     dic[s[p1]] = dic.get(s[p1],0) + 1
        #     if maxcount < dic[s[p1]]:
        #         maxcount = dic[s[p1]]
        #     while p1 - p0 - maxcount + 1 > k:
        #         dic[s[p0]] -= 1
        #         p0 += 1
        #     maxs = max(maxs,p1-p0+1)
        # return maxs

        count = {}
        result = 0
        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            result = max(result, r - l + 1)
        return result
