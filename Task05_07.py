"Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать "
"данные о фирме: название, форма собственности, выручка, издержки."
"Пример строки файла: firm_1 ООО 10000 5000."
"Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. "
"Если фирма получила убытки, в расчет средней прибыли ее не включать."
"Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. "
"Если фирма получила убытки, также добавить ее в словарь (со значением убытков)."
"Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}]."
"Итоговый список сохранить в виде json-объекта в соответствующий файл."
"Пример json-объекта:"
"[{""firm_1"": 5000, ""firm_2"": 3000, ""firm_3"": 1000}, {""average_profit"": 2000}]"
"Подсказка: использовать менеджер контекста."

import json

data_firms = []

with open("Task05_07_Data") as f_obj:
    content = f_obj.readlines()
    firms_list = {}
    profit_list = []

    for line in content:
        name, type_of_ownership, revenue, costs = line.split()
        profit = float(revenue) - float(costs)
        firms_list[name] = profit
        if profit > 0:
            profit_list.append(profit)
    print(firms_list)
    print(profit_list)

    data_firms.append(firms_list)
    data_firms.append({"average_profit": sum(profit_list)/len(profit_list)})
    print(data_firms)

with open("Task05_07.json", "w") as f_obj_js:
    json.dump(data_firms, f_obj_js)