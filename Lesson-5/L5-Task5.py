# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

file = open("Task-5.txt", "w")
num = input("Введите число (enter для завершения) ")
s = 0
while num != "":
    file.write(num + " ")
    s += int(num)
    num = input("Введите число (enter для завершения) ")

print(f"Сумма равна {s}")
file.close()
