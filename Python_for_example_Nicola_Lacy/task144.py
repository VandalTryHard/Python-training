"""Используя базу данных BookInfo из программы 141, предложите пользователю ввести имя автора.
Сохраните все книги этого автора в текстовом файле; поля должны разделяться дефисами, так что
выводимая информация должна выглядеть примерно так:
5 - Murder on the Orient Express - Agatha Christie - 1934
8 - The murder on the links - Agatha Christie - 1923
10 - The secret adversary - Agatha Christie - 1921
11 - The seven dials mystery - Agatha Christie - 1929
Откройте текстовый файл и убедитесь в том, что программа работает правильно."""

import sqlite3
import csv

with sqlite3.connect("BookInfo_task141.db") as db: #читает БД
    cursor = db.cursor()

user_author = input("Enter author: ")

cursor.execute("""SELECT * FROM Books WHERE author = ? """, [user_author]) #Все совбадения

file_ = open("List_Books_task144.csv", "w")

for row in cursor.fetchall(): # преобразует turple в str и записывает в .csv файл
    row = str(row)
    new_str = row + "\n"
    file_.write(new_str)

file_.close()
db.close()
