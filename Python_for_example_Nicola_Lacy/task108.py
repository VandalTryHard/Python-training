"""Откройте файл Names.txt. Предложите пользователю вве-
сти новое имя. Добавьте его в конец файла и выведите все
содержимое файла."""

file = open("Names_task106.txt", "r")
print(file.read())

file = open("Names_task106.txt", "a")
user = input("Please enter name: ")
file.write(f"{user} \n")

file = open("Names_task106.txt", "r")
print(file.read())
