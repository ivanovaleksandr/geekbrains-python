"""4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию. Элементы вывести в порядке их следования в исходном
списке. Для выполнения задания обязательно использовать генератор.

Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].

Результат: [23, 1, 3, 10, 4, 11]"""

from random import randint


my_list = [randint(-10, 42) for _ in range(10)]
a = [el for el in my_list if my_list.count(el) == 1]
print(f"Список\n{my_list}")
print(f"Нет повторений\n{a}")