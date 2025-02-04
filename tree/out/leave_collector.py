import unittest

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def postorder(node):
    """
    Performs a postorder traversal.

    Returns a tuple (is_leaf, leaves):
      - is_leaf: True if 'node' is a leaf; otherwise, False.
      - leaves: A list of leaf values collected from this subtree.

    As a side effect, if a child is a leaf, its pointer is set to None.
    """
    # If node is a leaf, return immediately.
    if node.left is None and node.right is None:
        return (True, [node.val])

    leaves = []

    # Process the left subtree.
    if node.left is not None:
        is_left_leaf, left_leaves = postorder(node.left)
        leaves.extend(left_leaves)
        # If the left child is a leaf, remove it.
        if is_left_leaf:
            node.left = None

    # Process the right subtree.
    if node.right is not None:
        is_right_leaf, right_leaves = postorder(node.right)
        leaves.extend(right_leaves)
        # If the right child is a leaf, remove it.
        if is_right_leaf:
            node.right = None

    # The current node is not a leaf because it had at least one child.
    return (False, leaves)


def leaf_collector(root):
    """
    Iteratively collects leaves from the tree and removes them until the tree is empty.

    Returns a list of lists where each inner list contains the leaves removed
    in one iteration.
    """
    output = []
    while root is not None:
        is_leaf, collected_leaves = postorder(root)
        output.append(collected_leaves)
        # If the root itself has become a leaf, remove it by setting root to None.
        if is_leaf:
            root = None
    return output


def build_example_tree():
    """
    Builds the following tree:

           1
          / \
         2   3
        / \   \
       4   5   6
      /
     7

    Expected removal order: [[7, 5, 6], [4, 3], [2], [1]]
    """
    node7 = TreeNode(7)
    node4 = TreeNode(4, left=node7)
    node5 = TreeNode(5)
    node2 = TreeNode(2, left=node4, right=node5)
    node6 = TreeNode(6)
    node3 = TreeNode(3, right=node6)
    root = TreeNode(1, left=node2, right=node3)
    return root

# Unit test for our leaf collector based on your approach.


class TestLeafCollector(unittest.TestCase):
    def test_example_tree(self):
        root = build_example_tree()
        expected_output = [[7, 5, 6], [4, 3], [2], [1]]
        result = leaf_collector(root)
        print(result)
        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()
