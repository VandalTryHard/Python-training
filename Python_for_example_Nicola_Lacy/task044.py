user = int(input("How many people will be at the party?: "))

if user > 0 and user <= 10:
    for i in range(0, user):
        people = input("Guest name: ")
        print(f"{people.title()} has been invited.")
else:
    print("Too many people")