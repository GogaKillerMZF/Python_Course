class Data:
    data = ''

    def __init__(self, data):
        Data.data = data

    @classmethod
    def to_int(cls):
        s = cls.data.split('-')
        return tuple((int(s[0]), int(s[1]), int(s[2])))

    @staticmethod
    def check(day, month, year):
        if day > 31 or day < 1:
            print(f"День задан неверно: {day}")
        elif month > 12 or month < 1:
            print(f"Месяц задан неверно: {month}")


d = Data('12-3-2000')
day, month, year = Data.to_int()
Data.check(day, month, year)
d1 = Data("33-3-2000")
day, month, year = Data.to_int()
Data.check(day, month, year)
d2 = Data("31-13-2000")
day, month, year = Data.to_int()
Data.check(day, month, year)
