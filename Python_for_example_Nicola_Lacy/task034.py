import math

print(f"1)Square \n2)Triagle")
program = int(input("Enter a number:"))

if program == 1:
    side_length = float(input("side length of a square: "))
    square_area = side_length ** 2
    print(f"Square area: {square_area}")
elif program == 2:
    side_length = float(input("side length of a triangle: "))
    height_triagle = float(input("the height of the triangle: "))
    triangle_area = side_length * height_triagle * 0.5
    print(f"Area of a triangle : {triangle_area}")
else:
    print("Enter correct values!!! ")