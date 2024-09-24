first read this: https://docs.google.com/document/d/1gb3HGTzR770yV3kLLhlmkLr4JiIs6MM_Oo50Lk3US9A/edit?usp=sharing

# How do I solve a recursion problem Systematically?

You should answer the following questions:

## What is the base case? E.g. F(0) = F(1) = 1

## What is the recursive function and its parameters and what are the parameters of the subproblems.

    We need to solve F(n-1) and F(n-2)

## How do I combine the solution of the subproblems?

    E.g. combine the result using ADD operation:
    F(n) = F(n-1) + F(n-2)

### Every recursion is really DFS on the corresponding recursion tree!

def dfs(node):
if is_leaf(node):
return
dfs(node.left)
dfs(node.right)

https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/description/
https://www.geeksforgeeks.org/convert-binary-tree-to-doubly-linked-list-by-keeping-track-of-visited-node/#

'''
Given a set of coins and a target sum, find the minimum number of coins needed to make the target sum.
Example:
coins = [1, 2, 5], target = 11
Output: 3
Explanation: 5 + 5 + 1 = 11

Solution: CoinChange(coins, target) - What are the subproblems? - CoinChange(coins, target - coin[i]) - How do we combine them? - MIN(CoinChange(coins, target - coin[i])) + 1 - What is the base case? - CoinChange(coins, 0) = 0 - CoinChange(coins, k<0) = +inf

'''

class Solution:
def coinChange(self, coins: List[int], amount: int) -> int:
if amount == 0:
return 0
if amount < 0:
return float("inf")
result = float("inf")

        for coin in coins:
            current = self.coinChange(coins, amount - coin)
            if current != -1:
                result = min(result, current + 1)

        return -1 if result == float("inf") else result

https://leetcode.com/problems/coin-change/submissions/1400243456

'''
Given a binary tree, find the maximum value in the tree.
Solution: - What are the subproblems? - find_max_value(node.left) - find_max_value(node.right) - Combining operator: - MAX(left, right, node.value) - Base case: - find_max_value(null) = -infinity
'''

class node:
def **init**(self, val):
self.val = val
self.left = None
self.right = None

def combine(left, right, node_val):
return max(left, right, node_val)

def find_max_value(node):
if node is None:
return float("-inf")
left = find_max_value(node.left)
right = find_max_value(node.right)

    return combine(left, right, node.val)

# https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/description/

# https://www.geeksforgeeks.org/convert-binary-tree-to-doubly-linked-list-by-keeping-track-of-visited-node/#

# https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/description/

# https://www.geeksforgeeks.org/convert-binary-tree-to-doubly-linked-list-by-keeping-track-of-visited-node/#

'''
Solution: BtToDLL(node) - What are the subproblems? - left = BtToDLL(node.left) - right = BtToDLL(node.right)

    - Combining operator?
        - APPEND(left, node, right)

    - What is the base case?
        - BtToDLL(None) = None

'''

def combine(left, node, right):
if left is None and right is None:
node.left = node
node.right = node
return node
elif left is None:
node.right = right
node.left = right.left
right.left.right = node
right.left = node
return node
elif right is None:
left.left.right = node
node.left = left.left
left.left = node
node.right = left
return left
else:
left.left.right = node
node.left = left.left
right.left.right = left
left.left = right.left
right.left = node
node.right = right
return left

def BtToDLL(node):
if node is None:
return None
left = BtToDLL(node.left)
right = BtToDLL(node.right)

    return combine(left, node, right)
