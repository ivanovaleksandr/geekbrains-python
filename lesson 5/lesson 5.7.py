"""7. Создать (не программно) текстовый файл, в котором каждая строка
должна содержать данные о фирме: название, форма собственности, выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.

Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.

Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста."""

import json

result = []
with open("text_7.1.json", "w", encoding="utf - 8") as text_7_1:
    with open("text_7.txt", "r", encoding="utf - 8") as text_7:
        profit = {}
        for i in text_7:
            profit[i.split(" ")[0]] = int(i.split(" ")[2]) - int(i.split(" ")[3])
        average = sum([int(a) for a in profit.values() if int(a) > 0]) / len\
            ([int(a) for a in profit.values() if int(a) > 0])
        result.append(profit)
        result.append({"average": round(average)})
    json.dump(result, text_7_1, ensure_ascii=False, indent=4)
