"""Создайте два массива: один будет содержать три
числа, введенных пользователем, а другой — пять
случайных чисел. Объедините эти два массива
в один большой. Отсортируйте и выведите его, при
этом каждое число должно выводиться в отдельной
строке."""

from array import *
import random

array_user = array("i", [])
array_random = array("i", [])
for i in range(0, 3):
    user_num = int(input("Enter number: "))
    array_user.append(user_num)
for i in range(0, 5):
    random_num = random.randint(0, 999)
    array_random.append(random_num)
super_array = array_user + array_random
super_array = sorted(super_array)
print(super_array)


