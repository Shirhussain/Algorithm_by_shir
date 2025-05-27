'''
Given a tree, create a serialized version (a string representation) that can subsequently
  be deserialized to produce exactly the same tree.

What kind of tree?

Binary tree, nodes have value, left, and right properties.
Given the root node.

node {
  value: int,
  left: node,
  right: node
}

Does the serialization need to have any particular properties, e.g., 
  represent a breadth-first traversal?

Example: No, I don't have an example.

Why? I want you to decide on the representation. Be creative.

Size constraints: Serialization should be linearly related to size of the tree.

'''
'''
                       1
                  2         3
                          4

Option 1: [1 | 2 3 | 2xnull 4 null]
Option 2: [1LR | 2 3L | 4]
Option 3: [1 2 null null 3 4 null null null]
Option 4: [1, [2, null, null], [3, [4, null, null], null]]
          If the input tree is null, null
Option 5: [1, [2, []], []]], [3, [4, []], []]], []]]]
If the input tree is null, []]


'''
'''
answer: 
                       1
                  2         3
                          4


'''
'''
serialize(root):

  if node is null
    return empty list
  else 
    create a list containing node.value
    append to list serialize(node.left)
    append to list serialize(node.right)
    return tne list
      

'''


'''
Design an algorithm to deserialize a serialized 
version of a binary tree.
Assume that each tree node has variables val,
left, and right. A serialized version of a nonempty subtree will be an array/list where the first 
element is the value of the root of the subtree,
the second element is a serialization of the
left subtree, and the third element is a serialization
of the right subtree. A serialized version of an
empty subtree is an empty array/list.
'''
'''

[1, [2, []], []]], [3, [4, []], []]], []]]]

               1
          2         3
                  4

'''
'''
          [1, [2, []], []]], [3, [4, [], []], []]]]

                          1
          [2, []], []]]        [3, [4, [], []], []]
                2                          3
            []    []          [4, [], []]      []
            null null             4            null
                              null null

'''
'''

deserialize(list):
  if list is empty
    return null
  else
    create node with value the first element of the list
    set node.left to deserialize(second element of list)
    set node.right to deserialize(third element of list)
    return node

'''


'''
Constraints:
Linear time in the size of the tree.
Linear space in the size of the tree.




















'''
'''
[a, 
  [b, 
    [d, 
      [g, [], []], 
      [h, [], []]], 
    [e, 
      [i, [], []], 
      []
    ] 
  ], 
  [c, 
    [], 
      [f, 
        [j, [], []], 
        [k, 
          [], 
            [l, [], []]
        ]
      ]
  ] 
]

                   a
        b                      c
  d          e                      f
g   h      i                      j   k
                                        l



Edge cases: Tree can be empty, in which case output should be null/None.

'''

'''
Diagram
                      
'''
'''
Pseudocode


  
'''
'''


'''
