def find_node_in_tree(target, rootNode):
    if not rootNode:
        return False
    if target == rootNode:
        return True
    else:
        return (find_node_in_tree(target, rootNode.left) or find_node_in_tree(target, rootNode.right))


def find_first_common_ancestor(n1, n2, root):
    n1_on_left = find_node_in_tree(n1, root.left)
    n2_on_left = find_node_in_tree(n2, root.left)

    if n1_on_left ^ n2_on_left:
        return root
    else:
        if n1_on_left:
            return find_first_common_ancestor(n1, n2, root.left)
        else:
            return find_first_common_ancestor(n1, n2, root.right)


class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


node54 = Node(54)
node88 = Node(88, node54)
node35 = Node(35)
node22 = Node(22, node35, node88)
node33 = Node(33)
node90 = Node(90, None, node33)
node95 = Node(95)
node99 = Node(99, node90, node95)
node44 = Node(44, node22, node99)
node77 = Node(77)
root_node = Node(55, node44, node77)

common_ancestor = find_first_common_ancestor(node88, node33, root_node)
print(common_ancestor.value)
