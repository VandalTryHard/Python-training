"""Создайте список из четырех трехзначных чисел. Выведите 
содержимое списка, при этом каждый
элемент должен выводиться на
отдельной строке. Предложите
пользователю ввести число из трех
цифр. Если введенное число совпадает 
с одним из чисел в списке,
выведите позицию этого числа;
в противном случае выведите сообщение 
«That is not in the list»."""

numbers = [456, 228, 366, 356]
for i in numbers:
    print(i)
num_user = int(input("Please enter three-digit number: "))
if num_user in numbers:
    print(f"The value {num_user} is in the list and has index {numbers.index(num_user)} ")
else:
    print("That is not in the list.")