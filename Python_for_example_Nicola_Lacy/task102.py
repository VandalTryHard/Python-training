"""Предложите пользователю ввести имя, возраст и размер обуви для че-
тырех человек. Запросите имя одного из них в списке и выведите зна-
чения его возраста и размера обуви."""

humans = {}

for i in range(4):
    human = input("Name: ")
    human = human.title()
    age = input("Age: ")
    foot_size = input("Foot size: ")
    humans[human] = {"Age": age, "Foot size:": foot_size, }
print(humans)

choice_human = input("Enter name: ")
print(humans[choice_human])
