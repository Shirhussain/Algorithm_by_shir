class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def preorder_traversal(root):
    result = []

    def traverse(node):
        if node is None:
            return
        result.append(node.value)  # Process the root node (visit)
        traverse(node.left)        # Recur on the left subtree
        traverse(node.right)       # Recur on the right subtree

    traverse(root)
    return result


def preorder_traversal_iterative(root):
    if not root:
        return []
    stack, result = [root], []
    while stack:
        node = stack.pop()
        result.append(node.value)  # Visit the root node
        if node.right:
            stack.append(node.right)  # Push right child to stack
        if node.left:
            stack.append(node.left)   # Push left child to stack
    return result
