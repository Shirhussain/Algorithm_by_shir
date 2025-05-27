class TreeNode:
    def __init__(self, value = None):
        self.value = value
        self.left = None 
        self.right = None
        

def preDFS(root):
    result = []
    def traverse(node):
        if node is None:
            return 
        result.append(node.value)
        traverse(node.left)
        traverse(node.right)

    traverse(root)
    return result


def pred_dfs_depth(root):
    result = []
    max_depth = -1
    def traverse(node, depth):
        nonlocal max_depth
        if node is None:
            return 
        max_depth = max(depth,max_depth)
        result.append(node.value)
        traverse(node.left, depth+1)
        traverse(node.right, depth+1)
    traverse(root, 0)
    return result, max_depth     


root = TreeNode(10)
root.left = TreeNode(8)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(5)
root.right.left = TreeNode(2)
print(preDFS(root))

"""
                10
               /  \
              8    2
            /  \   / 
           3    5 2


"""

print(pred_dfs_depth(root))


def pre_iterative(node):
    if root is None:
        return
    result = []
    stack = [node]
    while stack:
        current = stack.pop()
        result.append(current.value)
        
        # because I need to pop left side from the stack first so I need to add first right then left
        if current.right is not None:
            stack.append(current.right)
        if current.left is not None:
            stack.append(current.left)
    return result

print(pre_iterative(root))
