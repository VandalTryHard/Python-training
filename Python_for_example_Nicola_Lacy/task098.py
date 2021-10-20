"""Используя двумерный список из задачи 096, пред-
ложите пользователю выбрать строку и выведите
только ее. Предложите ввести новое значение, до-
бавьте его в конец строки, после чего снова выведите
измененную строку."""

numbers = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
print(numbers)

row_user = int(input("Enter row: "))
row = numbers[row_user]
print(row)

new_num = int(input("Enter a value to add: "))
row.append(new_num)

print(row)
print(numbers)