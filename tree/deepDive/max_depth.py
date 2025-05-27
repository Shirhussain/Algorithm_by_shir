from typing import Optional

from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None 
        self.right = None
        
    def insert(self, new_node):
        if self.value:
            if new_node > self.value:
                if self.right is None:
                    self.right = Node(new_node)
                else:
                    self.right.insert(new_node)
            elif new_node < self.value:
                if self.left is None:
                    self.left = Node(new_node)
                else:
                    self.left.insert(new_node)
        else:
            self.value = Node(new_node)
            
        
    # def insert(self, data):
    # # Compare the new value with the parent node
    #     if self.value:
    #         if data < self.value:
    #             if self.left is None:
    #                 self.left = Node(data)
    #             else:
    #                 self.left.insert(data)
    #         elif data > self.value:
    #             if self.right is None:
    #                 self.right = Node(data)
    #             else:
    #                 self.right.insert(data)
    #     else:
    #         self.value = data
        
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.value)
        if self.right:
            self.right.print_tree()


def max_depth(root):
    if root is None:
        return 0
    # max_left = max_depth(root.left) + 1
    # max_right = max_depth(root.right) + 1
    # return max(max_left, max_right)
    # or 
    return 1 + max(max_depth(root.left), max_depth(root.right))


def max_dfs_depth(root):
    if root is None:
        return 0
    stack = [(root, 1)]
    max_depth = 1
    while stack:
        node, depth = stack.pop()
        max_depth = max(depth, max_depth)
        if node.left is not None:
            stack.append((node.left, depth + 1))
        if node.right is not None:
            stack.append((node.right, depth +1))
    return max_depth



def max_bfs_depth(root):
    if root is None:
        return 0
    
    q = [root]
    len_current_q = len(q)
    depth = 1
    
    while q:
        curr = q.pop(0)
        if curr.left:
            q.append(curr.left)
        if curr.right:
            q.append(curr.right)
        len_current_q -= 1
        if len_current_q == 0:  # Visited all for this depth
            depth += 1
            len_current_q = len(q)  # Remaining nodes are at next depth
    return depth


# Iterative DFS solution using a stack
def maxDepth(root) -> int:
    if not root:
        return 0
        
    dque = deque([root])
    nodes_at_curr_depth = len(dque)
    depth = 1
    
    while dque:
        node = dque.popleft()
        if node.left:
            dque.append(node.left)
        if node.right:
            dque.append(node.right)
    
        nodes_at_curr_depth -= 1
        if nodes_at_curr_depth == 0: # Visited all for this depth
            depth += 1
            nodes_at_curr_depth = len(dque) # Remaining nodes are at next depth
            
    return depth
        
tree = Node(12)
tree.insert(6)
tree.insert(14)
tree.insert(3)
tree.print_tree()

print("max depth: ",max_depth(tree))
print("max_depth: ", max_dfs_depth(tree))
print("max bfs depth: ", max_bfs_depth(tree))
print("max dfs depth: ", maxDepth(tree))