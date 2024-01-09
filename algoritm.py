from character import Character

def get_shorter(characters:list[Character], attack:int, defence:int) -> list[Character]:
    new_characters = []

    for character in characters:
        if character.attack <= attack and character.defence <= defence:
            new_characters.append(character)

    return new_characters

characters = [
    Character("medusa", 15, 15, 120),
    Character("tomtom", 40, 10, 120),
    Character("teptep", 25, 30, 120),
    Character("thorfin", 10, 40, 120),
]

lala = get_shorter(characters, 20, 50)

for character in lala:
    print(character)