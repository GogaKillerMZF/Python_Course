a = int(input('Введите a: '))
b = int(input('Введите b: '))
day = 1
res = a
while res < b:
    res *= 1.1
    day += 1
print('Ответ:', day)