"""2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property."""

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, data):
        self.data = data

    @property
    @abstractmethod
    def expenditure(self):
        pass

    def __add__(self, other):
        return self.expenditure + other.expenditure


class Coat(Clothes):
    @property
    def expenditure(self):
        print(f"Расход ткани на пошив пальто: {round(self.data / 6.5) + 0.5}м².")
        return round(self.data / 6.5) + 0.5


class Costume(Clothes):
    @property
    def expenditure(self):
        print(f"Расход ткани на пошив костюма: {(2 * self.data + 0.3) / 100}м².")
        return (2 * self.data + 0.3) / 100


coat = Coat(12)
costume = Costume(150)
print(f"Общее расход ткани на пошив пальто и костюма: {coat + costume}м².")

