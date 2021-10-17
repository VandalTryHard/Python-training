"""Введите список из десяти цветов.
Предложите пользователю ввести
начальное число в диапазоне от
0 до 4 и конечное число в диа-
пазоне от 5 до 9. Выведите список
цветов из интервала, заданного
начальным и конечным числом."""

colors = ["green", "blue", "pink", "brown", "purple", "black", "white", "red", "yellow", "orange", ]
print(colors)
num1 = int(input("Enter (0-4): "))
num2 = int(input("Enter (5-9): "))
print(colors[num1:num2])