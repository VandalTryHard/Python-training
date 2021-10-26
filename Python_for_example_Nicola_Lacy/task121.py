"""Напишите программу, которая помогает пользователю легко управлять списком имен. Программа
должна выводить меню, дающее возможность добавлять, изменять и удалять имена из списка,
а также отображать их все. Кроме того, в меню должна присутствовать команда для завершения
работы программы. Если пользователь выбрал несуществующую команду, программа выводит соот-
ветствующее сообщение. После того как пользователь выбрал команду добавления, изменения или
удаления имени или просмотра всех имен, меню должно выводиться снова без необходимости пере-
запуска программы. Программа должна быть по возможности простой и удобной в использовании."""

def main():
    start = True
    while start == True:
        print("1) Adding a name")
        print("2) Name change")
        print("3) Deleting a name")
        print("4) View names")
        print("5) For Exit")
        user_choice = int(input("Enter: "))
        if user_choice == 1:
            list_name = adding_name()
        elif user_choice == 2:
            list_name = change_name()
        elif user_choice == 3:
            list_name = delete_name()
        elif user_choice == 4:
            list_name = view_name()
        elif user_choice == 5:
            start = False
        else:
            print("Error")

def adding_name():
    user_adding_name = input("Enter name for adding: ")
    list_name.append(user_adding_name)
    return list_name
    
def change_name():
    user_change_name = input("Enter name for change: ")
    list_name.remove(user_change_name)
    user_new_name = input("Enter new name: ")
    list_name.append(user_new_name)
    return list_name
    
def delete_name():
    user_delete_name = input("Enter name for delete: ")
    list_name.remove(user_delete_name)
    return list_name
    
def view_name():
    for name in list_name:
        print(name)

list_name = []
main()

