"""Добавлена проверка на тип переменной отвечающей за количество техники,
проверка достаточного количества техники, при передаче в отдел компании,
возможность слияния складов,
возможность вывода информации о складе
"""


import copy


def check(val):
    try:
        res = int(val)
        return res
    except:
        print('Некорректный тип введенных данных')
        return check(input('Введите корректное значение: '))


class Not_Enough(Exception):
    def __init__(self):
        super().__init__('Не хватает техники требуемой модели')


class Type_Err(Exception):
    def __init__(self):
        super().__init__('Некорректный тип введенных данных')


class Storage:

    def __init__(self, name):
        self.info = {'fastest printing time': float('inf'), 'fastest scanning time': float('inf'),
            'fastest xerox time': float('inf'), 'fastest printer model': '',
            'fastest scanner model': '', 'fastest xerox model': '',
            'printers': {'cls': set(), 'amount': {}}, 'scanners': {'cls': set(), 'amount': {}}, 'xeroxes': {'cls': set(), 'amount': {}}}
        self.name = name

    def getting(self, cls, amount):
        name = type(cls).__name__
        amount = check(amount)
        if name == 'Printer':  # Если на склад привезли принтер
            if cls.model in self.info['printers']['amount']:
                self.info['printers']['amount'][cls.model] += amount
            else:
                self.info['printers']['amount'][cls.model] = amount
            self.info['printers']['cls'].add(cls)
            if self.info['fastest printing time'] > cls.print_speed:
                self.info['fastest printing time'] = cls.print_speed
                self.info['fastest printer model'] = cls.model
        elif name == 'Scanner':  # Если на склад привезли сканер
            if cls.model in self.info['scanners']['amount']:  
                self.info['scanners']['amount'][cls.model] += amount
            else:
                self.info['scanners']['amount'][cls.model] = amount
            self.info['scanners']['cls'].add(cls)
            if self.info['fastest scanning time'] > cls.scanning_time:
                self.info['fastest scanning time'] = cls.scanning_time
                self.info['fastest scanner model'] = cls.model
        else:  # Если на склад привезли ксерокс
            if cls.model in self.info['xeroxes']['amount']:
                self.info['xeroxes']['amount'][cls.model] += amount
            else:
                self.info['xeroxes']['amount'][cls.model] = amount
            self.info['xeroxes']['cls'].add(cls)
            if self.info['fastest xerox time'] > cls.xerox_time:
                self.info['fastest xerox time'] = cls.xerox_time
                self.info['fastest xerox model'] = cls.model

    def transfer(self, cls, amount, department):
        name = type(cls).__name__
        if name == 'Printer':
            try:
                if self.info['printers']['amount'][cls.model] >= amount:
                    self.info['printers']['amount'][cls.model] -= amount
                    print(f'В {department}  передано {amount} принтеров')
                else:
                    raise Not_Enough
            except Not_Enough as err:
                print(err)
                print(f"\В {department}  передано {self.info['printers']['amount'][cls.model]} принтеров")
                self.info['printers']['amount'][cls.model] = 0
        elif name == 'Scanner':
            try:
                if self.info['scanners']['amount'][cls.model] >= amount:
                    self.info['scanners']['amount'][cls.model] -= amount
                    print(f'В {department}  передано {amount} сканеров')
                else:
                    raise Not_Enough
            except Not_Enough as err:
                print(err)
                print(f"\В {department}  передано {self.info['scanners']['amount'][cls.model]} сканнеров")
                self.info['scanners']['amount'][cls.model] = 0
        else:
            try:
                if self.info['xeroxes']['amount'][cls.model] >= amount:
                    self.info['xeroxes']['amount'][cls.model] -= amount
                    print(f'В {department}  передано {amount} ксероксов')
                else:
                    raise Not_Enough
            except Not_Enough as err:
                print(err)
                print(f"\В {department}  передано {self.info['xeroxes']['amount'][cls.model]} ксероксов")
                self.info['xeroxes']['amount'][cls.model] = 0

    def __add__(self, other):
        res = copy.deepcopy(self)
        if res.info['fastest printing time'] > other.info['fastest printing time']:
            res.info['fastest printing time'] = other.info['fastest printing time']
            res.info['fastest printer model'] = other.info['fastest printer model']
        if res.info['fastest scanning time'] > other.info['fastest scanning time']:
            res.info['fastest scanning time'] = other.info['fastest scanning time']
            res.info['fastest scanner model'] = other.info['fastest scanner model']
        if res.info['fastest xerox time'] > other.info['fastest xerox time']:
            res.info['fastest xerox time'] = other.info['fastest xerox time']
            res.info['fastest xerox model'] = other.info['fastest xerox model']
        res.info['printers']['cls'].update(other.info['printers']['cls'])
        res.info['scanners']['cls'].update(other.info['scanners']['cls'])
        res.info['xeroxes']['cls'].update(other.info['xeroxes']['cls'])
        for i in other.info['printers']['amount']:
            if i in res.info['printers']['amount']:
                res.info['printers']['amount'][i] += other.info['printers']['amount'][i]
            else:
                res.info['printers']['amount'][i] = other.info['printers']['amount'][i]
        for i in other.info['scanners']['amount']:
            if i in res.info['scanners']['amount']:
                res.info['scanners']['amount'][i] += other.info['scanners']['amount'][i]
            else:
                res.info['scanners']['amount'][i] = other.info['scanners']['amount'][i]
        for i in other.info['xeroxes']['amount']:
            if i in res.info['xeroxes']['amount']:
                res.info['xeroxes']['amount'][i] += other.info['xeroxes']['amount'][i]
            else:
                res.info['xeroxes']['amount'][i] = other.info['xeroxes']['amount'][i]
        return res

    def __str__(self):
        res = f'\n--------Склад {self.name}--------\n'
        if self.info['fastest printer model'] != '':
            res += f"Самый быстрый принтер на складе: {self.info['fastest printer model']} (время печати - {self.info['fastest printing time']})\n"
        if self.info['fastest scanner model'] != '':
            res += f"Самый быстрый сканер на складе: {self.info['fastest scanner model']} (время сканирования - {self.info['fastest scanning time']})\n"
        if self.info['fastest xerox model'] != '':
            res += f"Самый быстрый ксерокс на складе: {self.info['fastest xerox model']} (время копирования - {self.info['fastest xerox time']})\n\n"
        res += f"\nПринтеры на складе:\n"
        for i in self.info['printers']['amount']:
            res += f"Принтер модели {i} - {self.info['printers']['amount'][i]} ед.\n"
        res += f"\nСканеры на складе:\n"
        for i in self.info['scanners']['amount']:
            res += f"Сканер модели {i} - {self.info['scanners']['amount'][i]} ед.\n"
        res += f"\nКсероксы на складе:\n"
        for i in self.info['xeroxes']['amount']:
            res += f"Ксерокс модели {i} - {self.info['xeroxes']['amount'][i]} ед.\n"
        res += '-------------------------------'
        return res


class Technic:

    def __init__(self, model, year_of_release):
        self.model = model
        self.year_of_release = year_of_release


class Printer(Technic):
    num_of_printers = 0

    def __init__(self, model, year_of_release, paint_volume, print_speed):
        year_of_release = check(year_of_release)
        print_speed = check(print_speed)
        Printer.num_of_printers += 1
        super().__init__(model, year_of_release)
        self.paint_volume = paint_volume
        self.print_speed = print_speed


class Scanner(Technic):
    num_of_scanners = 0

    def __init__(self, model, year_of_release, scanning_time):
        Scanner.num_of_scanners += 1
        scanning_time = check(scanning_time)
        year_of_release = check(year_of_release)
        super().__init__(model, year_of_release)
        self.scanning_time = scanning_time


class Xerox(Technic):
    num_of_xeroxes = 0

    def __init__(self, model, year_of_release, xerox_time):
        Xerox.num_of_xeroxes += 1
        xerox_time = check(xerox_time)
        year_of_release = check(year_of_release)
        super().__init__(model, year_of_release)
        self.xerox_time = xerox_time


main = Storage('Main')
other = Storage('NotMain')
p1 = Printer('K123', 2004, 2, 20)
p2 = Printer('K143', 2008, 3, 10)
p3 = Printer('В1', 2009, 4, 11)
p4 = Printer('В2', 2020, 6, 3)
s1 = Scanner('Vov1', 2000, 20)
s2 = Scanner('Vov1.2', 2010, 10)
s3 = Scanner('Scanf', 2009, 9)
s4 = Scanner('ScanfFast', 2015, 1)
x1 = Xerox('Xex1', 1999, 58)
x2 = Xerox('Xex00', 2000, 34)
x3 = Xerox('VoV1', 2005, 34)
x4 = Xerox('Vov1.1', 2015, 15)
main.getting(p1, 25)
main.getting(p3, 12)
main.getting(s1, 28)
main.getting(s2, 3)
main.getting(s4, 45)
main.getting(x1, 21)
main.getting(x1, 12)
main.getting(x4, 45)
main.getting(x3, 78)
other.getting(p2, 13)
other.getting(p1, 13)
other.getting(s2, 13)
print(other)
print(main)
newMain = main + other
newMain.name = 'NewMain'
print(newMain)
