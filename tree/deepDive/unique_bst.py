""" 
Unique Binary Search Trees

Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

 

Example 1:


Input: n = 3
Output: 5
Example 2:

Input: n = 1
Output: 1



solution:
if we have [1,2,3..... n]
then for each element i in the list we can make it as the root of the BST and 
the left subtree will be the elements less than i and the right subtree will be
the elements greater than i.

so we can use a recursive approach to solve this problem.

we can use a helper function to generate the BST for each element i in the list.
or do it with dynamic programming 


[1,2,3..... n]
    i -> root
    j-1 -> left subtree
    n-j -> right subtree
dp[i] = sum of dp[j-1] * dp[i-j] for all j from 1 to i
                         
        When j is root:
              j
             / \
          j-1   n-j


"""


def unique_bst(n):
    dp = [0] * (n+1)
    dp[0] = 1  # if we have 0 nodes, we have 1 BST
    dp[1] = 1  # if we have 1 node, we have 1 BST

    for i in range(2, n+1):
        for j in range(1, i+1):
            dp[i] += dp[i-j] * dp[j-1]

    return dp[n]


print(unique_bst(3))
print(unique_bst(1))
