"""Определите подпрограмму,которая предлагает пользователю выбрать большое
и маленькое число, а затем генерирует случайное число
из этого диапазона и сохраняет его в переменной с именем comp_num. 

Определите другую подпрограмму, которая выводит
сообщение «I am thinking of a number…», после чего предлагает пользователю угадать загаданное число.

Определите третью подпрограмму, которая проверяет,
совпадает ли comp_num с предположением пользователя. 
Если совпадает, то подпрограмма выводит сообщение «Correct, you win»; в противном случае цикл
продолжается, а подпрограмма сообщает, больше или
меньше их предположение загаданного числа, и предла-
гает сделать новую попытку до тех пор, пока пользователь его не угадает."""

import random

def bot_random():
    num1 = int(input("Small number: "))
    num2 = int(input("Big number : "))
    comp_num = random.randint(num1, num2)
    return comp_num
    
def ask_num():
    print("I am thinking of a number…")
    user_ansver = int(input("What number am I thinking?: "))
    return user_ansver

def bot_response(comp_num, user_ansver):
    start = True
    while start == True:
        if comp_num == user_ansver:
            print("Correct, you win!!!")
            start = False
        elif comp_num > comp_num:
            user_ansver = int(input("Too low: "))
        else:
            user_ansver = int(input("Too high: "))

def main():
    comp_num = bot_random()
    user_ansver = ask_num()
    bot_response(comp_num, user_ansver)

main()


