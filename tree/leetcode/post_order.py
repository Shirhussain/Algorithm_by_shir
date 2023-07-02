class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


def insert(root, new_node):
    node = Node(new_node)
    if root.value is None:
        root.value = new_node
    if new_node > root.value:
        if root.right is None:
            root.right = node
        else:
            insert(root.right, new_node)
    else:
        if root.left is None:
            root.left = node
        else:
            insert(root.left, new_node)


def post_order(root):
    result = []

    def helper(node):
        if node is None:
            return
        helper(node.left)
        helper(node.right)
        result.append(node.value)

    helper(root)
    return result


tree = Node()

insert(tree, 10)
insert(tree, 4)
insert(tree, 1)
insert(tree, 2)
insert(tree, 3)
insert(tree, 4)
insert(tree, 5)
insert(tree, 6)
insert(tree, 7)
insert(tree, 8)

print(post_order(tree))
