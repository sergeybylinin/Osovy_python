"""
3. Реализовать базовый класс Worker (работник), в котором определить
атрибуты: name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker. В классе Position
реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income). Проверить работу примера
на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).
"""

class Worder:
    def __init__(self, name, surname, position, wage, bonus):
        self.fist_name = name
        self.last_name = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worder):
    def get_full_name(self):
        return f'{self.fist_name} {self.last_name}'

    def get_total_income(self):
        return f"{sum(self._income.values())}"

if __name__ == '__main__':
    print(__doc__)
    woker123 = Position('Ivan', 'Petrov', 'dev', 50000, 10000)
    print(woker123.get_full_name())
    print(woker123.position)
    print(woker123.get_total_income())
    
