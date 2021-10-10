num1 = float(input("How much space do we have (more than 100)? "))
num2 = float(input("One cell fits  (less than 10)? "))
num3 = num1 // num2
how_much = f"{num1} places fit {num2} cells, {num3} pieces each "
print(how_much)