"""Нарисуйте в один ряд
три квадрата, разделенных промежутками.
Заполните их тремя разными цветами"""
import turtle
import random
turt = 0
color_line = ["black", "yellow", "purple", "green"]
color = ["yellow", "black", "green", "purple"]
while turt < 3:
    turtle.color(random.choice(color_line), random.choice(color))
    turtle.begin_fill()
    for i in range(0, 4):
        turtle.forward(50)
        turtle.left(90)
    turtle.penup()
    turtle.end_fill()
    turtle.forward(100)
    turtle.pendown()
    turt = turt + 1
turtle.exitonclick()