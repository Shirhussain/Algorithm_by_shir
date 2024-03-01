"""
Evaluate an Expression Tree

Given the root of a binary tree with interior nodes + or – and leaves that are numbers, compute the value of the expression represented by the tree. Assume nodes have value, left, and right as properties.

Input: 
                      +
             -	                  +
        -         +            5      6
     1    2     3    4
     
Output: 3  = (1-2) – (3+4) + (5+6) = -1 – 7 + 11


time (N)
space : height of three


solution is that because is in order traversal, because in in order we can go column by column
so it's process first let colum -> left child then parent and then right child
"""


class TreeNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def post_order(node):
    if node is None:
        return 0
    if not is_operator(node.value):
        return int(node.value)

    left_child = post_order(node.left)
    right_child = post_order(node.right)
    operation = node.value
    return apply(left_child, right_child, operation)


def apply(left, right, op):
    if op == '-':
        return left - right
    elif op == '+':
        return left + right
    else:
        raise ValueError('Invalid operation')


def is_operator(value):
    return value in ('+', '-', )


root = TreeNode('+',
                TreeNode('-',
                         TreeNode('-',
                                  TreeNode('1'),
                                  TreeNode('2')
                                  ),
                         TreeNode('+',
                                  TreeNode('3'),
                                  TreeNode('4')
                                  )
                         ),
                TreeNode('+',
                         TreeNode('5'),
                         TreeNode('6')
                         )
                )


print(post_order(root))
