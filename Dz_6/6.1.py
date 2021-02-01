"""
1. Создать класс TrafficLight (светофор) и определить у него один
атрибут color (цвет) и метод running (запуск). Атрибут реализовать
как приватный. В рамках метода реализовать переключение светофора
в режимы: красный, желтый, зеленый. Продолжительность первого состояния
(красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего
(зеленый) — на ваше усмотрение. Переключение между режимами должно
осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""

from time import sleep

class TrafficLight:          
    def red(self):
        self.__color = 'red'
        print('Горит красный')
        self.countdown(7)
        return self.yellow()
        
    def yellow(self):
        self.__color = 'yellow'
        print('Горит желтый')
        self.countdown(2)
        return self.green()
        
    def green(self):
        self.__color = 'green'
        print('Горит зеленый')
        self.countdown(7)
        return self.red()

    def countdown(self, seconds):
        for i in range(seconds, 0, -1):
            print(i)
            sleep(1)

    def running(self):
        self.red()
    
if __name__ == '__main__':
    print(__doc__)
    Svetofor = TrafficLight()
    Svetofor.running()

