"""Измените программу из задачи 098.
Предложите пользователю выбрать строку и выведите только ее. Предложите вы-
брать столбец из выведенной строки и выведите только хранящееся там значение.
Спросите, хочет ли пользователь изменить его. Если ответ будет положительным,
предложите ввести новое значение и измените данные. Наконец, снова выведите
измененную строку."""

numbers = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
print(numbers)

user_row = int(input("Please choose row: "))
row = numbers[user_row]
print(row)

user_column = int(input("Please select a column: "))
column = row[user_column]
print(column)

change_num = input(f"You want to change the value {column}? (y/n): ")
if change_num == "y":
    new_value = int(input("Enter value: "))
    numbers [user_row] [user_column] = new_value
    print("Value changed ")
else:
    print("Value not changed ")

print(row)
print(numbers)