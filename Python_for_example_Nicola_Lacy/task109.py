"""Выведите следующее меню:
1) Create a new file
2) Display the file
3) Add a new item to the file
Make a selection 1, 2 or 3: 
Предложите пользователю выбрать один из вариантов.
Если пользователь введет что-либо, кроме 1, 2 и 3, программа должна вывести соответствующее сообщение об ошибке.
Если пользователь выберет 1, предложите ему ввести название школьного предмета и сохраните его в новом файле
с именем Subject.txt. Существующий файл с таким именем должен быть заменен новым файлом.
Если пользователь выберет 2, выводится содержимое файла Subject.txt.
Если пользователь выберет 3, предложите пользователю ввести новый предмет, сохраните его в файле, а затем выведите все его содержимое.
Запустите программу несколько раз, чтобы протестировать разные команды."""


print("Menu:\n 1)Create a new file\n 2)Display the file\n 3)Add a new item to file\n")
choice = int(input("Make a selection 1, 2 or 3: "))
start = True
if choice != 1 and choice != 2 and choice != 3:
    print("Error")
elif choice == 1:
    file = open("Subject_task109.txt", "w")
    subject = input("Subject: ")
    file.write(f"{subject} \n")
    file.close()
elif choice == 2:
    file = open("Subject_task109.txt", "r")
    file.close()
elif choice == 3:
    file = open("Subject_task109.txt", "a")
    subject_new = input("New subject: ")
    file.write(f"{subject_new} \n")
    file.close()

file = open("Subject_task109.txt", "r")
print(file.read())
file.close()


