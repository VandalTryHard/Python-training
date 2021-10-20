"""Создайте новый файл с именем Names.txt. Добавьте в него пять имен,
отображающихся на разных строках. После запуска программы найдите
папку, в которой располагается ваша программа; убедитесь в том, что файл
был создан."""

file = open("Names_task106.txt", "w")
file.write("Valentin\n")
file.write("Nikitos\n")
file.write("Kirill\n")
file.write("Jenya\n")
file.write("Anryouha\n")
file.close()