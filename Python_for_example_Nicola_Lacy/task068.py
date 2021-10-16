"""Нарисуйте узор, который меняется при
каждом запуске программы. Используйте
функцию random для выбора количества
линий, длины каждой линии и каждого угла
поворота."""
import turtle
import random

for i in range(0, random.randint(0, 10)):
    turtle.forward(random.randint(0, 100))
    turtle.left(random.randint(0, 360))
    turtle.right(random.randint(0, 360))

turtle.exitonclick()