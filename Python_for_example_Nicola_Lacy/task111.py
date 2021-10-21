"""Создайте файл .csv с данными, приведенными в следующей таблице. Назовите его Books.csv.
Книга Автор Год выпуска
0 To Kill a Mockingbird Harper Lee 1960
1 A Brief History of Time Stephen Hawking 1988
2 The Great Gatsby F. Scott Fitzgerald 1922
3 The Man Who Mistook His Wife for a Hat Oliver Sacks 1985
4 Pride and Prejudice Jan Austen 1813"""

import csv
file_ = open("Books_task111.csv", "w")
new_book1 = "0, To Kill a Mockingbird, Harper Lee, 1960\n"
file_.write(str(new_book1))
new_book2 = "1, A Brief History of Time, Stephen Hawking, 1988\n"
file_.write(str(new_book2))
new_book3 = "2, The Great Gatsby, F. Scott Fitzgerald, 1922\n"
file_.write(str(new_book3))
new_book4 = "3, The Man Who Mistook His Wife for a Hat, Oliver Sacks, 1985\n"
file_.write(str(new_book4))
new_book4 = "4, Pride and Prejudice, Jan Austen, 1813\n"
file_.write(str(new_book4))
file_.close()

