from character import Character

def sort_characters_by_attack(characters, count):
    # Выбираем count персонажей с наибольшей атакой
    selected_characters = []
    for i in range(count):
        max_attack = 0
        max_character = None
        for character in characters:
            if character.attack > max_attack and character not in selected_characters:
                max_attack = character.attack
                max_character = character
        if max_character is not None:
            selected_characters.append(max_character)

    # Сортируем выбранных персонажей по возрастанию
    for i in range(count - 1):
        for j in range(0, count - i - 1):
            if selected_characters[j].attack > selected_characters[j + 1].attack:
                selected_characters[j], selected_characters[j + 1] = selected_characters[j + 1], selected_characters[j]

    return selected_characters

# Пример использования
characters = [
    Character("medusa", 15, 15, 120),
    Character("tomtom", 40, 10, 120),
    Character("teptep", 25, 30, 120),
    Character("thorfin", 10, 40, 120),
]

count = 2
sorted_characters = sort_characters_by_attack(characters, count)

# Вывод отсортированных персонажей
for character in sorted_characters:
    print(character)
