"""Напишите программу, которая помогает пользователю легко управлять списком имен. Программа
должна выводить меню, дающее возможность добавлять, изменять и удалять имена из списка,
а также отображать их все. Кроме того, в меню должна присутствовать команда для завершения
работы программы. Если пользователь выбрал несуществующую команду, программа выводит соот-
ветствующее сообщение. После того как пользователь выбрал команду добавления, изменения или
удаления имени или просмотра всех имен, меню должно выводиться снова без необходимости пере-
запуска программы. Программа должна быть по возможности простой и удобной в использовании."""

def adding_name():
    name = input("Please enter a name to add: ")
    list.append(name)
    
def change_name():

def delete_name():

def view_name():


def main():
    print("1) Adding a name")
    print("2) Name change")
    print("3) Deleting a name")
    print("4) View names")
    print("Exit (e)")
    list_name = []
    user_choice = input("Enter: ")
    if user_choice == "1":
        adding_name()
    elif user_choice == "2":
        change_name()
    elif user_choice == "3":
        delete_name()
    elif user_choice == "4":
        view_name()
    else:
        print("Goodbye")

main()
