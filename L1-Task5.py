revenue = float(input("Введите размер выручки: "))
expense = float(input("Введите размер издержек: "))

if revenue - expense >= 0:
    print(f"Фирма работает с прибылью {revenue - expense}")
    print(f"Рентабельность выручки составляет {(revenue - expense) / revenue}")
    headcount = int(input("Введите количество сотрудников:"))
    print(f"Прибыль фирмы на одного сотрудника {(revenue - expense) / headcount}")
else:
    print(f"Фирма работает с убытком {expense - revenue}")
