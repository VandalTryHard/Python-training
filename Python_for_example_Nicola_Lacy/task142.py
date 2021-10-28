"""Используя базу данных BookInfo из программы 141,
выведите список авторов с датами рождения. Пред-
ложите пользователю ввести место рождения, а затем
выведите название, дату издания и имя автора для
всех книг авторов, родившихся в указанном месте."""

import sqlite3

with sqlite3.connect("BookInfo_task141.db") as db:
    cursor = db.cursor()

cursor.execute("SELECT * FROM Authors")
for row in cursor:
    print(row)
cursor.execute("SELECT * FROM Books")


user_choice = input("Enter Place of Birth author: ")

cursor.execute("""SELECT Books.title, Books.author, Books.date_published 
FROM Books,Authors WHERE Authors.name = Books.author AND Authors.place_of_birth = ?""", [user_choice]) #Поиск в Authors через Books
for row in cursor:
    print(row)

db.close()