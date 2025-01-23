from src.models import *
from src.utils import *

def app():
    
    tree = Tree("tree")
    fm = FileManager('data')
    tree.set_json(fm.load())
    
    choise = ""
    
    while choise != "0":
        print(
              "\n__Dynamic_Tree__\n"
              "0. Sair\n"
              "1. Inserir nó\n"
              "2. Deletar nó\n"
              "3. Total de nós\n"
              "4. Exist tree\n"
              "5. Is_none tree\n"
              "6. Show json")
        choise = input("-> ")
        
        if choise == "0":
            print("Saindo...")
        elif choise == "1":
            tree.add(str(input("Pai nó: ")), str(input("Inserir nó: ")))
        elif choise == "2":
            tree.remove(input("Deletar nó: "))
        elif choise == "3":
            print(f"Total de nós: {tree.count()}")
        elif choise == "4":
            print("Valor procurado: ", end='')
            print(f"Exist tree: {tree.exist(str(input()))}")
        elif choise == "5":
            print(f"Is_none tree: {tree.is_none()}")
        elif choise == "6":
            print(f"Show json: {tree.get_json()}")
        else:
            print("Valor inválido... Tente novamente!")
        
        if choise != "0":
            tree.show_levels()
    
    fm.save(tree.get_json())
    
    pass
