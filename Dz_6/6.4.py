"""
4. Реализуйте базовый класс Car. У данного класса должны
быть следующиеатрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда). Опишите несколько
дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать
текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите
метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""
class Car:
    def __init__(self, speed, color, name, is_police):
        self.max_speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.status = 'Машина остановалась'

    def go(self):
        self.status = 'Машина в пути'
        return self.status

    def stop(self):
        self.status = 'Машина остановалась'
        return self.status

    def turn(self, direction):
        self.direction = direction
        self.status = f'Машина повернула {self.direction}'
        return self.status

    def showSpeed(self, show_speed):
        self.show_speed = show_speed
        if self.status != 'Машина остановалась':
            print(f'Текущая скорость {self.show_speed}')
        else: print(0)

class TounCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name, False)

    def showSpeed(self, show_speed, max_show_speed=60):
        self.show_speed = show_speed
        self.max_show_speed = max_show_speed
        if self.status != 'Машина остановалась':
            print(f'Текущая скорость {self.show_speed}')
            if show_speed > max_show_speed:
                print('Скорость превышена!')
        else: print(0)
        

class WorkCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name, False)

    def showSpeed(self, show_speed):
        TounCar.showSpeed(self, show_speed, max_show_speed=40)
        

class Police(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name, True)


if __name__ == '__main__':
    print(__doc__)
    
    Lada = TounCar(200, 'blue', 'kalina')
    print(Lada.max_speed)
    print(Lada.color)
    print(Lada.status)
    Lada.go()
    print(Lada.status)
    Lada.turn('налево')
    print(Lada.status)
    Lada.showSpeed(50)
    Lada.showSpeed(70)
    Lada.stop()
    print(Lada.status)
    Lada.showSpeed(70)
    
    print('-'*30)
    
    Gaz = WorkCar(180, 'yellow', 'gazel')
    print(Gaz.name)
    print(Gaz.is_police)
    Gaz.go()
    print(Gaz.status)
    Gaz.showSpeed(50)
    Gaz.showSpeed(30)
    
    print('-'*30)

    Zaz = Police(100, 'blue-wight', 'запорожец')
    print(Zaz.max_speed)
    print(Zaz.color)
    print(Zaz.is_police )
