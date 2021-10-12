import math

radius = float(input("Please enter the radius of the circle: "))
height = float(input("Please enter height: "))
area_circle = math.pi * radius ** 2
volume = area_circle * height
print(round(volume, 2))