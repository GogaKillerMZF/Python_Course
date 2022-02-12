class Cell:
    def __init__(self, amount):
        self.amount = amount
        
        
    def __add__(self, other):
        return Cell(self.amount + other.amount)
    
    
    def __sub__(self, other):
        if self.amount > other.amount:
            return Cell(self.amount - other.amount)
        else:
            print('Не хватает ячеек')
            return -1
    
    
    def __mul__(self, other):
        return Cell(self.amount * other.amount)
    
    
    def __truediv__(self, other):
        return Cell(round(self.amount // other.amount))
    
    
    def make_order(self, k):
        res = ''
        for i in range(self.amount // k):
            res += '*' * k + '\n'
        res += '*' * (self.amount % k)
        return res
    
    
c1 = Cell(125)
c2 = Cell(5)
c3 = c1 + c2
print(f'Количество ячеек после сложения: {c3.amount}')
c4 = c1 - c2
print(f'Количество ячеек после вычетания: {c4.amount}')
c5 = c1 * c2
print(f'Количество ячеек после усножения: {c5.amount}')
c6 = c1 / c2
print(f'Количество ячеек после деления: {c6.amount}')
print(f'Своримируем порядок из 130 ячеек (20 ячеек в ряду):\n{c3.make_order(20)}')