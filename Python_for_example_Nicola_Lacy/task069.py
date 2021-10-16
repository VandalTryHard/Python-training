"""Создайте кортеж с названиями пяти стран. Выведите все содержимое кортежа. Предложите
пользователю ввести название одной из этих стран и выведите индекс (то есть позицию в списке)
этого элемента кортежа."""

countries = ("USA", "Japan", "Germany", "Czech", "Kanada", "Sweden ", "France")
print(countries)
choice = input(f"Choose your country : ")
print(countries.index(choice))
