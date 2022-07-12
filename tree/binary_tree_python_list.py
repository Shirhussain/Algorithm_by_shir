from hashlib import new
from operator import index, ne


class Binary_tree_python_list:
    def __init__(self, size):
        self.custome_list = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size
        
    def insertNode(self, node):
        if self.lastUsedIndex + 1 == self.maxSize:
            return "The binary tree is full"
        self.custome_list[self.lastUsedIndex + 1] = node
        self.lastUsedIndex += 1
        return "The value has been successfully inserted"
    
    def search(self, node_value):
        for i in range(len(self.custome_list)):
            if self.custome_list[i] == node_value:
                return "success"
        return "Not found"
    
    def pre_order_traversal(self, index):
        if index > self.lastUsedIndex:
            return 
        print(self.custome_list[index])
        self.pre_order_traversal(index *2)
        self.pre_order_traversal(index *2 + 1) 
        
    def inOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return 
        self.inOrderTraversal(index*2)
        print(self.custome_list[index])
        self.inOrderTraversal(index*2 + 1)
        
    def post_order_traversal(self, index):
        if index > self.lastUsedIndex:
            return 
        self.post_order_traversal(index*2)
        self.post_order_traversal(index*2 + 1)
        print(self.custome_list[index])
        
    
    def level_order_traversal(self, index):
        for i in range(index, self.lastUsedIndex+1):
            print(self.custome_list[i])
            
    
    def deleteNode(self, value):
        if self.lastUsedIndex == 0:
            return "there is not any node to delete"
        for i in range(1, self.lastUsedIndex + 1):
            if self.custome_list[i] == value:
                self.custome_list[i] = self.custome_list[self.lastUsedIndex]
                self.custome_list[self.lastUsedIndex] = None
                self.lastUsedIndex -= 1
                return "The node has been successfully deleted"
            
    def delete_binary_tree(self):
        self.custome_list = None
        return "The binary tree has been successfully deleted"
    
new_binary_tree = Binary_tree_python_list(8)
print(new_binary_tree.insertNode("Drink"))
print(new_binary_tree.insertNode("Hot"))
print(new_binary_tree.insertNode("Cold"))
print(new_binary_tree.insertNode("Tee")) 
print(new_binary_tree.insertNode("Coffee"))

print(new_binary_tree.search("Hot"))


new_binary_tree.pre_order_traversal(1)
print("--------------------------------")

new_binary_tree.inOrderTraversal(1)

print("--------------------------------")
new_binary_tree.post_order_traversal(1)

print("--------------------------------")
new_binary_tree.level_order_traversal(1)

print("--------------------------------")

print(new_binary_tree.deleteNode("Tee"))

new_binary_tree.level_order_traversal(1)

print("--------------------------------")

print(new_binary_tree.delete_binary_tree())
