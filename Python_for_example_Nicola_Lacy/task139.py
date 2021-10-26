"""Создайте базу данных SQL с именем PhoneBook. База данных долж-
на содержать таблицу Names со следующими данными:
ID First Name Surname Phone Number
1 Simon Howeis 01223 349752
2 Karen Phillips 01954 295773
3 Darren Smith 01583 749012
4 Anne Jones 01323 567322
5 Mark Smith 01224 855534"""

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