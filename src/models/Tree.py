from .TreeNode import TreeNode

class Tree:
    def __init__(self, name: str):
        self.root = None
        self.name: str = name
    
    # Árvore Existe
    def is_none(self):
        return self.root != None
    
    # Nome da árvore
    def name(self, name: str):
        self.name = name
    
    # Adicionar nó
    def add(self, data: str, newnode: str = None):
        if not self.is_none():
            self.root = TreeNode(data)
        elif newnode == None:
            print("Nó vazio!")
        else:
            node = self.root.find(data)
            if node:
                node.add_child(TreeNode(newnode))
            else:
                print("Nó não encontrado!")
    
    # Remover nó
    def remove(self, data: str):
        if not self.is_none(): return
        
        if self.root.data == data:
            self.root = None
        else:
            self.root.remove_child(data)
    
    # Contar nós
    def count(self):
        if not self.is_none(): return 0
        
        return self.root.count()
    
    # Verifica se nó existe
    def exist(self):
        if not self.is_none(): return False
        
        return self.root.exist()
    
    def get_json(self):
        json = {
            "data": [
                
            ]
        }
        self.root.get_json(json)
        return json
    
    #ALERT ERROR
    def set_json(self,json):
        if len(json["data"]) > 0:
            self.root = TreeNode(json["data"].pop(0)['data'])
            for child in json['data']:
                if child['data'] != None:
                    self.root.find(child['parent']).add_child(TreeNode(child['data']))
        else:
            print("Dados de JSON vazios!")
            
    
    # Mostrar árvore
    def show(self):
        if not self.is_none(): return
        
        print("SHOW")
        self.root.show_tree()