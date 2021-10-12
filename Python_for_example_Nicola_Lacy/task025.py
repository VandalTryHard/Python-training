name = input("What is your name? ")
name1 = len(name)
if name1 < 5:
    surname = input("What is your surname? ")
    full_name = name + surname
    print(full_name.upper())
else:
    print(name.lower())