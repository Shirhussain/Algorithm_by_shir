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
        
            
new_binary_tree = Binary_tree_python_list(8)
print(new_binary_tree.insertNode("Drink"))
print(new_binary_tree.insertNode("Hot"))
print(new_binary_tree.insertNode("Cold"))
print(new_binary_tree.search("Hot"))
print(new_binary_tree.insertNode("Coffee"))


new_binary_tree.pre_order_traversal(1)