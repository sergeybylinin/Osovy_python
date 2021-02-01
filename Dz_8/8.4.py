"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс,
описывающий склад. А также класс «Оргтехника», который будет базовым
для классов-наследников. Эти классы — конкретные типы оргтехники (принтер,
сканер, ксерокс). В базовом классе определить параметры, общие для
приведенных типов. В классах-наследниках реализовать параметры, уникальные
для каждого типа оргтехники.

5. Продолжить работу над первым заданием. Разработать методы, отвечающие
за приём оргтехники на склад и передачу в определенное подразделение
компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру,
например словарь.

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
пользователем данных. Например, для указания количества принтеров, отправленных
на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники»
максимум возможностей, изученных на уроках по ООП.
"""

class Werehouse:
    """
    Склад
    """
    def __init__(self, nameOffice):
        self.name = nameOffice
        self.listProducts = {}

    def acceptance(self, **products):
        for (item, qty) in products.items():
            self.listProducts[item] = qty
        
    @staticmethod
    def transfer(name1: 'from', name2: 'to'):
        while name1.listProducts:
            print(name1.name)
            i = 0            
            productList = list(name1.listProducts.keys())
            for name in productList:
                i += 1
                print(f'{i}. {name}')
            while True:
                nom = input('Выберете передаваемую технику: ')
                if nom.isdigit() and 0 < int(nom) <= len(name1.listProducts):
                    produktName = productList[int(nom)-1]
                    break
                print(f'Введите номер позиции от 1 до {len(name1.listProducts)}')
            while True:
                qty = input(f'Укажите кол-во передавых позиций\
от 1 до {name1.listProducts[produktName]}: ')
                if qty.isdigit() and 0 < int(qty) <= name1.listProducts[produktName]:
                    qty = int(qty)
                    break
                print(f'Введите номер позиции от 1 до {name1.listProducts[produktName]}')
            name1.listProducts[produktName] -= qty
            if name1.listProducts[produktName] == 0:
                name1.listProducts.pop(produktName)
            if name2.listProducts.get(produktName, 1):
                name2.listProducts[produktName] = qty
            else:
                name2.listProducts[produktName] += qty
            a = input('Продолжить передачу техники y/n? ')
            if a == 'n': break
        else:
            print(f'На складе {name1.name} оргтехники нет')

    def __repr__(self):
        return f'{self.name}'
    
    def __str__(self):
        i = 0
        print(f'{self.name}')
        print('-' * 13)
        for productName in self.listProducts:
            i += 1
            print('%2d. %5s - %d' %
                  (i, productName, self.listProducts[productName]))
        return ''


class OfficeEquipments:
    """
    Офисная техника
    """    
    def __init__(self, name, size: 'l: длина, s: ширина, h: высота',
                 cost: 'in $', workSpeed: 'sheets / min', twoSlider: bool):
        self.name = name
        self.size = size
        self.cost = cost
        self.workSpeed = workSpeed
        self.twoSlider = twoSlider

    def __repr__(self):
        return self.name

    def __str__(self):
        return f'{self.name}\n\
{"mm * ".join(self.size.split("x"))}mm\n\
{self.cost}$\n\
{self.workSpeed} sheets/min'


class Printer(OfficeEquipments):
    """
    Принтер
    """
    def __init__(self, name, size, cost, workSpeed, twoSlider, colorPrint: bool):
        OfficeEquipments.__init__(self, name, size, cost, workSpeed, twoSlider)
        self.colorPrint = colorPrint

    def __str__(self):
        return (OfficeEquipments.__str__(self) +
                f'\n{self.colorPrint} color')


class Scaner(OfficeEquipments):
    """
    Сканер
    """
    def __init__(self, name, size, cost, workSpeed,
                 twoSlider, resolution: '...x...'):
        OfficeEquipments.__init__(self, name, size, cost, workSpeed, twoSlider)
        self.resolution = resolution

    def __str__(self):
        return (OfficeEquipments.__str__(self) +
                f'\n{self.resolution}')
    

class Copier(Printer):
    """
    Копир
    """
    def __init__(self, name, size, cost, workSpeed, resolution,
                 twoSlider, colorPrint):
        Printer.__init__(self, name, size, cost, workSpeed, twoSlider, colorPrint)
        self.resolution = resolution

    def __str__(self):
        return (Printer.__str__(self) +
                f'\n{self.resolution}')
    
if __name__ == '__main__':

    print('8.4'.center(13, '-'))
    hp = Printer('HP Laser 107w', '331x178x215', 7680, 20, False, False)
    print(hp)
    print('-' * 13)
    xerox = Copier('Canon FC-128', '359x439x115', 15000, 4, '1200x600', True, False)
    print(xerox)
    
    print('8.5'.center(13, '-'))
    general = Werehouse('General_Warehouse')
    general.acceptance(xerox=8, hp=5)
    bookkeeping = Werehouse('Bookkeeping')
    Werehouse.transfer(general, bookkeeping)
    print()
    print(general)
    print(bookkeeping)
    
    
