"""Предложите пользователю ввести имя,
а затем сообщите, сколько в нем гласных букв."""

user_name = input("Enter name: ")
name = user_name.lower()
consonants = 0
for latter in name:
    if latter == "a" or latter == "e" or latter == "i" or latter == "o" or latter == "u" or latter == "y":
        consonants = consonants + 1
    else:
        consonants = consonants
print(f"There are {consonants} consonants in the name {user_name.title()} ")