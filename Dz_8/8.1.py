"""
1. Реализовать класс «Дата», функция-конструктор которого должна
принимать дату в виде строки формата «день-месяц-год». В рамках
класса реализовать два метода. Первый, с декоратором @classmethod,
должен извлекать число, месяц, год и преобразовывать их тип к
типу «Число». Второй, с декоратором @staticmethod, должен проводить
валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""

class Data:
    def __init__(self, data):
        self.data = data
        
    @classmethod
    def first_method(cls, data):
        months = ['January', 'February', 'March',
                  'April', 'May', 'June',
                  'July', 'Augusy', 'September',
                  'October', 'November', 'December']
        day, month, year = data.split('-')
        if month in months:
            month = months.index(month)+1
        else: month = -1
        day, year = list(map(int, (day, year)))
        return [day, month, year]
        
    @staticmethod
    def second_method(data):
        res = True
        day, month, year = Data.first_method(data)
        if  not 1900 < year  <= 2021:
            res = False
        elif month not in range(1, 13):
            res = False
        elif (month in (1,3,5,7,8,10,12) and
              day not in range(1, 32)):
            res = False
        elif (month in (4,6,9,11) and
            day not in range(1, 31)):
            res = False
        elif (month == 2 and
            day not in range(1, 28)):
            res = False
        return data, res
           
if __name__ == "__main__":
    print(Data.first_method('27-January-2021'))
    x = Data('27-January-2021')
    print(x.data)
    print(x.second_method(x.data))
    print(x.second_method('27-Januar-2021'))
