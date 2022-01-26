n = int(input('Введите количество элементов списка: '))
l = []
for i in range(n):
    l.append(input(f'Введите элемент списка под номером {i + 1}: '))
for i in range(0,n - 1,2):
    l[i], l[i + 1] = l[i + 1], l[i]
print(l)