"""Создайте пустой список с именем nums. Предложите поль-
зователю последовательно вводить числа. После ввода
каждого числа добавьте его в конец списка nums и вы-
ведите список. После того как пользователь введет три числа,
спросите, хочет ли он оставить последнее введенное число
в списке. Если пользователь ответит «no», удалите последний
элемент из списка. Выведите список."""
#nums = []
#num1 = int(input("Plese enter number1: "))
#num2 = int(input("Plese enter number2: "))
#num3 = int(input("Plese enter number3: "))
#nums.append(num1)
#nums.append(num2)
#nums.append(num3)
#print(nums)
#leave = input("Leave the last? (y/no): ")
#if leave == "no":
#    nums.remove(num3)
#print(nums)
nums = []
total = 0
while total < 3:
    total = total + 1
    num = int(input(f"Plese enter number {total}: "))
    nums.append(num)
    print(nums)
leave = input("Leave the last? (y/no): ")
if leave == "no":
    nums.remove(num)
print(nums)