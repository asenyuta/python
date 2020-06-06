# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

my_func1 = lambda x, y: x ** y


def my_func2(x, y):
    z = x
    for i in range(-y - 1):
        z = z * x
    z = 1 / z
    return z


x = int(input("Введите x: "))
y = int(input("Введите y: "))

print(my_func1(x, y))
print(my_func2(x, y))
