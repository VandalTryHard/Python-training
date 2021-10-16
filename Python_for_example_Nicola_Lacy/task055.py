import random
num = random.randint(1, 5)
again = "y"
while again == "y":
    choice = int(input("Please enter number: "))
    if choice == num:
        print("Well done")
    elif choice <= num:
        print("More")
    elif choice >= num:
        print("Smaller")
    again = input("Again (y/n): ")
print("Correct")