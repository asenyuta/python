# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов
# (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32


from statistics import mean

file = open("Task-3.txt", "r")
salaries = []
for line in file:
    name, salary = line.split()
    salary = float(salary)
    if salary < 20000:
        print(name)
    salaries.append(salary)
print(f"Средний доход - {mean(salaries)}")

file.close()
