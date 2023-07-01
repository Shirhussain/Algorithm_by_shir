class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Solution:
    def post_order(self, root):
        result = []

        def helper(node):
            if node is None:
                return
            helper(root.left)
            helper(root.right)
            result.append(node.value)
        helper(root)
        return result

    def add_node(self, root, new_node):
        node = Node(new_node)
        if root is None:
            root = node
        if root.value > node:
            if root.left is None:
                root.left = Node(new_node)
            else:
                root.left.add_node(root.left, new_node)
        elif root.right is not None:
            root.right.add_node(root.right, new_node)
        else:
            root.right = Node(new_node)


tree = Solution()
tree.add_node(tree, 4)
tree.add_node(tree, 1)
tree.add_node(tree, 2)
tree.add_node(tree, 3)
tree.add_node(tree, 4)
tree.add_node(tree, 5)
tree.add_node(tree, 6)
tree.add_node(tree, 7)
tree.add_node(tree, 8)

print(tree.post_order(tree))
