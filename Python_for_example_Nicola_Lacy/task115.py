"""Используя файл Books.csv, выведите данные
с нумерацией строк."""

import csv

file_= open("Books_task111.csv", "r")

for line in file_:
    print(line)

file_.close()



