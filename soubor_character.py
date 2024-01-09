import sys

class Character:
    def __init__(self, name:str, attack:int, defence:int, hp:int):
        self._name = name
        self.attack = attack
        self._defence = defence
        self._hp = hp 


    @property
    def name(self) -> str:
        return self._name
    
    @property
    def defence(self) -> int:
        return self._defence
    
    @property
    def hp(self) -> int:
        return self._hp
    
    def __str__(self) -> str:
        return f"{self._name} [{self.attack}/{self._defence}, {self._hp}]"
    

def load(filename: str) -> list[Character]:
    characters = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            # Разбиваем строку по символу "/"
            parts = line.strip().split('/')

            # Извлекаем значения из частей и создаем объект Character
            name = parts[0]
            attack = int(parts[1])
            defence = int(parts[2])
            hp = int(parts[3])

            characters.append(Character(name, attack, defence, hp))
    return characters


def save(characters:list[Character], filename:str):
    with open(filename, 'w') as file:
        for character in characters:
            file.write(str(character) + '\n')

input_file = sys.argv[1]
output_file = sys.argv[2]

character_list = load(input_file) # загрзили книжки в лист из input_file

save(character_list, output_file) # загрузим book_list в output_file