number = float(input("Number: "))
while number <= 10 or number >= 20:
    if number <= 10:
        print("Too low")
    elif number >= 20:
        print("Too high")
    else: 
        print("I dont understend")
    number = float(input("Try again: "))
print("Thank you")