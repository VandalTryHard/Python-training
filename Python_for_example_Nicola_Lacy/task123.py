"""В языке Python невозможно напрямую удалить запись из
файла .csv. Вместо этого приходится сохранять файл во вре-
менном списке, вносить в него изменения, а затем заменять
исходный файл временным списком.
Измените предыдущую программу, чтобы она предоставля-
ла такую возможность. Меню должно выглядеть так:
1) Add to file
2) View all records
3) Delete a record
4) Quit program
Enter the number of your selection:"""

import csv

def main():
    start = True
    while start == True:
        print("1) Add to file")
        print("2) Viev all records")
        print("3) Delete a record")
        print("4) Quit program")
        user_choice = str(input("Enter the number of your selection: "))
        if user_choice == "1":
            add_file()
        elif user_choice == "2":
            view_file()
        elif user_choice == "3":
            delete_file()
        elif user_choice == "4":
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

def delete_file(): #task123
    file_salaries = open("Salaries_task122_123.csv", "r")
    list_worker = []
    x = 0
    for row in file_salaries:
        list_worker.append(row)
    file_salaries.close()

    for row in list_worker:
        print(x, row)
        x = x + 1
    delete_worker = int(input("Enter the worker number to be deleted: "))
    del list_worker[delete_worker]

    file_salaries = open("Salaries_task122_123.csv", "w")
    for row in list_worker:
        file_salaries.write(row)
    file_salaries.close()

def view_file():
    file_salaries = open("Salaries_task122_123.csv", "r")
    print(file_salaries.read())
    file_salaries.close()

main()
