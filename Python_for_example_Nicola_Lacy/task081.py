"""Предложите пользователю ввести его любимый школьный предмет.
Выведите его так, чтобы после каждой буквы следовал дефис —
например, S-p-a-n-i-s-h-."""

item = input("Favorite school item: ")
for letter  in item:
    print(letter , end = "-")