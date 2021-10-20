"""Измените программу
102, чтобы она выво-
дила имя и возраст для
всех людей в списке, но
не их размер обуви"""

humans = {}

for i in range(4):
    human = input("Name: ")
    human = human.title()
    age = input("Age: ")
    foot_size = input("Foot size: ")
    humans[human] = {"Age": age, "Foot size:": foot_size, }

for human in humans:
    print((human), humans[human] ["Age"] + " years old")

