"""Создайте список с названиями двух видов
спорта. Предложите пользователю ввести
свой любимый вид спорта и добавьте его
в конец списка. Отсортируйте список и вы-
ведите его."""

sports = ["football", "basketball", ]
user_sport = input("Enter your favorite sport: ")
sports.append(user_sport)
print(sorted(sports))