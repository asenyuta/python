# 2. Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

my_list = []
n = int(input('Введите количество элементов списка: '))
for i in range(n):
    a = input(f'Введите элемент {i+1}: ')
    my_list.append(a)

print(f'Изначальный список: {my_list}')

# for i in range(len(my_list)):
i = 0
while i <= len(my_list) - 2:
    tmp = my_list[i]
    my_list[i]=my_list[i+1]
    my_list[i+1]=tmp
    i = i + 2
print(f'Измененный список: {my_list}')
