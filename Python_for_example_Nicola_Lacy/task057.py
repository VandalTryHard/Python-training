import random
num = random.randint(1, 10)
again = "y"
while again == "y":
    choice = int(input("Plese enter number: "))
    if choice == num:
        print("Yep")
        break
    elif choice < num:
        print(f"{choice} < num")
        print("Try again")
    elif choice > num:
        print(f"{choice}>num")
        print("Try again")
