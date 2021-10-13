user = input("In which direction should the report be conducted? (forward / reverse): ")
user = user.lower()
if user == "forward":
    number = int(input("Number: "))
    for i in range(1, number + 1):
        print(i)
elif user == "reverse":
    number = int(input("Number: "))
    for i in range(number, 0, -1):
        print(i)
else:
    print("I don't understand")

