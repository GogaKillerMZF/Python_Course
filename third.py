class Worker:
    
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    
    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        res = self._income['wage'] + self._income['bonus']
        return res


p1 = Position('Gordey', 'Shapovalov', 'Director', {'wage': 10000000, 'bonus': 1000000000})
print(p1.get_full_name())
print(p1.get_total_income())
p2 = Position('Vanua', 'Mamaev', 'Assistant', {'wage': 10000, 'bonus': 1000})
print(p2.get_full_name())
print(p2.get_total_income())
            