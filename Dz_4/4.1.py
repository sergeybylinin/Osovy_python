"""
1. Реализовать скрипт, в котором должна быть предусмотрена
функция расчета заработной платы сотрудника. В расчете необходимо
использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать
скрипт с параметрами.
"""

from sys import argv

def payroll(hour: 'выработка в часах', rate: 'cтавка в часах',
            prize: 'премия в денежном эквиваленте'):
    salary = (hour * rate) + prize
    return salary

hour, rate, prize = argv

print('Выработка в часах: ', hour)
print('Ставка в часах: ', rate)
print('Премия: ', prize)
print('Зарплата: ', payroll(hour, rate, prize))


