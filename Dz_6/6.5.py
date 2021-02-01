"""
5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних
класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод
для каждого экземпляра.
"""

class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')

class Pen(Stationary):
    def draw(self):
        print('Отрисовка ручкой.')

class Pencil(Stationary):
    def draw(self):
        print('Отрисовки карандашом.')

class Handle(Stationary):
    def draw(self):
        print('Отрисовки маркером.')

if __name__ == '__main__':
    
    my_pen = Pen('Parker')    
    my_pencil = Pencil('Brauberg')
    my_handle = Handle('Copic')

    for stationary in (my_pen, my_pencil, my_handle):
        print(stationary.title)
        stationary.draw()
        print('-'*30)
