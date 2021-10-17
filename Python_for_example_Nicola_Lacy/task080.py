"""Предложите пользователю
ввести свое имя, а затем выведите длину имени.
Запросите фамилию и выведите длину фамилии.
Соедините имя с фамилией, разделив их пробелом,
и выведите результат. Наконец, выведите длину полного имени (включая пробел)."""

name = input("Name: ")
print(len(name))
surname = input("Surname: ")
print(len(surname))
full_name = surname + " " + name
print(full_name)
print(len(full_name))