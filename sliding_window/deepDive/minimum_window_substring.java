""" 
Minimum Window Substring

Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

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

class Solution {
    public String minWindow(String s, String t) {
        Map<Character, Integer> map = new HashMap<>();
        for (char c : t.toCharArray()) {
            map.put(c, map.getOrDefault(c, 0) + 1);
        }

        int left = 0, right = 0;
        String res = "";
        int count = t.length();
        int bestLen = s.length();

        // a a
        while (right < s.length()) { // 0
            // hunting phase, move right
            char rc = s.charAt(right); // a
            if (map.containsKey(rc) && map.get(rc) > 0) {
                // found it!
                count--; // when it is 0, we found all the letters! // 0
            }
            map.put(rc, map.getOrDefault(rc, 0) - 1); // a:0
            right++; // 1

            // catching up phase
            while (count == 0) {
                // all elements found, we can catch up (shrink the substring, move left pointer to the right)
                // before shrinking, get one result
                if (right - left <= bestLen) {
                    bestLen = right - left; 
                    res = s.substring(left, right); // +1?
                }

                // now, shrink
                char lc = s.charAt(left);
                if (map.get(lc) >= 0) {
                    count++;
                }
                map.put(lc, map.get(lc) + 1);
                left++;
            }
        }



        return res;
    }
}