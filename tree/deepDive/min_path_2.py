'''
Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Input: Node in a Binary Tree
Output: Integer
'''
'''
Examples:

Input:
             3

        9        20

               15   7
Output: 2
Explanation: 9 is a leaf and there are two nodes on the path to this leaf, 3 and 9.
15 and 7 are also leaves, but there are three nodes on the paths to these leaves.

Input:

     2
        3
          4
            5
              6
Output: 5
Explanation: The only leaf in this tree is 6. There are five nodes on the path to this node,
2, 3, 4, 5, and 6.
'''
'''
Constraints:

Let D be the depth of the shallowest leaf, N the number of nodes in the tree.
Time complexity: O(min(N, 2^D))
Auxilliary space complexity: O(min(N, 2^D))

'''

'''
Diagram

               3,1
          
          9,2        20,2
          
     17,3         15,3   7,3

        5,4

queue: 17, 15, 7
'''

'''
Pseudocode

bfs(node):
create a queue
push (node,1) onto queue
while queue is not empty
   remove (new_node,level) from the front of the queue
   if node is a leaf (has no children) then return level
   push (new_node's left_child, level+1) onto queue
   push (new_node's right_child, level+1) onto the queue
  
'''
'''
if root is None:
    return 0
result = 0
q = deque([root])

while q:
    result += 1
    my_len = len(q)
    for i in range(my_len):
        node = q.popleft()
        if node:
            if node.left is None and node.right is None:
                return result
            q.append(node.left)
            q.append(node.right)
return result
'''
