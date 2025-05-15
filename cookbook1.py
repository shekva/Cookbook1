import os

def read_recipes_from_file(filename):
    cook_book = {}
    with open(filename, 'r', encoding='utf-8') as file:
        while True:
            dish_name = file.readline().strip()
            if not dish_name:
                break
            ingredient_count = int(file.readline().strip())
            ingredients = []
            for _ in range(ingredient_count):
                ingredient_line = file.readline().strip()
                ingredient_info = [part.strip() for part in ingredient_line.split('|')]
                ingredient = {
                    'ingredient_name': ingredient_info[0],
                    'quantity': int(ingredient_info[1]),
                    'measure': ingredient_info[2]
                }
                ingredients.append(ingredient)
            cook_book[dish_name] = ingredients
            file.readline()  # Пропускаем пустую строку
    return cook_book

def create_sample_recipes_file(filename):
    if not os.path.exists(filename):
        with open(filename, 'w', encoding='utf-8') as file:
            file.write("""Омлет
3
Яйцо | 2 | шт
Молоко | 100 | мл
Помидор | 2 | шт

Утка по-пекински
4
Утка | 1 | шт
Вода | 2 | л
Мед | 3 | ст.л
Соевый соус | 60 | мл

Запеченный картофель
3
Картофель | 1 | кг
Чеснок | 3 | зубч
Сыр гауда | 100 | г
""")

if __name__ == '__main__':
    filename = 'recipes.txt'
    create_sample_recipes_file(filename)  # Создаст файл, если его нет
    cook_book = read_recipes_from_file(filename)
    print(cook_book)