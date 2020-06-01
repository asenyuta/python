# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

script_name, T_hours, P_hour, Premium = argv

print("Имя скрипта: ", script_name)
print("Выработка (часов): ", T_hours)
print("Ставка (за час): ", P_hour)
print("Премия: ", Premium)
print(f"Зарплата сотрудника составляет: ", float(T_hours) * float(P_hour) + float(Premium))
