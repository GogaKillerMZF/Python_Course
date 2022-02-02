def my_func(x, y):
    first = x**y
    second = 1
    for i in range(-y):
        second *= x
    second = 1 / second
    print(f'Результат первого способа: {first}\nРезультат второго способа: {second}')
    
    
my_func(2,-2)