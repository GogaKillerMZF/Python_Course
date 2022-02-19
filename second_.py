class DivZero(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    a = int(input('Первое число: '))
    b = int(input('Второе число: '))
    if b == 0:
        raise DivZero('b = 0, ошибка!')
    else:
        print(f'Результат деления: {a/b}')
except DivZero as ex:
    print(ex)