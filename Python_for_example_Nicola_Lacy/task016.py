weather = input("Is it raining on your street? ")
answer = str.lower(weather)
if answer == "yes":
    weather2 = input("Is it windy outside? ")
    answer2 = str.lower(weather2)
    if answer2 == "yes":
        print("It is too windy for an umbrella")
    else:
        print("Take an umbrella")
else:
    print("Enjoy your day <3")
