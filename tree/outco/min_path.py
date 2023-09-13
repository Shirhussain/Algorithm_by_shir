'''
Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Input: Node in a Binary Tree
Output: Integer
'''
'''
Examples:

Input:
             3

        9        20

               15   7
Output: 2
Explanation: 9 is a leaf and there are two nodes on the path to this leaf, 3 and 9.
15 and 7 are also leaves, but there are three nodes on the paths to these leaves.

Input:

     2
        3
          4
            5
              6
Output: 5
Explanation: The only leaf in this three is 6. There are five nodes on the path to this node,
2, 3, 4, 5, and 6.

'''
'''
Constraints:

Let D be the depth of the shallowest leaf, N the number of nodes in the tree.
Time complexity: O(min(N, 2^D))
Auxilliary space complexity: O(min(N, 2^D))

'''
'''
Diagram
             3

        9        20

               15   7


                  R
      BigFullTree     L

queue: bft_left, bft_right
new_node: L
'''
'''
Pseudocode

find_min_depth(node)
  bfs(node, depth):
    create queue containing (node, depth)
    while queue is not empty
      pop (new_node, new_depth) from queue
      if new_node is not null
        if new_node is a leaf:
          return new_depth of new_node
        push on queue (new_node's left child, new_depth+1)
        push on queue (new_node's right child, new_depth+1)

  return bfs(node, 1)
'''




import random
from collections import deque
class BstNode:

    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None

    def min_depth(self):
        if self.key is None:
            return 0

        q = deque((self,))
        result = 0

        while q:
            result += 1
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    if node.left is None and node.right is None:
                        return result
                    q.append(node.left)
                    q.append(node.right)
        return result

    def min_depth_bfs(self):
        if self.key is None:
            return 0

        q = deque([(self, 1)])

        while q:
            node, path = q.popleft()
            if node:
                if node.left is None and node.right is None:
                    return path
                q.append((node.left, path+1))
                q.append((node.right, path+1))
        return 0

    def insert(self, key):
        if self.key == key:
            return
        elif self.key < key:
            if self.right is None:
                self.right = BstNode(key)
            else:
                self.right.insert(key)
        else:  # self.key > key
            if self.left is None:
                self.left = BstNode(key)
            else:
                self.left.insert(key)

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * \
            '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + \
            (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + \
            [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


nums = [1, 3, 9, 20, 15, 7]
b = BstNode(3)
# for _ in range(50):
#     b.insert(random.randint(0, 100))
for num in nums:
    b.insert(num)
b.display()

print(b.min_depth())
print(b.min_depth_bfs())
