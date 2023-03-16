from collections import deque

class Tree(object):
    def __init__(self, val, left=None, right=None):
        self.val = val 
        self.left = left 
        self.right = right 
        

def build_tree(arr):
    if not arr:
        return
    mid = len(arr)//2
    root = Tree(arr[mid])
    root.left = build_tree(arr[:mid])
    root.right = build_tree(arr[mid+1:])
    return root 


def level_order_traversal(node):
    if not node:
        return 
    q = deque([node])
    while q:
        current_node = q.popleft()
        print(current_node.val)
        
        if current_node.left is not None:
            q.append(current_node.left)
        if current_node.right is not None:
            q.append(current_node.right)
            


lst = [5, 2, 7, 1, 6, 8, 3, 4]
sorted_lst = sorted(lst)
root = build_tree(sorted_lst)

level_order_traversal(root)