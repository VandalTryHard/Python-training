"""Используя программу из задачи 100, запросите у пользователя имя и регион. Выведите соответ-
ствующие данные. Запросите у пользователя имя и регион того значения, которое он хочет изме-
нить, и позвольте скорректировать объем продаж. Выведите объемы продаж по всем регионам для
имени, выбранного пользователем."""

sales  = {"John": {"N":3056, "S":8463, "E":8441, "W":2694},
 "Tom": {"N":4832, "S":6786, "E":4737, "W":3612},
 "Anna": {"N":5239, "S":4802, "E":5820, "W":1859},
 "Fiona": {"N":3904, "S":3645, "E":8821, "W":2451}
}
name_user = input("Name: ")
region_user = input("Region: ")

choice = sales [name_user] [region_user]
print(choice)

change = input("Do you want change (y/n)? ")
if change == "y":
    new_value = int(input("New value: "))
    sales [name_user] [region_user] = new_value
    print("Value changed!")
else:
    print("Value not changed!")

print(sales[name_user])

