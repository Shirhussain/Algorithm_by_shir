class Node:
    def __init__(self, value=None):
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
            elif self.left is None:
                self.left = Node(new_node)
            else:
                self.left.insert(new_node)
        else:
            self.value = new_node

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.value)
        if self.right:
            self.right.print_tree()

    def in_order(self, root):
        result = []
        if root is None:
            return result
        result.extend(self.in_order(root.left))
        result.append(root.value)
        result.extend(self.in_order(root.right))
        return result

    def printPostorder(self, root):
        result = []
        if root:
            result.extend(self.printPostorder(root.left))
            result.extend(self.printPostorder(root.right))
            result.append(root.value)
        return result


tree = Node()
tree.insert(4)
tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)
tree.insert(6)
tree.insert(7)
tree.insert(8)

tree.print_tree()
print(tree.in_order(tree))
print(tree.printPostorder(tree))


# leetcode

class Solution:
    def inorderTraversal(self, root):
        answer = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            answer.append(node.val)
            inorder(node.right)
        inorder(root)
        return answer
