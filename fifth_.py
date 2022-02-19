class Storage:
    info = {'fastest printing time': float('inf'), 'fastest scanning time': float('inf'),
            'fastest xerox time': float('inf'), 'fastest printer model': '',
            'fastest scanner model': '', 'fastest xerox model': '',
            'printers': {'cls': set(), 'amount': {}}, 'scanners': {'cls': set(), 'amount': {}}, 'xeroxes': {'cls': set(), 'amount': {}}}

    def __init__(self, name):
        self.name = name

    def getting(self, cls, amount):
        name = cls.__name__
        if name == 'Printer':  #Если на склад привезли принтер
            if cls.model in Storage.info['printers']['amount']:
                Storage.info['printers']['amount'][cls.model] += amount
            else:
                Storage.info['printers']['amount'][cls.model] = amount
            Storage.info['printers']['cls'].add(cls)
            if Storage.info['fastest printing time'] > cls.print_speed:
                Storage.info['fastest printing time'] = cls.print_speed
                Storage.info['fastest printer model'] = cls.model
        elif name == 'Scanner':  #Если на склад привезли сканер
            if cls.model in Storage.info['scanners']['amount']:  
                Storage.info['scanners']['amount'][cls.model] += amount
            else:
                Storage.info['scanners']['amount'][cls.model] = amount
            Storage.info['scanners']['cls'].add(cls)
            if Storage.info['fastest scanning time'] > cls.scanning_time:
                Storage.info['fastest scanning time'] = cls.scanning_time
                Storage.info['fastest scanner model'] = cls.model
        else:  #Если на склад привезли ксерокс
            if cls.model in Storage.info['xeroxes']['amount']:
                Storage.info['xeroxes']['amount'][cls.model] += amount
            else:
                Storage.info['xeroxes']['amount'][cls.model] = amount
            Storage.info['xeroxes']['cls'].add(cls)
            if Storage.info['fastest xerox time'] > cls.xerox_time:
                Storage.info['fastest xerox time'] = cls.xerox_time
                Storage.info['fastest xerox model'] = cls.model

    def transfer(self, cls, amount, department):
        name = cls.__name__
        if name == 'Printer':
            Storage.info['printers']['amount'][cls.model] -= amount
            print(f'В {department}  передано {amount} принтеров')
        elif name == 'Scanner':
            Storage.info['scanners']['amount'][cls.model] -= amount
            print(f'В {department}  передано {amount} сканеров')
        else:
            Storage.info['xeroxes']['amount'][cls.model] -= amount
            print(f'В {department}  передано {amount} ксероксов')
 
 
class Technic:

    def __init__(self, model, year_of_release):
        self.model = model
        self.year_of_release = year_of_release


class Printer(Technic):
    num_of_printers = 0

    def __init__(self, model, year_of_release, paint_volume, print_speed):
        Printer.num_of_printers += 1
        super().__init__(model, year_of_release)
        self.paint_volume = paint_volume
        self.print_speed = print_speed


class Scanner(Technic):
    num_of_scanners = 0

    def __init__(self, model, year_of_release, scanning_time):
        Scanner.num_of_scanners += 1
        super().__init__(model, year_of_release)
        self.scanning_time = scanning_time


class Xerox(Technic):
    num_of_xeroxes = 0

    def __init__(self, model, year_of_release, xerox_time):
        Xerox.num_of_xeroxes += 1
        super().__init__(model, year_of_release)
        self.xerox_time = xerox_time
