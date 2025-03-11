
"""
Binary Tree Swapping Problem

Problem Description:
------------------
A binary tree is characterized by:
- Can be empty (null)
- Contains a root node only
- Contains a root node with left subtree, right subtree, or both

In-order traversal process:
1. Traverse left subtree
2. Visit root
3. Traverse right subtree

Node visit conditions (store value when):
- First node visited
- Leaf node (visited once)
- All subtrees explored (visited once)
- Root node (first visit)

Swapping Operation:
- Swapping subtrees means if node has left subtree L and right subtree R,
  after swap left becomes R and right becomes L

Depth Definition:
- Root node is at depth 1
- If parent depth is d, child depth is d+1

Swap Rules:
- Given integer k, swap subtrees of all nodes at depths h, where h ∈ [k, 2k, 3k,...]
- In other words, swap at depths that are multiples of k

Input Format:
- First line: n (number of nodes)
- Next n lines: two integers (left_child right_child), -1 for null
- Next line: t (number of queries)
- Next t lines: k values for each query

Output Format:
- For each k, perform swap and print in-order traversal

Constraints:
- 1 ≤ n ≤ 1024
- 1 ≤ t ≤ 100
- 1 ≤ k ≤ n
- Either child is -1 or 1 ≤ child ≤ n
- Child index > parent index
"""

#
# Complete the 'swapNodes' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY indexes
#  2. INTEGER_ARRAY queries
#


def swapNodes(indexes, queries, use_level_order=False):
    class Node:
        def __init__(self, val=1, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    def build_tree():
        # Create nodes array with None at index 0 to match 1-based indexing
        nodes = [Node(i) for i in range(n + 1)]

        # Build connections
        for i, (left, right) in enumerate(indexes, 1):
            if left != -1:
                nodes[i].left = nodes[left]
            if right != -1:
                nodes[i].right = nodes[right]

        return nodes[1]  # Return root

    def swap_nodes_dfs(root, k, level=1):
        """Depth-first approach for swapping nodes"""
        if not root:
            return

        # If current level is multiple of k, swap children
        if level % k == 0:
            root.left, root.right = root.right, root.left

        # Recurse on children with increased level
        swap_nodes_dfs(root.left, k, level + 1)
        swap_nodes_dfs(root.right, k, level + 1)

    def swap_nodes_bfs(root, k):
        """Level-order (BFS) approach for swapping nodes"""
        if not root:
            return

        # Use queue for level order traversal
        queue = [(root, 1)]  # (node, level)

        while queue:
            level_size = len(queue)

            # Process entire level
            for _ in range(level_size):
                node, level = queue.pop(0)

                # If current level is multiple of k, swap children
                if level % k == 0:
                    node.left, node.right = node.right, node.left

                # Add children to queue with next level
                if node.left:
                    queue.append((node.left, level + 1))
                if node.right:
                    queue.append((node.right, level + 1))

    def inorder(root, result):
        if not root:
            return

        inorder(root.left, result)
        result.append(root.val)
        inorder(root.right, result)

    # Build initial tree
    root = build_tree()
    result = []

    # Process each query
    for k in queries:
        # Perform swap operation using selected approach
        if use_level_order:
            swap_nodes_bfs(root, k)
        else:
            swap_nodes_dfs(root, k)

        # Get inorder traversal after swap
        current = []
        inorder(root, current)
        result.append(current)

    return result


def run_test_case(test_name, n, indexes, queries):
    print(f"\nTest Case {test_name}:")
    print("Input:")
    print(f"n = {n}")
    print(f"indexes = {indexes}")
    print(f"queries = {queries}")

    print("\nDFS Approach Output:")
    result_dfs = swapNodes(indexes, queries, use_level_order=False)
    for r in result_dfs:
        print(' '.join(map(str, r)))

    print("\nLevel-Order Approach Output:")
    result_bfs = swapNodes(indexes, queries, use_level_order=True)
    for r in result_bfs:
        print(' '.join(map(str, r)))

    # Verify both approaches give same result
    if result_dfs == result_bfs:
        print("\nBoth approaches produced identical results ✓")
    else:
        print("\nWarning: Results differ between approaches!")


if __name__ == '__main__':
    # Test Case 1
    n = 3
    indexes = [[2, 3], [-1, -1], [-1, -1]]
    queries = [1, 1]
    run_test_case(1, n, indexes, queries)

    # Test Case 2
    n = 5
    indexes = [[2, 3], [-1, 4], [-1, 5], [-1, -1], [-1, -1]]
    queries = [2]
    run_test_case(2, n, indexes, queries)

    # Test Case 3
    n = 11
    indexes = [
        [2, 3], [4, -1], [5, -1], [6, -1], [7, 8],
        [-1, 9], [-1, -1], [10, 11], [-1, -1], [-1, -1], [-1, -1]
    ]
    queries = [2, 4]
    run_test_case(3, n, indexes, queries)
