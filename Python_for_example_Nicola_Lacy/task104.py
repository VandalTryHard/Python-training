"""После получения имени, возраста и размера обуви для четырех человек
запросите у пользователя имя человека для удаления из списка. Удалите
эту строку и выведите остальные данные с разбивкой по строкам."""

humans = {}

for i in range(4):
    human = input("Name: ")
    human = human.title()
    age = input("Age: ")
    foot_size = input("Foot size: ")
    humans[human] = {"Age": age, "Foot size": foot_size, }

for human in humans:
    print((human), humans[human] ["Age"] + " years old")

delete = input("Whom to remove?: ")
delete = delete.title()
del humans[delete]

for human in humans:
    print((human), humans[human]["Age"],  humans[human]["Foot size"] + "foot size")