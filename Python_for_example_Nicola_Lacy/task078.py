"""Создайте список с названиями четырех телевизионных
передач и выведите их на отдельных строках. Предложите
пользователю ввести название еще одной передачи и позицию,
на которой она должна быть вставлена в список. Снова вы-
ведите список, в котором все пять передач находятся на но-
вых позициях."""

tv_show = ["silicon valley", "mr. robot", "breaking bad", "simpsons", ]
for i in tv_show:
    print(i.title())

tv_show_user = input("Plese enter your favorite show: ")
tv_show_user_position = int(input("What position is she in: "))
tv_show.insert(tv_show_user_position, tv_show_user)
for i in tv_show:
    print(i.title())