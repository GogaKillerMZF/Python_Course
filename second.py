from abc import ABCMeta, abstractmethod


class Clothes(metaclass = ABCMeta):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def Expenditure(self):
        pass
    
    
class Coat(Clothes):
    sum_size = 0
    def __init__(self, size, name = ''):
        Coat.sum_size += size
        self.size = size
        super().__init__(name)
    
    
    @property
    def Expenditure(self):
        return round(Coat.sum_size / 6.5 + 0.5, 2)
        
        
class Suit(Clothes):
    sum_height = 0
    def __init__(self, height, name = ''):
        Suit.sum_height += height
        self.height = height
        super().__init__(name)
        
        
    @property
    def Expenditure(self):
        return round(Suit.sum_height * 2 + 0.3, 2)
        
        
c1 = Coat(52)
c2 = Coat(54)
s1 = Suit(182)
s2 = Suit(165)
res1 = c1.Expenditure
res2 = s1.Expenditure
print(f'Расход ткани на пальто: {res1}')
print(f'Расход ткани на костюмы: {res2}')
print(f'Суммарный расход ткани: {res1 + res2}')