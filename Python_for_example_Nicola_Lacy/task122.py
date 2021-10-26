"""Создайте следующее меню:
1) Add to file
2) View all records
3) Quit program
Enter the number of your selection:
Если пользователь выбрал вариант 1, данные должны добавляться в файл Salaries.csv, содержащий имена и зарплаты.
Если пользователь выбрал вариант 2, программа выводит все записи из файла Salaries.csv. Если пользователь выбрал ва-
риант 3, программа завершается. Если выбран несуществующий вариант, выводится сообщение об ошибке. Пользователь
снова и снова возвращается к меню, пока не будет выбран вариант 3."""

import csv

def main():
    start = True
    while start == True:
        print("1) Add to file")
        print("2) Viev all records")
        print("3) Quit program")
        user_choice = str(input("Enter the number of your selection: "))
        if user_choice == "1":
            add_file()
        elif user_choice == "2":
            view_file()
        elif user_choice == "3":
            start = False
        else:
            print("Error, try again")
    
def add_file():
    file_salaries = open("Salaries_task122_123.csv", "a")
    name_salaries = input("Enter name: ")
    salary_salaries = input("Enter salary: ")
    employee_data = name_salaries + " " + salary_salaries + "\n"
    file_salaries.write(employee_data)
    file_salaries.close()
    return employee_data

def view_file():
    file_salaries = open("Salaries_task122_123.csv", "r")
    print(file_salaries.read())
    file_salaries.close()

main()
