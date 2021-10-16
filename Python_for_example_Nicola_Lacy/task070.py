"""Доработайте программу 069 так,
чтобы она предлагала пользователю
ввести число и выводила название
страны, находящейся в заданной
позиции."""

countries = ("USA", "Japan", "Germany", "Czech", "Kanada", "Sweden ", "France")
print(countries)
choice = int(input(f"Choose number: "))
print(countries[choice])
