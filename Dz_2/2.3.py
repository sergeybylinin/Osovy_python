"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""
print(__doc__)
print('Решение №1\n')
while True:
    m = int(input('Введите номер месяца: '))
    if m in range(1, 13): break
    else: print('Месяце в году всего 12')
z = ['Зима', 12, 1, 2,]
v = ['Весна', 3, 4, 5]
l = ['Лето', 6, 7, 8]
o = ['Осень', 9, 10, 11]
g = [z, v, l, o]
for i in g:
    if m in i: print(f'{m}-ый месяц - это {i[0]}')
    
print('\nРешение №2\n')
while True:
    m = int(input('Введите номер месяца: '))
    if m in range(1, 13): break
    else: print('Месяце в году всего 12')
g = dict(z = ['Зима', 12, 1, 2,],
         v = ['Весна', 3, 4, 5],
         l = ['Лето', 6, 7, 8],
         o = ['Осень', 9, 10, 11]
         )
for i in g:
    if m in g[i]: print(f'{m}-ый месяц - это {g[i][0]}')
