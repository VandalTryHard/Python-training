"""Используя базу данных PhoneBook из программы
139, напишите программу, которая выводит следующее меню:
Main Menu
1) View phone book
2) Add to phone book
3) Search for surname
4) Delete person from phone book
5) Quit
Enter your selection:
Если пользователь выбирает пункт 1, он сможет просмотреть всю телефонную книгу. 
Если он выбирает пункт 2, он сможет добавить новую запись в телефонную книгу. 
Если выбран пункт 3, программа предлагает ввести фамилию, а затем выводит записи
всех людей с заданной фамилией. 
При выборе пункта 4 программа предлагает ввести идентификатор и удаляет соответствующую запись из таблицы.
При выборе пункта 5 программа завершается.
Наконец, при вводе недопустимого числа должно выводиться соответствующее сообщение об ошибке.
После каждого действия пользователь должен возвращаться к меню, пока не будет выбран пункт 5."""

import sqlite3

with sqlite3.connect("PhoneBook_task139.db") as db: #инициализирует БД
        cursor = db.cursor()

def main():
    start = True
    while start == True:
        print("1) View phone book")
        print("2) Add to phone book")
        print("3) Search for surname")
        print("4) Delete person from phone book")
        print("5) Quit")
        user_response = input("Enter: ")
        if user_response == "1":
            view_book()
        elif user_response == "2":
            try:
                add_phone()
            except sqlite3.IntegrityError:
                print("The given ID is already in use ")
        elif user_response == "3":
            search_surname()
        elif user_response == "4":
            delete_person()
        elif  user_response == "5":
            quit()
        else:
            print("Error")

def view_book():
    cursor.execute("SELECT * FROM Names") #выбирает все данные из БД Names
    for line in cursor.fetchall():
        print(line) #выводит все даные

def add_phone():
    newID = input("Enter ID: ")
    newFirstname = input("Enter firstname: ")
    newSurname = input("Enter surname: ")
    newPhone = input("Enter phone: ")
    newNumber = input("Enter number: ")
    cursor.execute("""INSERT INTO Names(id, firstname, surname, phone, number) 
    VALUES(?, ?, ?, ?, ?)""",(newID, newFirstname, newSurname, newPhone, newNumber))
    db.commit()

def search_surname():
    surname_search = input("Enter surname: ")
    cursor.execute("SELECT * FROM Names WHERE surname = ?", [surname_search]) #помещает surname_search на место ? ЗАПОМНИТЬ!!!!!!!!
    for line in cursor.fetchall():
        print(line)

def delete_person():
    selectid = int(input("Enter ID: "))
    cursor.execute("DELETE FROM Names WHERE id = ?", [selectid])
    db.commit()

main()