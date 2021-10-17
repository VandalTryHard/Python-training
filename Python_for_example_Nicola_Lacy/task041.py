name = input("What is you name: ")
number = int(input("Number: "))
if number < 10:
    for i in range(number):
        print(name)
else:
    print("Too high")