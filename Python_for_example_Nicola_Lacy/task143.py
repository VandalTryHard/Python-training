"""Используя базу данных BookInfo из
программы 141, предложите пользова-
телю ввести год. Выведите все книги, из-
данные после этого года; список должен
быть упорядочен по году издания."""

import sqlite3

with sqlite3.connect("BookInfo_task141.db") as db:
    cursor = db.cursor()

cursor.execute("""SELECT date_published FROM Books AS INTEGER""")
cursor.execute("""SELECT * FROM Books ORDER BY date_published DESC""")

start = True
while start == True:
    user_choice = input("Enter date published: ")
    cursor.execute("""SELECT * FROM Books WHERE date_published > ? ORDER BY date_published""", [user_choice])
    for row in cursor:
        print(row)

db.close()