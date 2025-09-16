'''
Given the root node of a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

The node structure is:

node
{
  val: int
  left: node
  right: node
}

'''
'''
Example:

Input: nodes p=5, q=1
                  3
            5            1
        6      2      0     8
              7 4
Output: 3

Input 2: p=5, q=4
Output: 5

                  1
              2
P=1, q=2
Output: 1

reversed:
[1]
[1,2]

Example 3:
                                    1

                          2                 3
                     4         5
                                  6
                                  
p=4, q=6
Output: 2

                                  
Assume at least 2 nodes in the tree, p and q are nodes in the tree and are distinct
Number of nodes is at most 10^5
Guaranteed that all node values are distinct

'''
'''
Diagram

                                    1
                  
                          2                 3
                          
                     4         5 
                     
                                  6
                                  
p=4, q=6
Output: 2

queue: [(2, [1,2]), (3, [1,3])]

[4, 2, 1]
[6, 5, 2, 1]

reversed:
[1,2,4]
[1,2,5,6]
'''

'''
Pseudocode:

def lca(root, p, q):

   def path_find_bfs(target):
        let queue be an empty queue
        add (root, [root.val]) to queue
        while queue is not empty
          remove (node, path) from front of queue
          if node == target:
             return path
          add (node.left, path + node.left.val) to the back of the queue
          add (node.right, path + node.right.val) to the back of the queue
          
   def path_find_dfs(target):
     let answer_path be empty
     def helper(node, path):
       if node is null
          return false
        if node == target:
          save a copy of path in answer_path
          return true
        add node.left.val to the end of path
        if helper(node.left, path):
          return true
        remove node.left.val from end of path
        add node.right.val to end of path
        right_val = helper(node.right, path)
        if right_val:
          return true
        remove node.right.val from end of path
        return false         

     helper(root, [root.val])
     return answer_path
   
   let p_path path_find(p)
   let q_path path_find(q)

   let i = 0
   while i is not outside either path and p_path[i] == q_path[i]
      increment i
   return p_path[i-1]
   
DFS: O(size of tree)
Aux. Space: O(height of tree)

'''