"""
5. Создать (программно) текстовый файл, записать в него
программно набор чисел, разделенных пробелами. Программа
должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
print(__doc__)

def num():
    while True:
        number = input('Введите число: ')
        if number.isdigit():
            return number
        else:
            print('\nОшибка!\n')
        
            
print('Введите количество чисел в наборе: ')
kol = int(num())
Sum = 0
k = 0
with open('5.5.txt', 'w') as f:
    print('\nВведите первое число набора.')
    for number in range(kol):
        number = num()
        f.write(number + ' ')
        Sum += int(number)
        k += 1
        if k < kol:
            print('\nВведите следующее число.')
print(f'\nТогда сумма всех чисел набора равна - {Sum}')


