"""
2. Создать текстовый файл (не программно),
сохранить в нем несколько строк,
выполнить подсчет количества строк,
количества слов в каждой строке.
"""
print(__doc__)

with open('5.2.txt') as f:
    line = f.readline()
    k = 0
    while line:
        if not line: break
        else: k += 1
        world_count = line.count(' ') + 1
        print(f'В строке #{k} {world_count} слов')
        print(line)
        line = f.readline()
        
        
