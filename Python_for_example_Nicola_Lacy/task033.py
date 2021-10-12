import math

number1 = int(input("Please enter an integer value 1: "))
number2 = int(input("Please enter an integer value 2: "))
integer = number1 // number2
residual = number1 % number2
print(f"Если разделить {number1} на {number2}, получим {integer} с остатком {residual}")