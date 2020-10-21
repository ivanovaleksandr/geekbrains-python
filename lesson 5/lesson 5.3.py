"""3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников."""

with open("text_3.txt", encoding="utf - 8") as salary:
    summa = []
    less = []
    my_list = salary.readlines()
for i in my_list:
    i = i.split()
    if float(i[1]) <= 20000.0:
        less.append(i[0])
        summa.append(i[1])
print(f"Оклад меньше 20.000: {less:}.\nСредний оклад: {sum(map(float, summa)) / len(summa)}.")