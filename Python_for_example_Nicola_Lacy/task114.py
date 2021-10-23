"""Используя файл Books.csv, предложите поль-
зователю ввести начальный и конечный год.
Выведите все книги, выпущенные в заданном
промежутке времени."""

# я хуй его знает как это делать! убил 2 часа но не смог решить. Кто сможет напиши мне в лс пж
# I dick him knows how to do it! killed 2 hours but couldn't solve. Who can write to me in ls pzh 
import csv

search_year1 = input("From : ")
search_year2 = input("to: ")

file_= list(csv.reader(open("Books_task111.csv")))
new_list = []
for row in file_:
    new_list.append(row)
    print(new_list)

x = 0
for row in new_list:
    if int(new_list[x][1]) >= search_year1 and int(new_list[x][1]) <= search_year2:
        print(new_list[x])
    x = x + 1


