import json

class FileManager:
    def __init__(self, name: str):
        self.name = name
        
    def save(self, data):
        with open(f'{self.name}.json', 'w') as arquivo:
            json.dump(data, arquivo, indent=4)
    
    def load(self):
        with open(f'{self.name}.json', 'r') as arquivo:
            return json.load(arquivo)