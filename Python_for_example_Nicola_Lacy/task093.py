"""Предложите пользователю ввести пять чисел. Отсортируйте
их и выведите для пользователя. Предложите вы-
брать одно из чисел. Удалите выбранное число из исходного
массива и сохраните его в новом."""

from array import *

array_user = array("i", [])
for x in range(0, 5):
    user_num = int(input("Number: "))
    array_user.append(user_num)
array_user = sorted(array_user)
print(array_user)

array_num_del = array("i", [])
num_del = int(input("Enter number for deleting: "))
array_num_del.append(num_del)

array_user.remove(num_del)

print(f"Del: {num_del}")
print(f"Array user: {array_user}")
