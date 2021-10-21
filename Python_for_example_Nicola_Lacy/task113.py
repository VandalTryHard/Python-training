"""Используя файл Books.csv, спросите пользователя, сколь-
ко записей он хочет добавить в список, и предоставьте
ему такую возможность. После того как данные будут до-
бавлены, запросите автора и выведите все книги указан-
ного автора из списка. Если в списке нет ни одной книги
этого автора, выведите соответствующее сообщение."""

import csv
file_ = open("Books_task111.csv", "a")

user_number = int(input("How many entries to add: "))
for i in range(user_number):
    number = input("№: ")
    title = input("Title: ")
    author = input("Author: ")
    publishing = input("The year of publishing: ")
    user_line = number + ", " + title + ", " + author + ", " + publishing + "\n"
    file_.write(str(user_line))
file_.close()

file_ = open("Books_task111.csv", "r")
search_author = input("Author: ")
reader = csv.reader(file_)
for line in file_:
    if search_author in str(line):
        print(line)
    elif search_author not in str(line):
        print(f"The author {search_author} is not on the list ")


