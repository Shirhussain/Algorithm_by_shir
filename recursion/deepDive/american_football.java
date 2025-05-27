/**
 American Football Score

In a simplified game of American football, teams score points by either achieving a touchdown (7 points) or a field goal (3 points).

Given the score for a single team, please return how many different permutations of touchdowns and/or field goals exist in order to arrive at that score.

Input: Integer
Output: Integer

Examples:
Input:  10
Output: 2

3 + 7 = 10
7 + 3 = 10

use a moving target, starting with input 10
deduct by 3, 7 every time
take 0 as base: when 0 happens it is a working solution

Explanation: For a score of 10, the output would be 2. The 2 ways to arrive at
this score is to:

1) Score a field goal (3 points) and then touchdown (7 points)
2) Score a touchdown (7 points) and then field goal (3 points)


Input: 21
Output: 2

3 3 3 3 3 3 3 = 21
7 7 7 = 21

Explanation: For a score of 21, the output would be 2. The 2 ways to arrive at
this score is to:

1) Score 7 field goals (3 * 7 points)
2) Score 3 touchdowns (7 * 3 points)


Input:  16
Output: 4

3 3 3 7 = 16
....

Explanation: For a score of 16, the output would be 4. The 4 ways to arrive at
this score is to:

1) Score 1 touchdown (7 points) and 3 field goals (3 * 3 points)
2) Score 1 field goal (3 points), then 1 touchdown (7 points), and then 2 field goals (2 * 3 points)
3) Score 2 field goals (2 * 3 points), then 1 touchdown (7 points), and lastly 1 field goal (3 points)
4) Score 3 field goals (3 * 3 points) and then 1 touchdown (7 points) 


                                                                    10
                                        
                                        ([3], 7)                                ([7], 3)
                        
                            ([3, 3], 4).  ([3, 7], 0).                          ([...], 4)
                    
                    ([3, 3, 3], 1) ([3, 3, 7], -3)
                
        ([3, 3, 3, 3], -2). ([3, 3, 3, 7], -6)


 */
 import java.util.*;
public class MyClass {
    static int count = 0;
    // cache[4] = 0
    
    static void getCount(int target) { // 10, 7, 4, 1, -2. // 3
        // base condition
        if (target == 0) {
            count += 1;
            return;
        }
        
        if (target < 0) {
            return;
        }
        
        // recursion
        // -3, -7
        // ([7, 3], target = 0)
        getCount(target - 3); // ([], target = 10) ([3], target = 7), ([3, 3], 4), ([3, 3, 3], 1), ([3, 3, 3, 3], -2)
        getCount(target - 7); // ([7], target = 3)
        
        // ([3, 3, 3], 1) -> ([3, 3, 3, 7], -6)
        // ([3, 3], 4) -> ([3, 3, 7], -3)
        // ([3], target = 7) -> ([3, 7], target = 0) => count = 1
        // ([], target = 10) -> ([7], target = 3) -> ([7, 3], target = 0) => count = 2
    }
    
    static int getCount2(int target) { // 10, 7, 4, 1, -2. // 3
        // base condition
        if (target == 0) {
            return 1;
        }
        
        if (target < 0) {
            return 0;
        }
        
        int count3 = getCount2(target - 3); 
        int count7 = getCount2(target - 7);
        
        return count3 + count7;
        
    }
    
    static int getCount3(int target) {
        // hold targets
        Stack<Integer> stack = new Stack<Integer>();
        stack.push(target); // 0
        int count = 0;
        
        if (target == 0) {
            return 0;
        }
        
        while (!stack.isEmpty()) {
            // get the last element
            int cur = stack.pop();  // 0
            
            // do some operations on this current element
            if (cur == 0) {
                count++; // count = 1
            }
            
            if (cur < 0) {
                continue;
            }
            
            stack.push(cur - 3);
            stack.push(cur - 7);
            
        }
        
        return count;
    }
    
    public static void main(String args[]) {
      int res = getCount3(1);

      System.out.println("Count = " + res);
    }
}
