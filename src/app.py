from src.models import *
from src.utils import *

def build_product_tree():
    tree = Tree("tree")
    tree.add("Eletronics")
    tree.add("Eletronics", "Laptop")
    tree.add("Laptop", "128gb")
    
    return tree

def app():
    tree = build_product_tree()
    fm = FileManager('data')
    fm.save(tree.get_json())
    
    tree.remove('128gb')
    tree.show()
    
    tree.set_json(fm.load())
    tree.show()
    
    
    pass
