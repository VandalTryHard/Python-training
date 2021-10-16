"""Создайте список с названиями шести школьных предметов. Спросите у пользова-
теля, какие из этих предметов ему не нравятся. Удалите выбранные предметы из
списка и выведите его повторно."""

subjects = ["computer science", "physics", "maths", "literature", "languages", "PE", ]
print(f"Which of these items do you dislike {subjects}?")
answer = input("Answer: ")
answer = answer.lower()
subjects.remove(answer)
print(subjects)