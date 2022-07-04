from hashlib import new


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
            
new_binary_tree = Binary_tree_python_list(8)
print(new_binary_tree.insertNode("Drink"))
print(new_binary_tree.insertNode("Hot"))
print(new_binary_tree.insertNode("Cold"))
