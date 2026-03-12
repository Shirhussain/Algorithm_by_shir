""" 
In a simplified game of American football, teams score points by either achieving a touchdown (7 points) or a field goal (3 points).

Given the score for a single team, please return how many different permutations of touchdowns and/or field goals exist in order to arrive at that score.

Input: Integer
Output: Integer

Examples
Input:  10
Output: 2

Explanation: For a score of 10, the output would be 2. The 2 ways to arrive at
this score is to:

1) Score a field goal (3 points) and then touchdown (7 points)
2) Score a touchdown (7 points) and then field goal (3 points)


Input: 21
Output: 2

Explanation: For a score of 21, the output would be 2. The 2 ways to arrive at
this score is to:

1) Score 7 field goals (3 * 7 points)
2) Score 3 touchdowns (7 * 3 points)

Input: 24
Output: 5

8 3's
3 7's and 1 3
1 3 and 3 7's
1 7, 1 3, 2 7's
2 7's, 1 3, 1 7

Input:  16
Output: 4

Explanation: For a score of 16, the output would be 4. The 4 ways to arrive at
this score is to:

1) Score 1 touchdown (7 points) and 3 field goals (3 * 3 points)
2) Score 1 field goal (3 points), then 1 touchdown (7 points), and then 2 field goals (2 * 3 points)
3) Score 2 field goals (2 * 3 points), then 1 touchdown (7 points), and lastly 1 field goal (3 points)
4) Score 3 field goals (3 * 3 points) and then 1 touchdown (7 points)


Constraints
Time Complexity: O(2^N)
Auxiliary Space Complexity: O(N)
'''
'''
Diagram

                16
           7,1          3
        9                    13
    7,0    3,1
  2            6
 7 3       7,0  3,0+1
-5 -1      -1      3
x   x      x    7,0  3,1
                -4    0



you can score 7, or 3 

how many way exist to get to get to 16, 

input : 16, 
output: 4

              16
            7/    3\
           9       13 
        7/. 3\    7/  3\
        2.   6.  6     10
    7/. 3\
 -5     -1
"""

from collections import deque


def number_of_ways(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    return number_of_ways(n-7) + number_of_ways(n-3)


print(number_of_ways(16))


def number_of_way_bfs(n):

    def bfs(n):
        counter = 0
        q = deque([n])
        while q:
            node = q.popleft()
            if node == 0:
                counter += 1
            if node > 0:
                q.append(node-7)
                q.append(node-3)
        return counter
    return bfs(n)


print(number_of_way_bfs(16))
print(number_of_way_bfs(21))


def number_of_ways_memo(n, memo={}):
    if n == 0:
        return 1
    if n < 0:
        return 0
    if n in memo:
        return memo[n]

    memo[n] = number_of_ways_memo(n-7, memo) + number_of_ways_memo(n-3, memo)
    return memo[n]


print(number_of_ways_memo(21))
