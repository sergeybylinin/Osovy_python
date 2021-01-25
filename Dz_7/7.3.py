"""
3. Реализовать программу работы с органическими клетками. Необходимо создать
класс Клетка. В его конструкторе инициализировать параметр, соответствующий
количеству клеток (целое число). В классе должны быть реализованы методы
перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()),
умножение (__mul__()), деление (__truediv__()). Данные методы должны применяться
только к клеткам и выполнять увеличение, уменьшение, умножение и обычное
(не целочисленное) деление клеток, соответственно. В методе деления должно
осуществляться округление значения до целого числа.

Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно
равняться сумме ячеек исходных двух клеток.

Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность
количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.

Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется
как произведение количества ячеек этих двух клеток.

Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как
целочисленное деление количества ячеек этих двух клеток.

В классе необходимо реализовать метод make_order(), принимающий экземпляр класса
и количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек
между \n равно переданному аргументу. Если ячеек на формирование ряда не хватает,
то в последний ряд записываются все оставшиеся.

Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n*****.
Подсказка: подробный список операторов для перегрузки доступен по ссылке.
"""

class Cell:
    
    def __init__(self, i):
        self.i = i

    def __add__(self, other):
        print('add', self.i, other)
        return self.i + other

    def __radd__(self, other):
        print('radd', self.i, other)
        return self.__add__(other)

    def __sub__(self, other):
        res = other - self.i
        if res > 0:
            print('sub', self.i, other)
            return res
        else:
            print('Отрицательное значение')
            return 0

    def __mul__(self, other):
        print('mul', self.i, other)
        return (self.i*other)
    
    def __rmul__(self, other):
         print('rmul', self.i, other)
         return self.__mul__(other)    

if __name__ == '__main__':
    x = Cell(5)
    y = Cell(7)
    print(x + y)
    print(x - y)
    print(y - x)
    print('-'*10)
    print(x * y)
