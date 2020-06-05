# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

file = open("Task-4.txt", "r")
file_new = open("Task-4_new", "w")
line_new = str

for line in file:
    s = line.split()
    # print(s[2])
    if s[2] == "1":
        line_new = "Один - 1\n"
    elif s[2] == "2":
        line_new = "Два - 2\n"
    elif s[2] == "3":
        line_new = "Три - 3\n"
    elif s[2] == "4":
        line_new = "Четыре - 4\n"
    print(line_new)
    file_new.writelines(line_new)

file.close()
file_new.close()
