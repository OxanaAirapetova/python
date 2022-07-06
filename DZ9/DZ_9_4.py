# Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police(булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

class Car:
    def __init__(self, speed, name, color, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        print(f'Машина {self.name} {self.color}ого цвета поехала'
              f' и набрала скорость {self.speed} миль/час в классе Car')
    def stop(self):
        return f'Машина {self.name} {self.color}ого цвета остановилась на светофоре '
    def turn(self, direction):
        self.direction = direction
        return f'Машина повернула {self.direction}'
    def show_speed(self):
        return f'{self.name} едет со скоростью {self.speed}'

class TownCar(Car):
    def go(self):
        super().go()
        print(f'Машина {self.name} {self.color}ого цвета спокойно поехала '
                f'и набрала скорость {self.speed} миль/час в классе TownCar')
    def accident(self):
        print(f'Машина {self.name} врезалась в столб в классе TownCar')
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f'Скорость превышена!')
        else:
            print(f'Машина движется со скоростью {self.speed} в классе TownCar\n')

class SportCar(Car):
    def go(self):
        super().go()
        print(f'Обновленный {self.name} едет по магистрали со скоростью {self.speed} в классе SportCar!!!!!')

class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            delta_speed = self.speed - 40
            print(f'Скорость рабочей машины превышена на {delta_speed} км в час!')
        else:
            print(f'Машина движется со скоростью {self.speed} в классе WorkCar')

class PoliceCar(Car):
    pass

towncar_1 = TownCar(100, 'Тойота', 'черн', True)
towncar_1.show_speed()
towncar_2 = TownCar(50, 'Lada', 'бел', True)
towncar_2.show_speed()

workcar_1 = WorkCar(45, 'Scania', 'красн', False)
workcar_1.show_speed()
workcar_2 = WorkCar(20, 'Kamaz', 'желт', False)
workcar_2.show_speed()
police = PoliceCar(20, 'Kamaz', 'желт', False)
print(police.show_speed())







#
#
#
#
#
# class WorkCar(Car):
#
#
#
#
# class PoliceCar(Car):
