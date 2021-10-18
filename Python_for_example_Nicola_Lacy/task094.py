"""Выведите массив из пяти чисел. Предложите пользователю
выбрать одно из них. После того как число будет выбрано,
выведите его позицию в массиве. Если пользователь вве-
дет значение, отсутствующее в массиве, предложите ему
выбрать снова, пока не будет выбрано допустимое значение."""

from array import *

array_ = array("i", [54, 23, 56, 73, 2362])
print(array_)
start = True
while start == True:
    user_choice = int(input("Number (228 for exit): "))
    if user_choice in array_:
        array_index = array_.index(user_choice)
        print(array_index)
    elif user_choice == 228:
        start = False
    else:
        print("Choose again ")
