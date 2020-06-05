# Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные
# о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки,
# также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

import json

firm_dict = {}
i = 0
total_positive_income = 0
with open("Task-7.txt", "r") as file:
    for line in file:
        s = line.split()
        income = int(s[2]) - int(s[3])
        if income > 0:
            i += 1
            total_positive_income += income
        firm_res = {s[0]: income}
        firm_dict.update(firm_res)
    average = {"average_profit": round(total_positive_income / i)}
    final_list = [firm_dict, average]
    print(final_list)

with open("Task-7JSON.json", "w") as file_json:
    json.dump(final_list, file_json)
