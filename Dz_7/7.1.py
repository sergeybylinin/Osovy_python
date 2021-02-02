"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку
конструктора класса (метод __init__()), который должен принимать
данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин,
расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода
матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции
сложения двух объектов класса Matrix (двух матриц). Результатом сложения
должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент
первой строки первой матрицы складываем с первым элементом первой строки
второй матрицы и т.д.
"""

class Matrix:
    def __init__(self, a, b, c, d, e, f, g, h, i):
        self.matrix = [[a, b, c,], [d, e, f], [g, h, i]]
        print("Создана новая матрица")

    def __str__(self):
        res = ''
        for el in self.matrix:
            res += str(el) + '\n'
        return res[:-1]

    def __add__(self, other):
        print('add')
        result = []
        numbers = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                summa = other.matrix[i][j] + self.matrix[i][j]
                numbers.append(summa)
                if len(numbers) == len(self.matrix):
                    result.append(numbers)
                    numbers = []
        return result

    def __radd__(self, other):
        return self.__add__(other)

a = Matrix(*range(1, 10))
b = Matrix(*range(10, 100, 10))
print(a)
print()
print(b)
c = a + b
print(c)
