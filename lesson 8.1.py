"""1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
«день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число,
месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию
числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных."""


class Data:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def class_method(cls, day, month, year):
        print(f"Текущая дата: {str(day)} - {str(month)} - {str(year)}")

    @staticmethod
    def static_method(day, month, year):
        if 0 < day > 31:
            print("День введен не верно, введите число от 1 до 31.")
        if 0 < month > 12:
            print("Месяц введен не верно, введите число от 1 до 12.")
        if 0 < year > 2020:
            print("Год введен не верно, введите число от 1 до 2020.")
        print(f"Текущая дата: {str(day)} - {str(month)} - {str(year)}")


cl = Data
cl.class_method(11, 12, 2020)
cl.static_method(10, 11, 2019)
cl.static_method(45, 11, 2019)
cl.static_method(12, 15, 2019)
cl.static_method(12, 11, 2021)
cl.static_method(45, 15, 2022)
