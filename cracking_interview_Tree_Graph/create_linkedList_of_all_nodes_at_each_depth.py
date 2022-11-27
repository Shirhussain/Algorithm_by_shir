class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

    def add(self, value):
        if self.next is None:
            self.next = LinkedList(value)
        else:
            self.next.add(value)

    def __str__(self) -> str:
        return f"({str(self.value)}){str(self.next)}"


class BinaryTree(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def depth(tree):
    if tree is None:
        return 0
    if tree.left is None and tree.right is None:
        return 1
    depth_left = 1 + depth(tree.left)
    depth_right = 1 + depth(tree.right)
    return depth_left if depth_left > depth_right else depth_right


def tree_to_linked_list(tree, custom_dict=None, d=None):
    if custom_dict is None:
        custom_dict = {}
    if d is None:
        d = depth(tree)
    if custom_dict.get(d) is None:
        custom_dict[d] = LinkedList(tree.value)
    else:
        custom_dict[d].add(tree.value)
        # tis is going to be the base condition the recursive call for
        if d == 1:
            return custom_dict
    # here we are doing pre order traversal for three to create a linked list
    if tree.left != None:
        # if we are going to the next level the depth is decreasing so we put d-1
        custom_dict = tree_to_linked_list(tree.left, custom_dict, d-1)
    if tree.right != None:
        custom_dict = tree_to_linked_list(tree.right, custom_dict, d-1)
    return custom_dict


main_tree = BinaryTree(1)
two = BinaryTree(2)
three = BinaryTree(3)
four = BinaryTree(4)
five = BinaryTree(5)
six = BinaryTree(6)
seven = BinaryTree(7)

main_tree.left = two
main_tree.right = three

two.left = four
two.right = five

three.left = six
three.right = seven

my_tree_list = tree_to_linked_list(main_tree)

for depth_level, linked_list in my_tree_list.items():
    print(f"{depth_level}  {linked_list}")
