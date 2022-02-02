def division(divider : int, divisor : int):
    """Функция деления
    
    Параметры:
    divider - делимое
    divisor - делитель
    
    """
    return divider/divisor if divisor != 0 else 'Ощибка: деление на ноль'


print(division(5,0))
        