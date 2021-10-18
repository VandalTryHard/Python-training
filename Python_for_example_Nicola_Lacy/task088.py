"""Предложите пользователю ввести пять
целых чисел и сохраните их в массиве.
Отсортируйте список и выведите его со-
держимое в обратном порядке."""

from array import *
array_new = array('i', [])
how_much = int(input("How mach: "))
for x in range(0, how_much):
    value_new = int(input("Value: "))
    array_new.append(value_new)
array_new = sorted(array_new)
array_new.reverse()
print(array_new)


