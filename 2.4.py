"""
4. Пользователь вводит строку из нескольких слов,
разделённых пробелами. Вывести каждое слово с новой строки.
Строки необходимо пронумеровать. Если в слово длинное,
выводить только первые 10 букв в слове.
"""

print(__doc__)
text = input('Введите строку из нескольких слов: ')
nach = 0
L = []
while True:
    if text.find(' ', nach) != -1:  
        con = text.find(' ', nach)  
        sl = text[nach:con]         
        L.append(sl)                
        nach = con + 1              
    else:                           
        con = len(text)             
        sl = text[nach:con]
        L.append(sl)
        break
i = 1
for el in L:
    print(i, el[:10])
    i += 1
    
