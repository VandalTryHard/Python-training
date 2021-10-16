import random
num = random.randint(1, 10)
again = "y"
while again == "y":
    choice = int(input("Plese enter number: "))
    if choice == num:
        print("Yep")
        break
    else:
        print("No, try again")
