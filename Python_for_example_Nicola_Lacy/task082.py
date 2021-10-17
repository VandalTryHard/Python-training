"""Выведите строку из своего любимого стихотворения и предложите
пользователю ввести начальную и конечную позицию. Выведите
символы, находящиеся между ними."""

poem = f"Свои ошибки признаёт \nЛишь наделённый мудростью, \nА кто судьбу во всём клянёт, \nТот проштампован глупостью."
print(poem)
print(len(poem))
user_start = int(input("Plese enter start position: "))
user_finish = int(input("Plese enter finish position: "))
print(poem[user_start:user_finish])