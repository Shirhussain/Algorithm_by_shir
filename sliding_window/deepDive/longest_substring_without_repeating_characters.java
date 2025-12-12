""" 
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

""" 
class Solution {
    public int lengthOfLongestSubstring(String s) {
        int left = 0; // catchup. slower
        int right = 0; // hunting, faster
        int bestLen = 0;
        Map<Character, Integer> map = new HashMap<>();
        boolean hasDuplicate = false;

        while (right < s.length()) {
            // move right, hunting
            char rc = s.charAt(right);
            // need to check if this char is a duplicate
            if (map.containsKey(rc) && map.get(rc) > 0) {
                // duplicate! do sth!
                hasDuplicate = true;
            }

            map.put(rc, map.getOrDefault(rc, 0) + 1);
            right++;
            // done with hunting

            // when should we catch up, when should the left pointer move right?
            while (hasDuplicate) {
                // catch up phase
                char lc = s.charAt(left);
                // remove the duplicate, how
                if (map.get(lc) > 1) {
                    // this is a duplicate letter
                    hasDuplicate = false; // will remove the letter
                }
                map.put(lc, map.get(lc) - 1);
                left++;
            }

            // if there is no duplicate in current substring
            int curLen = right - left; // + 1
            bestLen = Math.max(curLen, bestLen);
        }


        return bestLen;
    }

    public int lengthOfLongestSubstring2(String s) {
        // iteratations
        // how we create the window?
        // from the left, double for loop
        // check duplicates: map,set

        Set<Character> set = new HashSet<>();
        int result = 0; // global longest to track the longest

        for (int i = 0; i < s.length(); i++) { // starting point
            int cur = 0; // what is the longest from this starting point
            set = new HashSet<>();

            for (int j = i; j < s.length(); j++) { // end point
                char c = s.charAt(j);
                if (set.contains(c)) { // O(1)
                    break; // dont move the ending point forward any more
                }
                set.add(c); // O(1)
                cur++;
            }

            result = Math.max(result, cur);
        }
        return result;
    }
}