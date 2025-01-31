class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children: TreeNode = []
        
    def add_child(self, child):
        self.children.append(child)
    
    def remove_child(self, data):
        for i, child in enumerate(self.children):
            if child.data == data:
                del self.children[i]
                return  # Após remover, não precisa continuar a busca
            else:
                child.remove_child(data)
    
    def exist(self, data):
        
        if self.data == data:
            return True
        
        found = False
        for child in self.children:
            found = found or child.exist(data)
        
        return found
    
    def find(self, data):
        
        if self.data == data:
            return self
        
        for child in self.children:
            found = child.find(data)
            if found:
                return found
            
        return None
    
    def count(self, i: int = 0):
        for child in self.children:
            i = i + child.count()
        return i + 1
    
    def show_levels(self, levels: int = 0):
        
        print('+' * levels + f'[{self.data}]')
        
        for child in self.children:
            child.show_levels(levels + 1)
    
    def get_json(self, json, parent=None):
            
        json["data"].append({'data': self.data, 'parent': parent})
        
        for child in self.children:
            child.get_json(json, self.data)
            