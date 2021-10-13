compnum = 50
attempt = 0
user = input("Start? (y/n) ")
while user == "y":
    try_number = int(input("Number: "))
    attempt = attempt + 1
    if try_number > compnum:
        print("Smaller")
    elif try_number < compnum:
        print("More")
    elif try_number == compnum:
        print(f"Well done you took {attempt} attempts")
        break
    else:
        print(f"I don't understand")