"""Нарисуйте цифры, изображенные ниже, начиная
от нижней точки цифры 1. (1, 2, 3)"""
import turtle
#1
turtle.left(90)
turtle.forward(100)
turtle.penup()
turtle.right(90)
turtle.forward(50)
#2
turtle.pendown()
turtle.forward(75)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(75)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(75)
turtle.penup()
turtle.forward(50)
#3
turtle.pendown()
turtle.forward(75)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.right(180)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(75)

turtle.exitonclick()