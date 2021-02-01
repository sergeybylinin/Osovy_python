"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления
на нуль. Проверьте его работу на данных, вводимых пользователем. При вводе
пользователем нуля в качестве делителя программа должна корректно обработать
эту ситуацию и не завершиться с ошибкой.
"""

class ZeroError(ZeroDivisionError):
    def __init__(self, text):
        self.text = text

def func(x, y):
    try:
        if y == 0:
            raise ZeroError('Деление на 0')
        
    except ZeroDivisionError:
        return 'Ошибка! На ноль делить нельзя!'

    else:
        return x/y
        

print(func(1, 0))
print(func(4, 2))
