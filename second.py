class Road:
    
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_mas(self, mas, depth):
        res = self._length * self._width * mas * depth
        return res


r = Road(25, 10)
print(r.calc_mas(25, 5))