
class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> map = new HashMap<>();
        int left =0, right = 0;
        int bestLen = 0;
        int dup = 0;

        // abba
        while (right < s.length()) {
            // 1. move right: hunting phase
            char rc = s.charAt(right); // a b b
            if (map.containsKey(rc) && map.get(rc) > 0) {
                dup++;  // 1
            } // b : 1
            map.put(rc, map.getOrDefault(rc, 0) + 1);
            right++; // 1 2 3

            while (dup >= 1) {
                System.out.println(left);
                // we have duplicate! need to move left, catchup phase
                char lc = s.charAt(left); // a b
                if (map.get(lc) > 1) {
                    // this is a duplicate letter
                    dup--; // 0
                }
                map.put(lc, map.get(lc) - 1); // 
                // if (map.get(lc) == 0) {
                //     map.remove(lc);
                // }

                left++; // 1 2
            }

            // no duplicate, we can get the length
            int curLen = right - left; // 1 2
            if (curLen > bestLen) {
                bestLen = curLen; // 1 2
            }
        }

        return bestLen;
    }
}