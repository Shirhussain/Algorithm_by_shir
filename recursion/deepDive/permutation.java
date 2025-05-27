/**
American Football Score

In a simplified game of American football, teams score points by either achieving a touchdown (7 points) or a field goal (3 points).

Given the score for a single team, please return how many different permutations of touchdowns and/or field goals exist in order to arrive at that score.

Input: Integer
Output: Integer

Examples:
Input:  10
Output: 2

Explanation: For a score of 10, the output would be 2. The 2 ways to arrive at
this score is to:

1) Score a field goal (3 points) and then touchdown (7 points) [3,7]
2) Score a touchdown (7 points) and then field goal (3 points) [7,3]


Input: 21
Output: 2

Explanation: For a score of 21, the output would be 2. The 2 ways to arrive at
this score is to:

1) Score 7 field goals (3 * 7 points) [7, 7, 7]
2) Score 3 touchdowns (7 * 3 points) [3, 3, 3, 3, 3, 3, 3]


Input:  16
Output: 4

Explanation: For a score of 16, the output would be 4. The 4 ways to arrive at
this score is to:

1) Score 1 touchdown (7 points) and 3 field goals (3 * 3 points) [7,  3 3 3]
2) Score 1 field goal (3 points), then 1 touchdown (7 points), and then 2 field goals (2 * 3 points)
3) Score 2 field goals (2 * 3 points), then 1 touchdown (7 points), and lastly 1 field goal (3 points)
4) Score 3 field goals (3 * 3 points) and then 1 touchdown (7 points)


                                        10
                                    3.      7(3)
                                3      7.  3  7
                                       0.  0
                                       
                                       
                                       16
                            3(13).            7(9)
                        3(10).   7(6).      3(6)    .    
                            
                            
               given a target, tell me how many solutions we can get to the target by using 3 and 7 unlimited
               3
               7
                                       

 */

import java.util.*;
public class MyClass {
    public static void main(String args[]) {
        int target = 16;
        int count = getSolutionCount(target);
        System.out.println(count);
    }
    
    static int res = 0;
    
    static int getSolutionCount(int target) {
        // helper(target);
        
        // return res;
        
        // return helper2(target);
        
        int[] count = {0};
        helper3(target, count);
        
        return count[0];
    }
    
    // Input 10, Output 2. 
    // 10000 -2 -4
    // target = 10, res = 2
    // target = 21, res = 2
    static Set<Integer> set = new HashSet<>();
    
    static void helper(int target) {
      if (set.contains(target)) {
          System.out.println("visited: " + target);
      }
      set.add(target);
      // when should we increase res/count
      // when we reach the end == target == 0
      if (target == 0) {
          res++;
          return;
      }
      
      if (target < 0) {
          return;
      }
      // 16, 13
      // 16, 9 
      // try the 2 scores
      helper(target - 3);
      helper(target - 7);
    }
    
    
    static int helper2(int target) {
        if (target == 0) {
            return 1;
        }
        
        if (target < 0) {
            return 0;
        }
        
        int leftCount = helper2(target - 3);
        int rightCount = helper2(target - 7);
        
        return leftCount + rightCount;
    }
    
    static void helper3(int target, int[] count) {
        if (target == 0) {
            count[0] += 1;
            return;
        }
        
        if (target < 0) {
            return;
        }
        
        helper3(target - 3, count);
        helper3(target - 7, count);
    }
    

/**
"ab" -> ["ab", "ab", "Ab", "aB", "AB"]

                ab

            a.   A.    b.  B

abcd

abC
abc

aBc
aBC

AbC
Abc


ABC
ABc

 */


class Solution {
    public List<String> letterCasePermutation(String s) {
        List<String> res = new ArrayList<>();
        helper(s, 0, "", res);

        return res;
    }

    // curStr is the path, 
    // "aab" -> ["ab", "ab", "Ab", "aB", "AB"]
    // a -> a, A
    // ab, aB, Ab, AB
    void helper(String originalStr, int pos, String curStr, List<String> res) {
        // when the pos reaches the end of original string, add current string to res
        if (pos == originalStr.length()) {
            res.add(curStr);
            return;
        }

        char curChar = originalStr.charAt(pos);

        if (Character.isLetter(curChar)) {
            helper(originalStr, pos + 1, curStr + Character.toLowerCase(curChar), res);
            helper(originalStr, pos + 1, curStr + Character.toUpperCase(curChar), res);
        } else {
            // curChar is a number!
            helper(originalStr, pos + 1, curStr + curChar, res);
        }
 
    }
}
    
    
    
    
    
    
    
    
    
    
    
    
    
}


/**
    [1, 2, 3, 4]

            []
      [1].               [2]             [3].    [4]   
    [12] [13] [14].     [23] [24].      [34].     




 */


class Solution {
    public List<List<Integer>> combine(int n, int k) {
        int[] nums = getArray(n);

        List<List<Integer>> res = new ArrayList<List<Integer>>();
        List<Integer> list = new ArrayList<Integer>();
        helper(res, list, nums, k, 0);

        return res;
    }

    void helper(List<List<Integer>> res, List<Integer> list, int[] nums, int k, int pos) {
        if (list.size() == k) {
            res.add(new ArrayList<Integer>(list));
            return;
        }

        // try all the new elements which are after me
        for (int i = pos; i< nums.length; i++ ) {
            list.add(nums[i]); // try it
            helper(res, list, nums, k, i + 1); // recursion
            list.remove(list.size() - 1); //remove it
        }
    }


    private int[] getArray(int n) {
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) {
            nums[i] = i + 1;
        }
        return nums;
    }
}


// [1, 2, 3, 4]
// [1, 2] [1, 3] [14] [23] [24] [34]

class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        List<Integer> list = new ArrayList<Integer>();
        helper(res, list, nums);

        return res;
    }

    // [1,2,3]
    // list = [1..] [2..] [3..]
    // [1..] -> [1 2] [1 3]
    // [1 2] -> [1 2 3] Great
    // [1 2] -> [1] -> [1 3] -> [1 3 2] Great

    // [1]


    //                 []
    //          [1].            [2].             [3]
    //       [1 2]. [1 3]     [2 1] [2 3]     [3 1].  [3 2]
    //    [123]       [132]   [213]




    // for efficiency, O(1) lookup in set. need to have a set, when you add a letter to list, add to set too.
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
}