# A Heap is a special Tree-based data structure in which the tree is a complete binary tree.

from logging import root


class Heap:
    def __init__(self, size):
        self.customeList = (size+1)*[None]
        self.heapSize = 0
        self.maxSize = size+1


def peak_heap(root_node):
    # peak meas the topst one which you cang get or the root one to peak
    # به فارسی به معنی قلعه یعنی آن از همه بالاتر را باید گرفت
    if not root_node:
        return
    else:
        return root_node.customeList[1]


def size_of_heap(root_node):
    if not root_node:
        return
    else:
        return root_node.heapSize


def leve_order_traversal(root_node):
    if not root_node:
        return
    else:
        for i in range(1, root_node.heapSize+1):
            print(root_node.customeList[i])


def heapify_tree_insert(root_node, index, heapType):
    # heap type can be "Min" or "Max"
    parent_index = int(index/2)
    if index <= 1:
        return
    if heapType == "Min":
        if root_node.customeList[index] < root_node.customeList[parent_index]:
            temp = root_node.customeList[index]
            root_node.customeList[index] = root_node.customeList[parent_index]
            root_node.customeList[parent_index] = temp
        heapify_tree_insert(root_node, parent_index, heapType)
    elif heapType == "Max":
        if root_node.customeList[index] > root_node.customeList[parent_index]:
            temp = root_node.customeList[index]
            root_node.customeList[index] = root_node.customeList[parent_index]
            root_node.customeList[parent_index] = temp
        heapify_tree_insert(root_node, parent_index, heapType)


def insert_node(root_node, node_value, heapType):
    if root_node.heapSize + 1 == root_node.maxSize:
        return "The binary heap is full"
    root_node.customeList[root_node.heapSize + 1] = node_value
    root_node.heapSize += 1
    heapify_tree_insert(root_node, root_node.heapSize, heapType)
    return "The value hass been sucessfuly inserted"


def heapify_tree_extract(root_node, index, heapType):
    left_index = index * 2
    right_index = index*2 + 1
    swap_child = 0

    # it means that we don't have any child in current node
    if root_node.heapSize < left_index:
        return
    # if it's has only one child in left index
    elif root_node.heapSize == left_index:
        if heapType == "Min":
            # if its' greater than its left child we should swap it
            if root_node.customeList[index] > root_node.customeList[left_index]:
                temp = root_node.customeList[index]
                root_node.customeList[index] = root_node.customeList[left_index]
                root_node.customeList[left_index] = temp
            return
        else:
            if root_node.customeList[index] < root_node.customeList[left_index]:
                temp = root_node.customeList[index]
                root_node.customeList[index] = root_node.customeList[left_index]
                root_node.customeList[left_index] = temp
    else:
        if heapType == "Min":
            if root_node.customeList[left_index] < root_node.customeList[right_index]:
                swap_child = left_index
            else:
                swap_child = right_index
            if root_node.customeList[index] > root_node.customeList[swap_child]:
                temp = root_node.customeList[index]
                root_node.customeList[index] = root_node.customeList[swap_child]
                root_node.customeList[swap_child] = temp
        else:
            if root_node.customeList[left_index] > root_node.customeList[right_index]:
                swap_child = left_index
            else:
                swap_child = right_index
            if root_node.customeList[index] < root_node.customeList[swap_child]:
                temp = root_node.customeList[index]
                root_node.customeList[index] = root_node.customeList[swap_child]
                root_node.customeList[swap_child] = temp


def extract_node(root_node, heapType):
    # for extracting just consider the place when you go to buy and appel and who you peak from the top.
    # here also you can extract from the root then bring the last leave to the root and push down
    # to swap with child nodes.

    if root_node.heapSize == 0:
        return
    else:
        extracted_Node = root_node.customeList[1]
        root_node.customeList[1] = root_node.customeList[root_node.heapSize]
        root_node.customeList[root_node.heapSize] = None
        root_node.heapSize -= 1
        heapify_tree_extract(root_node, 1, heapType)
        return extracted_Node


def delete_entire_binary_heap(root_node):
    root_node.customeList = None


new_binary_heap = Heap(5)
print(size_of_heap(new_binary_heap))


print("==========================")
insert_node(new_binary_heap, 3, "Max")
insert_node(new_binary_heap, 1, "Max")
insert_node(new_binary_heap, 5, "Max")
insert_node(new_binary_heap, 2, "Max")
insert_node(new_binary_heap, 4, "Max")

leve_order_traversal(new_binary_heap)

print("==========================")
extract_node(new_binary_heap, "Max")
leve_order_traversal(new_binary_heap)


print("==========================")
delete_entire_binary_heap(new_binary_heap)
# leve_order_traversal(new_binary_heap)
