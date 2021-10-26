"""Используя базу данных PhoneBook из программы
139, напишите программу, которая выводит следующее меню:
Main Menu
1) View phone book
2) Add to phone book
3) Search for surname
4) Delete person from
phone book
5) Quit
Enter your selection:
Если пользователь выбирает пункт 1, он сможет просмотреть всю телефонную
книгу. Если он выбирает пункт 2, он сможет доба-
вить новую запись в телефонную книгу. Если выбран пункт 3, программа пред-
лагает ввести фамилию, а затем выводит записи
всех людей с заданной фамилией. При выборе пункта
4 программа предлагает ввести идентификатор
и удаляет соответствующую запись из таблицы.
При выборе пункта 5 программа завершается.
Наконец, при вводе недопустимого числа должно
выводиться соответствующее сообщение об ошибке.
После каждого действия пользователь должен воз-
вращаться к меню, пока не будет выбран пункт 5."""

import sqlite3

with sqlite3.connect("PhoneBook_task139.db") as db:
    cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Names(
id integer PRIMARY KEY,
firstname text,
surname text,
phone text,
number text); """)

cursor.execute("""INSERT INTO names(id, firstname, surname, phone, number)
VALUES("1", "Simon", "Howeis", "01223", "349752")""")
db.commit()

cursor.execute("""INSERT INTO names(id, firstname, surname, phone, number)
VALUES("2", "Karen", "Phillips", "01954", "295773")""")
db.commit()

cursor.execute("""INSERT INTO names(id, firstname, surname, phone, number)
VALUES("3", "Darren", "Smith", "01583", "749012")""")
db.commit()

cursor.execute("""INSERT INTO names(id, firstname, surname, phone, number)
VALUES("4", "Anne", "Jones", "01323", "567322")""")
db.commit()

cursor.execute("""INSERT INTO names(id, firstname, surname, phone, number)
VALUES("5", "Mark", "Smith", "01224", "855534")""")
db.commit()