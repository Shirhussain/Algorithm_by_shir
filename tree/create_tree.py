class TreeNode:
    def __init__(self, data, children = None):
        if children is None:
            children = []
        self.data = data
        self.children = children
        
    def __str__(self, level=0) -> str:
        result = " "*level + str(self.data) + "\n"
        for child in self.children:
            result += child.__str__(level + 1)
        return result
    
    def addChild(self, TreeNode):
        self.children.append(TreeNode)
        

tree = TreeNode('Drink', [])
cold = TreeNode('cold', [])
hot = TreeNode('hot', [])

tree.addChild(cold)
tree.addChild(hot)

tea = TreeNode('tea', [])
coffee = TreeNode('coffee', []) 
cola = TreeNode('cola', [])
fonta = TreeNode('fonta', [])

cold.addChild(cola)
cold.addChild(fonta)
hot.addChild(tea)
hot.addChild(coffee)

print(tree)
