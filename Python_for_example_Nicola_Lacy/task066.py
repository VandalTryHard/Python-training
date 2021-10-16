"""Нарисуйте восьмиугольник, все стороны которого окрашены в разные
цвета (случайно выбираемые из списка шести возможных цветов)."""
import turtle
import random
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for i in range(0, 8):
    turtle.color(random.choice(colors))
    turtle.left(45)
    turtle.forward(100)
turtle.exitonclick()