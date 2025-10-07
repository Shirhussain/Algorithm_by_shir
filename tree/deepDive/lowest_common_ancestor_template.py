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
p=4, q=6
                                     []
                                      1
                               [1]        [1]
                          2                 3
                      [1,2]  [1,2]
                     4         5 
                              [1,2,5]
                                  6

find path to 4: [1,2,4]
find path to 6: [1,2,5,6]


'''
'''

Pseudocode:
  p_path = path_finder(root, p)
  q_path = path_finder(root, q)
  step along paths until they diverge; last element before divergence is the LCA!

path_finder(root, search_node):
  define answer_variable
  def pre_order(node, path):
    if node is null
      return
    if node == search_node
      copy path to answer_variable and append node
    modified_info = append node to path
    pre_order(node.left, modified_info)
    pre_order(node.right, modified_info)
    remove node from path
  pre_order(root, empty_info)
  return answer_variable
'''