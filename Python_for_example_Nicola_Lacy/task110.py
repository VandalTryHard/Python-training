"""С помощью созданного ранее файла
Names.txt выведите список имен в Python. 
Попросите пользователя ввести
одно из имен, а затем сохраните все,
кроме выбранного в новом файле, под
названием Names2.txt."""

file_ = open("Names_task106.txt", "r")
print(file_.read())
file_.close()

file_ = open("Names_task106.txt", "r")
new_name = input("Name: ")
new_name = new_name + "\n"
for row in file_:
    if row != new_name:
        file_ = open("Names2_task110.txt", "a")
        record = row
        file_.write(record)
        file_.close()
file_.close()




