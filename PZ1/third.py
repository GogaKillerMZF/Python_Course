n = int(input('Введите n: '))
res = 0
s = 0
for i in range(3):
    res = res * 10 + n
    s += res
print('Ответ: ', s)