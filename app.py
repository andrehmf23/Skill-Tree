class TreeNode:
    def __init__(self, data):
        self.parent = None
        self.data = data
        self.children: TreeNode = []
        
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    
    def find_child(self, data):
        if self.data == data:
            return self
        for child in self.children:
            child.find_child(data)
        return None
    
    def remove_child(self, data):
        del self.find_child(data)
    
    def count(self):
        i = 0
        for child in self.children:
            i = i + child.count()
        return i + 1
    
    def show_tree(self, levels: int = 0):
        
        print('+' * levels + f'[{self.data}]')
        
        for child in self.children:
            child.show_tree(levels + 1)
    
def build_product_tree():
    root = TreeNode("Eletronics")
    laptop = TreeNode('Laptop')
    memory_aux = TreeNode('128gb')
    
    laptop.add_child(memory_aux)
    root.add_child(laptop)
    return root


if __name__ == '__main__':
    root = build_product_tree()
    root.show_tree()
    print(root.count())
    pass