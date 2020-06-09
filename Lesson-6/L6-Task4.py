# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def turn(self, direction):
        return self.name + " повернула " + direction

    def show_speed(self):
        return "Текущая скорость " + self.name + " - " + str(self.speed)


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        if self.speed > 60:
            speeding = " ПРЕВЫШЕНИЕ СКОРОСТИ!!!"
        else:
            speeding = ""
        return "Текущая скорость " + self.name + " - " + str(self.speed) + speeding


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        if self.speed > 40:
            speeding = " ПРЕВЫШЕНИЕ СКОРОСТИ!!!"
        else:
            speeding = ""
        return "Текущая скорость " + self.name + " - " + str(self.speed) + speeding


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


town1 = TownCar(80, 'белый', 'Форд')
print(town1.name, town1.color, town1.speed, town1.is_police)

work1 = WorkCar(50, 'желтый', 'Опель')
work2 = WorkCar(40, 'грязный', 'Фольксваген')
print(work1.name, work1.color, work1.speed, work1.is_police)
print(work2.name, work2.color, work2.speed, work2.is_police)

police1 = PoliceCar(100, 'синий', 'Порше')
print(police1.name, police1.color, police1.speed, police1.is_police)

sport1 = SportCar(150, 'черный', 'Ламборгини')
print(sport1.name, sport1.color, sport1.speed, sport1.is_police)
print(sport1.turn('налево'))
print(sport1.show_speed())
print(town1.show_speed())
print(work1.show_speed())
print(work2.show_speed())
