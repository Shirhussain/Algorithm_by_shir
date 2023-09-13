'''
Longest Path of a Binary Tree

Given a binary tree node, return the number of nodes in the longest path between the root and a leaf node

Input: Node in a Binary Tree
Output: Integer


            1
      /         \
      2            3
                      \
                       4

Output: 3

Time Complexity: O(N)
Auxiliary Space Complexity: O(N)
Use a recursive dfs
Make good use of postorder search

max_path_length(node)

  dfs(node)
     if node is not null
        left_max_length = dfs(node's left child)
        right_max_length = dfs(node's right child)
        return max(left_max_length, right_max_length) + 1
      else
        return 0

  return dfs(node)

'''
