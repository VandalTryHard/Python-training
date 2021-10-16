import random
coin = ["орёл", "решка"]
side = random.choice(coin)
choice = input("Орёл или решка: ")
choice = choice.lower()
if choice == side:
    print("You win")
else:
    print("Bad luck")
print(f"Загаданное значение: {side}")