import copy


class ComplexNum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def __add__(self, other):
        res = copy.deepcopy(self)
        res.a += other.a
        res.b += other.b
        return res
    
    def __str__(self):
        if self.b > 0:
            res = f'{self.a} + {self.b}i'
        elif self.b < 0:
            res = f'{self.a} - {self.b * -1}i'
        else:
            res = f'{self.a}'
        return res

    def __mul__(self, other):
        res = copy.deepcopy(self)
        res.a *= other.a
        res.b *= other.b
        return res


first = ComplexNum(1,5)
second = ComplexNum(23, -23)
print(first)
print(second)
print(first + second)
print(first * second)