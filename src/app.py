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
    tree.show()
    json = tree.get_json()
    fm = FileManager('data')
    fm.save(json)
    json = None
    json = fm.load()
    print(json["data"])
    
    pass
