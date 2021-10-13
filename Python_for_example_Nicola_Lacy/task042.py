total = 0

for i in range(0, 5):
    user = int(input("Please enter a number: "))
    choice = input("Do you want to continue (y/n)? ")
    if choice == "y":
        total = total + user
print(total)

