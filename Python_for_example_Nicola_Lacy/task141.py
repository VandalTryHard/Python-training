"""Создайте базу данных SQL с именем BookInfo, предназначенную
для хранения списка авторов и написанных ими книг. Она состоит из
двух таблиц. Первая таблица с именем Authors содержит следую-
щие данные:
Name PlaceofBirth
Agatha Christie Torquay
Cecelia Ahern Dublin
J. K. Rowling Bristol
Oscar Wilde Dublin
Вторая таблица Books должна содержать следующие данные:
ID Title Author Date_Published
1 De Profundis Oscar Wilde 1905
2 Harry Potter and the chamber of secrets J. K. Rowling 1998
3 Harry Potter and the prisoner of Azkaban J. K. Rowling 1999
4 Lyrebird Cecelia Ahern 2017
5 Murder on the Orient Express Agatha Christie 1934
6 Perfect Cecelia Ahern 2017
7 The marble collector Cecelia Ahern 2016
8 The murder on the links Agatha Christie 1923
9 The picture of Dorian Gray Oscar Wilde 1890
10 The secret adversary Agatha Christie 1921
11 The seven dials mystery Agatha Christie 1929
12 The year I met you Cecelia Ahern 2014"""

import sqlite3

with sqlite3.connect("BookInfo_task141.db") as db: #инициализирует БД или создание БД
        cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Authors(
    name text PRIMARY KEY, 
    place_of_birth text); """)
    
cursor.execute("""CREATE TABLE IF NOT EXISTS Books(
    id integer PRIMARY KEY,
    title text,
    author text,
    date_published text); """)

def main():
    start = True
    while start == True:
        print("1) View phone book")
        print("2) Add authors")
        print("3) Add books")
        print("4) Quit")
        user_response = input("Enter: ")
        if user_response == "1":
            view_table()
        elif user_response == "2":
            try:
                add_authors()
            except sqlite3.IntegrityError:
                print("The given ID is already in use ")
        elif user_response == "3":
            add_books()
        elif  user_response == "4":
            quit()
        else:
            print("Error")

def view_table():
    cursor.execute("SELECT * FROM Authors") #выбирает все данные из БД Names
    for line in cursor.fetchall():
        print(line) #выводит все даные
    cursor.execute("SELECT * FROM Books")
    for line in cursor.fetchall():
        print(line)

def add_authors():
    newName = input("Enter Name: ")
    newplace_birth = input("Enter place of birth: ")
    cursor.execute("""INSERT INTO Authors(name, place_of_birth) 
    VALUES(?, ?)""",(newName, newplace_birth))
    db.commit()

def add_books():
    newID = input("Enter ID: ")
    newTitle = input("Enter title: ")
    newAuthor = input("Enter author: ")
    newData = input("Enter data published: ")
    cursor.execute("""INSERT INTO Books(id, title, author, date_published) 
    VALUES(?, ?, ?, ?)""",(newID, newTitle, newAuthor, newData))
    db.commit()

main()