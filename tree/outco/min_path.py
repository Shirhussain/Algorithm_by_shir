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
Explanation: The only leaf in this three is 6. There are five nodes on the path to this node,
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
             3

        9        20

               15   7


                  R
      BigFullTree     L

queue: bft_left, bft_right
new_node: L
'''
'''
Pseudocode

find_min_depth(node)
  bfs(node, depth):
    create queue containing (node, depth)
    while queue is not empty
      pop (new_node, new_depth) from queue
      if new_node is not null
        if new_node is a leaf:
          return new_depth of new_node
        push on queue (new_node's left child, new_depth+1)
        push on queue (new_node's right child, new_depth+1)

  return bfs(node, 1)
'''
