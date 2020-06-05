# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

file = open("Task-1.txt", "w")
str = input("Enter str: ")
while str != "":
    file.writelines(str + '\n')
    str = input("Enter str: ")
file.close()
