"""Создайте массив для хранения целых чисел. Сгенери-
руйте пять случайных чисел и сохраните их в массиве.
Выведите массив (каждый элемент должен выводить-
ся в отдельной строке)."""

from array import *
import random

array_new = array('i', [])
for x in range(0, 5):
    numbers = random.randint(1, 999)
    array_new.append(numbers)
for i in array_new:
    print(i)
