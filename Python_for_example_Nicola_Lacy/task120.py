"""Отобразите для пользователя следующее меню:
1) Addition
2) Subtraction
Enter 1 or 2:
Если пользователь выбирает 1, запускается подпрограмма, генерирующая два случайных числа из диапазона между 5 и 20.
Предложите пользователю сложить их. Рассчитайте правильный ответ и выведите его для пользователя вместе с его ответом.
Если он выбирает 2, должна запускаться подпрограмма, генерирующая случайное число между 25 и 50, а затем еще одно
между 1 и 25. Попросите пользователя вычесть второе из первого: так ему не придется беспокоиться об отрицательных
значениях. Выведите правильный ответ вместе с ответом пользователя.
Создайте еще одну подпрограмму, которая будет проверять совпадение ответа пользователя с правильным ответом. Если от-
веты совпали, выведите сообщение «Correct»; в противном случае выведите «Incorrect, the answer is» и правильный ответ.
Если пользователь ввел некорректное значение в самом первом меню, выведите соответствующее сообщение."""

import random

def random_num1():
    num1 = random.randint(5, 20)
    num2 = random.randint(5, 20)
    user_num = int(input(f"{num1}+{num2}= "))
    bot_num = num1 + num2
    print(f"You answer is {user_num}, the correct answer is {bot_num}.")
    answer = user_num, bot_num
    return answer

def random_num2():
    num1 = random.randint(25, 50)
    num2 = random.randint(1, 25)
    user_num = int(input(f"{num1}-{num2}= "))
    bot_num = num1 - num2
    print(f"You answer is {user_num}, the correct answer is {bot_num}.")
    answer = user_num, bot_num
    return answer

def examination(user_num, bot_num):
    if user_num == bot_num:
        print("Correct")
    else:
        print(f"Incorrect, the answer is {bot_num}")

def main():
    print("1) Addition")
    print("2) Subtraction")
    userchoice = input("Enter 1 or 2: ")
    if userchoice == "1":
        user_num, bot_num = random_num1()
        examination(user_num, bot_num)
    elif userchoice == "2":
        user_num, bot_num = random_num2()
        examination(user_num, bot_num)
    else:
        print("Error")
    
main()
