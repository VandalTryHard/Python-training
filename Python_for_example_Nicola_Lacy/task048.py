total = 0
guest1 = input("Invite a guest? (y/n) ")
while guest1 == 'y':
    guest = input("Guest: ")
    print(f"{guest.title()} has been invited!")
    total = total + 1
    guest1 = input("Invite more? (y/n) ")
    if guest1 == 'n':
        print(f"Number of guests: {total}")
