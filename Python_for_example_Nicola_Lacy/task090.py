"""Предложите пользователю вводить целые числа. Если поль-
зователь вводит число от 10 до 20, сохраните его в массиве;
в противном случае выведите сообщение «Outside the range».
После того как пять чисел будут успешно добавлены в массив,
выведите сообщение «Thank you» и выведите массив, каждый
элемент которого находился бы на отдельной строке."""

from array import *

array_new = array('i', [])
how_much = 0
while how_much <= 4:
    new_number = int(input(f"Number: "))
    if new_number > 10 and new_number < 20:
        array_new.append(new_number)
        how_much = how_much + 1
    else:
        print(f"{new_number} Outside the range. ")
print("Thank you")
for i in array_new:
    print(i)