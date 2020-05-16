a = float(input("Введите целое положительное число: "))
while a <= 0 or a % 1 != 0:
    a = float(input("Введите целое положительное число: "))

max = a % 10
while a > 10:
    a = a // 10
    if a % 10 > max:
        max = a % 10

print(f"Самая большая цифра в чиле: {int(max)}")
