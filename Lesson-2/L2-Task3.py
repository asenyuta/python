# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

vremena_list = ['зима', 'весна', 'лето', 'осень']
vremena_dict = {1: 'зима', 2: 'весна', 3: 'лето', 4: 'осень'}
m = int(input('Введите номер месяца :'))
while m < 1 or m > 12:
    print('Ошибка. Число должно быть от 1 до 12')
    m = int(input('Введите номер месяца :'))

print(f'Ваше время года - {vremena_list[((m % 12) // 3)]}')
print(f'Ваше время года - {vremena_dict.get(((m % 12) // 3) + 1)}')