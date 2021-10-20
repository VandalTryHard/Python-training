"""Используя двумерный список из задачи 096, пред-
ложите пользователю выбрать строку и столбец и вы-
ведите выбранное значение."""

numbers = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]

num_user1 = int(input("Enter row: "))
num_user2 = int(input("Enter column: "))

print(numbers [num_user1] [num_user2])