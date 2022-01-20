num = int(input('Введите число: '))
max = 0
while num > 0:
    val = num % 10
    num //= 10
    if val > max:
        max = val
print('Наибольшее число:', max)