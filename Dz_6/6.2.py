"""
2. Реализовать класс Road (дорога), в котором определить атрибуты:
length (длина), width (ширина). Значения данных атрибутов должны
передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего
дорожного полотна. Использовать формулу: длина * ширина * масса асфальта
для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * число см
толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500т
"""

class Road():
    def __init__(self, lenght: 'длина в м', width: 'ширина в м'):
        self._linght = lenght
        self._width = width

    def asphalt_mass_calculation(self, m: 'масса асфальта для 1кв м дороги',
                                 s: 'толщина acфальта'):
        self.m = m
        self.s = s

        return self._linght * self._width * self.m * self.s / 1000

if __name__ == '__main__':
    print(__doc__)
    P777 = Road(5000, 20)
    massa = P777.asphalt_mass_calculation(25, 5)
    print('%0d' % massa, 'т', sep='')


    