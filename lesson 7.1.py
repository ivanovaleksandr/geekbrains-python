"""Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31  22         3   5   32        3  5  8  3
37  43         2   4   6         8  3  7  1
51  86        -1   64  -8

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
(двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и т.д."""

import numpy


class Matrix:
    def __init__(self, a):
        self.b = '\n'.join(['\t'.join([str(x) for x in y]) for y in a])
        list = []
        for y in a:
            list.append([x for x in y])
        self.a = list

    def __str__(self):
        self.c = str(self.a)
        return self.c

    def __add__(self, other):
        result = []
        numbers = []
        for y in range(len(self.a)):
            for x in range(len(self.a[0])):
                summa = other.a[y][x] + self.a[y][x]
                numbers.append(summa)
                if len(numbers) == len(self.a):
                    result.append(numbers)
                    numbers = []
        return Matrix(result)


m1 = numpy.array([[1, 6, 2], [9, 1, 10], [0, 8, 1]])
m2 = numpy.array([[9, 8, 12], [20, 0, 3], [4, 4, 7]])
print(m1)
print("-" * 50)
print(m2)
print("-" * 50)
s = m1 + m2
print(s)
