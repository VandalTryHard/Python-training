"""Напишите математическую игру, в которой пользователь
должен ответить на пять вопросов. Каждый вопрос строит-
ся из двух случайно сгенерированных целых чисел (напри-
мер, [num1] + [num2]). Предложите пользователю ввести
ответ. Если пользователь ввел правильный ответ, добавьте
одно очко в его пользу. В конце игры сообщите пользовате-
лю количество правильных ответов."""
import random
again = 0
correct = 0
while again < 5:
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    result = num1 + num2
    answer = int(input(f"{num1} + {num2} =  "))
    again = again + 1
    out_of = 5
    if answer == result:
        print("Yep")
        correct = correct + 1
        print(f"{correct} out of {out_of}")
    elif answer != result:
        print("Nop")
        print(f"{correct} out of {again}")
print(f"Total {correct} out of {again}")
