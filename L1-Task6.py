a = float(input("Количество км в 1-й день: "))
b = float(input("Хотим пробежать км: "))

day = 1
while a < b:
    a = a * 1.1
    day = day + 1

print(f"Дистанция покрыта за {day} дней")
