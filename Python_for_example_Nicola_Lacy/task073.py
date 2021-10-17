"""Предложите пользователю ввести
названия четырех любимых блюд и сохраните их в словаре с числовыми
индексами, начиная с 1. Выведите содержимое словаря с указанием индексов и элементов.
Спросите пользователя, какой элемент
он хочет исключить, и удалите его из
списка. Отсорти руйте оставшиеся
данные и выведите содержимое словаря."""

favorite_food = {}
favorite_food1 = input("first: ")
favorite_food[1] = favorite_food1
favorite_food2 = input("second: ")
favorite_food[2] = favorite_food2
favorite_food3 = input("third: ")
favorite_food[3] = favorite_food3
favorite_food4 = input("fourth: ")
favorite_food[4] = favorite_food4
print(favorite_food)
food_del = int(input("Which number to delete: "))
del favorite_food[food_del]
print(sorted(favorite_food.values()))