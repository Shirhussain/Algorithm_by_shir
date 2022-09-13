# A Heap is a special Tree-based data structure in which the tree is a complete binary tree.

class Heap:
    def __init__(self, size):
        self.customeList = (size+1)*[None]
        self.heapSize=0
        self.maxSize = size+1

def peak_heap(root_node):
    #peak meas the topst one which you cang get or the root one to peak
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
            


new_binary_heap = Heap(5)
print(size_of_heap(new_binary_heap))