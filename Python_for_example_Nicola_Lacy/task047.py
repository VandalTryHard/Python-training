num1 = float(input("Num1: "))
more = "y"
total = num1
while more == "y":
    num2 = float(input("Num2: "))
    total = num1 + num2
    num1 = total
    more = input("Again? (y/n): ")
    if more == "n":
        print(f"Total = {total}")