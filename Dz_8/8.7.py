"""
7. Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения
и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры
класса (комплексные числа) и выполнив сложение и умножение созданных
экземпляров. Проверьте корректность полученного результата.
"""

class C:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '{0}+{1}i'.format(self.x, self.y)

    def __add__(self, other):
        print(self, 'add', other)
        self.x += other.x
        self.y += other.y
        return f'{self.x}+{self.y}i'

    def __mul__(self, other):
        print(self, 'mul', other)
        self.x = self.x * other.x - self.y * other.y
        self.y = self.y * other.x + self.x * other.y
        return f'{self.x}+{self.y}i'

if __name__ == '__main__':
    a = C(5, 3)
    b = C(2, 1)
    print(a, b, sep='\n')
    print('-' * 15)
    print(a + b)
    print('-' * 15)
    print(a * b)
