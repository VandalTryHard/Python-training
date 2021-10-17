"""Предложите пользователю ввести его почтовый индекс.
Выведите первые две буквы слова в верхнем регистре."""
#SW1A 0AA – Палата Общин
#SW1A 1AA – Букингемский Дворец
#SW1A 2AA – 10 Даунинг Стрит

postcode = input("Enter your post code: ")
postcode = postcode[0:2]
print(postcode.upper())