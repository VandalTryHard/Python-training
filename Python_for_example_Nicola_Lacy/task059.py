"""Выведите названия пяти цветов, случайным образом выберите один и пред-
ложите сделать то же пользователю. Если пользователь выберет тот же
цвет, который выбрала программа, выведите сообщение «Well done»; в про-
тивном случае выведите ответ, в котором скрывается намек на правильный
цвет. Предложите пользователю повторить попытку; если пользователь и на
этот раз не угадает, снова выведите ту же подсказку и предложите выбрать
цвет (и так далее, пока пользователь не выдаст правильный ответ)."""
import random
play = True
print(f"What color did I choose?")
while play == True:
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    color = random.choice(colors)
    user = input("Color: ")
    user = user.lower()
    if user == color:
        print("Well done")
        play = False
    elif user != color and color == "red":
        print("The first color in the rainbow ")
    elif user != color and color == "orange":
        print("The second color in the rainbow ")
    elif user != color and color == "yellow":
        print("The third color in the rainbow ")
    elif user != color and color == "green":
        print("The fourth color in the rainbow ")
    elif user != color and color == "blue":
        print("The fifth, sixth color in the rainbow ")
    elif user != color and color == "purple":
        print("The seventh  color in the rainbow ")
    else:
        print(f"Sorry I don't understand: {user}")