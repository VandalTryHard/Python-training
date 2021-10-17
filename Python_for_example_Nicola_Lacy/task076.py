"""Предложите пользователю ввести имена трех людей, которых он хочет
пригласить на вечеринку, и сохраните их в списке. После того как будут
введены все три числа, спросите, хочет ли пользователь добавить еще
одно имя. Если ответ будет положительным, предложите ему добавлять
имена, пока не получите ответ «no». После ответа «no» выведите количе-
ство людей, приглашенных на вечеринку."""

guests = []
guest1 = guests.append(input("Enter guest 1: "))
guest2 = guests.append(input("Enter guest 2: "))
guest3 = guests.append(input("Enter guest 3: "))
more = input("Invite more (y/n): ")
if more == "y":
    while more == "y":
        guest_more = guests.append(input("More: "))
        more = input("More (y/n): ")
invite_guests = len(guests)
print(f"Number of guests: {invite_guests}")
