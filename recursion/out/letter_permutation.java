

    public List<String> letterCasePermutation(String s) {
        List<String> res = new ArrayList<String>();

        helper(res, s, 0, ""); // ([], aBc, 0, "")
        return res;
    }

    void helper(List<String> res, String s, int pos, String cur) {
        if (pos == s.length()) {
            res.add(cur); // [abc, abC, aBc, aBC, A...]
            return;
        }

        char curChar = s.charAt(pos); // a B c
        
        // ([], aBc, 1, "a")
        if (Character.isLetter(curChar)) {
            // lower case, StringBuilder, StringBuffer
            helper(res, s, pos + 1, cur + Character.toLowerCase(curChar));
            // upper case
            helper(res, s, pos + 1, cur + Character.toUpperCase(curChar));
        } else {
            // a number
            helper(res, s, pos + 1, cur + curChar);
        }
    }

    Map<Integer, Integer> map = new HashMap<>();

    public int combinationSum4(int[] nums, int target) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> list = new ArrayList<Integer>();

        helper(res, list, nums, target);
        return res.size();
    }

    void helper(List<List<Integer>> res, List<Integer> list, int[] nums, int target) {
        if (target == 0) {
            res.add(new ArrayList<Integer>(list));
            return;
        }
        if (target < 0) {
            return;
        }
        for (int num : nums) {
            list.add(num);
            helper(res, list, nums, target - num);
            list.remove(list.size() - 1);
        }
    }

    public int combinationSum43(int[] nums, int target) {
        
        return helper2(nums, target);
    }

    int helper2(int[] nums, int remaining) {
        if (remaining == 0) {
            return 1; // pick nothing is one solution
        }
        if (remaining < 0) {
            return 0;
        }

        if (map.containsKey(remaining)) {
            return map.get(remaining);
        }

        int res = 0;
        for (int num : nums) {
            res += helper2(nums, remaining - num);
        }

        map.put(remaining, res);
        return res;
    }

    public List<String> letterCasePermutation(String s) {
        List<String> res = new ArrayList<String>();

        helper(res, s, 0, new StringBuilder()); // ([], aBc, 0, "")
        return res;
    }

    void helper(List<String> res, String s, int pos, StringBuilder sb) {
        if (pos == s.length()) {
            res.add(sb.toString()); // [abc, abC, aBc, aBC, A...]
            return;
        }

        char curChar = s.charAt(pos); // a B c
        char[] options = {Character.toLowerCase(curChar), Character.toUpperCase(curChar)};
        
        if (Character.isLetter(curChar)) {
            for (char charOption : options) {
                sb.append(charOption); // try
                helper(res, s, pos + 1, sb); // next recursion
                sb.setLength(sb.length() - 1); // remove
            }
        } else {
            sb.append(curChar); // try
            helper(res, s, pos + 1, sb); // next recursion
            sb.setLength(sb.length() - 1); // remove
        }
    }

    void helper(List<List<Integer>> res, List<Integer> list, int[] nums) {
        if (list.size() == nums.length) {
            res.add(new ArrayList<Integer>(list));
            return;
        }

        // iterate through the nums
        for (int i = 0; i < nums.length; i++) {
            // duplicate check
            if (list.contains(nums[i])) {
                continue;
            }

            list.add(nums[i]); // try it
            helper(res, list, nums); // next round
            // backtracking
            list.remove(list.size() - 1); // remove it
        }
    }