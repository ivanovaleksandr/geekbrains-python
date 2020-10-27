"""4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько
дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите
метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат."""


class Car:
    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        return f"- Машина поехала."

    def stop(self):
        return f"- Машина остановилась."

    def turn_right(self):
        return f"- Машина повернула направо."

    def turn_left(self):
        return f"- Машина повернула налево."

    def show_speed(self):
        return f"- Текущая скорость: {self.speed}"


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f"- Скорость превышена: {self.speed}."
        else:
            return f"- Скорость машины: {self.speed}"


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f"- Скорость превышена: {self.speed}."
        else:
            return f"- Скорость машины: {self.speed}"


class SportCar(Car):
    def sport_car(self):
        return f"{self.name}\nСкорость машины: {self.speed()}."


class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)


town_car = TownCar("Smart", "Черный", 60)
print(f"Название машины: {town_car.name}, цвет машины: {town_car.color}")
print(f"{town_car.go()}\n{town_car.turn_left()}\n{town_car.show_speed()}\n{town_car.turn_right()}\n{town_car.stop()}")
print("*" * 70)

work_car = WorkCar("ЗИЛ", "Синий", 40)
print(f"Название машины: {work_car.name}, цвет машины: {work_car.color}")
print(f"{work_car.go()}\n{work_car.turn_left()}\n{work_car.show_speed()}\n{work_car.turn_right()}\n{work_car.stop()}")
print("*" * 70)

sport_car = SportCar("Ferrari", "Красный", 160)
print(f"Название машины: {sport_car.name}, цвет машины: {sport_car.color}")
print(
    f"{sport_car.go()}\n{sport_car.turn_left()}\n{sport_car.show_speed()}\n{sport_car.turn_right()}\n{sport_car.stop()}")
print("*" * 70)

police_car = PoliceCar("Полиция", "Синий", 80)
print(f"Название машины: {police_car.name}, цвет машины: {police_car.color}")
print(
    f"{police_car.go()}\n{police_car.turn_left()}\n{police_car.show_speed()}\n{police_car.turn_right()}\n{police_car.stop()}")
print("*" * 70)
