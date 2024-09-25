
class Node:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Solution(object):
    def longest_path(self, root: Node) -> int:
        self.global_max = float('-inf')

        def dfs(node):
            if not node:
                return 0
            # because we need to process the child first so we have do a post order
            left_node = dfs(node.left)
            right_node = dfs(node.right)

            self.global_max = max(self.global_max, left_node + right_node)

            return max(left_node, right_node) + 1

        dfs(root)
        return self.global_max


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


s = Solution()
print(s.longest_path(root))


# to show how does it work

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class PrintSolution:
    def longestPath(self, root: Node) -> int:
        self.max_length = 0

        def dfs(node, depth):
            if not node:
                print("  " * depth +
                      f"Reached null node, returning 0")
                return 0

            print("  " * depth + f"Visiting node with value: {node.val}")
            print("  " * depth + f"Going left from {node.val}")

            left_height = dfs(node.left, depth + 1)
            print("  " * depth + f"Going right from {node.val}")
            right_height = dfs(node.right, depth + 1)

            path_through_node = left_height + right_height
            self.max_length = max(self.max_length, path_through_node)

            print("  " * depth + f"At node {node.val}:")
            print("  " * depth +
                  f"  Left height: {left_height}, Right height: {right_height}")
            print("  " * depth + f"  Path through node: {path_through_node}")
            print("  " * depth + f"  Current max_length: {self.max_length}")

            subtree_height = max(left_height, right_height)
            print(
                "  " * depth + f"Returning subtree height for node {node.val}: {subtree_height}")
            return subtree_height + 1

        dfs(root, 0)
        print(f"Final result: {self.max_length}")
        return self.max_length


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

solution = PrintSolution()
solution.longestPath(root)
