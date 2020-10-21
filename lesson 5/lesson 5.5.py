"""5. Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран."""

from random import randint

with open("text_5.txt", "w", encoding="utf - 8") as number:
    summa = 0
    for i in range(50):
        num = randint(1, 50)
        summa += num
        number.write((str(num)) + " ")
print(f"Сумма чисел в файле 'text_5.txt': {summa}")