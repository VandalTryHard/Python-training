"""Используя файл Books.csv из программы 111, предложите пользо-
вателю ввести новую запись и добавьте ее в конец файла. Выведите
каждую строку файла .csv в отдельной строке."""

import csv
file_ = open("Books_task111.csv", "a")

user_line = input("Enter: ")
user_line = user_line + "\n"
file_.write(str(user_line))
file_.close()

file_ = open("Books_task111.csv", "r")
for line in file_:
    print(line)
