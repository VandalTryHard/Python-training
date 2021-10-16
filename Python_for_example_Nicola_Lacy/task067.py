"""Нарисуйте следующий узор:"""
import turtle

for i in range(0, 10):
    turtle.left(36)
    for i in range(0, 8):
        turtle.left(45)
        turtle.forward(50)
turtle.exitonclick()