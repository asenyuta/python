# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

""""Вариант 1"""
def my_func1(x, y, z):
    l = [x, y, z]
    l.sort(reverse=True)  # пробуем обратную сортировку
    print(l[0] + l[1])


""""Вариант 2"""
def my_func2(x, y, z):
    l = [x, y, z]
    l.remove(min(l))
    print(sum(l))


a = int(input("Введите число 1: "))
b = int(input("Введите число 2: "))
c = int(input("Введите число 3: "))

my_func1(a, b, c)
my_func2(a, b, c)
