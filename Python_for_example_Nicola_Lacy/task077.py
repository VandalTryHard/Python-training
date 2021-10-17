"""Измените программу 076, чтобы после ввода списка имен программа выводила полный список.
Предложите пользователю ввести одно из имен в списке и выведите позицию имени в списке. Спро-
сите, хочет ли пользователь, чтобы этот человек присутствовал на вечеринке. Если пользователь от-
ветит «no», удалите элемент из списка и снова выведите список."""

guests = []
guest1 = guests.append(input("Enter guest 1: "))
guest2 = guests.append(input("Enter guest 2: "))
guest3 = guests.append(input("Enter guest 3: "))
more = input("Invite more (y/n): ")
if more == "y":
    while more == "y":
        guest_more = guests.append(input("More: "))
        more = input("More (y/n): ")
invite_guests = len(guests)
print(f"Number of guests: {invite_guests}")
print(guests)
#077
analysis = input("Name: ")
if analysis in guests:
    print(guests.index(analysis))
delete_guest = input(f"Do you want '{analysis.title()}'to be present? (y/n): ")
if delete_guest == "n":
    guests.remove(analysis)
print(guests)

