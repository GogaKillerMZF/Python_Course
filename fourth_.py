class Storage:
    pass


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
    num_of_xeroxs = 0
    def __init__(self, model, year_of_release, xerox_time):
        Xerox.num_of_xeroxs += 1
        super().__init__(model, year_of_release)
        self.xerox_time = xerox_time