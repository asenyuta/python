# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def my_func():
    s = 0
    l = ''
    while l.find('#') == -1:
        k = l.split()
        result = [int(item) for item in k]
        s = s + sum(result)
        l = input("Введите сторку чисел (# для завершения): ")

    last_string = l.partition("#")
    last_list = last_string[0].split()
    result = [int(item) for item in last_list]
    s = s + sum(result)
    print(s)


my_func()
