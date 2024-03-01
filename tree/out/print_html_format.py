'''
Given the root node of a tree that is not necessarily binary, 
print a text representation of the tree in outline form. 
Assume that each node has properties value and children.

Example:
                                html
                  head						     body
          meta   title  link              h1              p
                                                  span   br   span    

Output:

html
- head
  - meta
  - title
  - link
- body
  - h1
  - p
    - span
    - br
    - span
'''

from collections import deque


class Node:
    def __init__(self, value=None, children=[]):
        self.value = value
        self.children = children

    def print_node(self, node, indent=""):
        print(indent + node.value)

        for child in node.children:
            self.print_node(child, indent="    - ")


def pre_order_traverse(node):
    def helper(node, level=0):
        if level == 0:
            print(node.value)
        else:
            print("   " * level, "-", node.value)
        for child in node.children:
            helper(child, level+1)
    return helper(node)


html_format = Node('html', [
    Node('head', [
        Node('meta'),
        Node('title'),
        Node('link'),]),
    Node('body', [
        Node('h1'),
        Node('p', [
            Node('span'),
            Node('br'),
            Node('span')])]),
])


# node = Node()
# result = node.print_node(html_format)

pre_order_traverse(html_format)
