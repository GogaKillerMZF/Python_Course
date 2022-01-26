n = int(input('Введите количество товаров: '))
res = []
for i in range(n):
    my_dict = {
        'Название' : input('Введите название: '),
        'Цена' : input('Цена: '),
        'Количество' : input('Количество: '),
        'Ед.' : input('Еденицы: ')   
    }
    res.append(tuple([i + 1, my_dict]))
print(res)
analysis = {}
for i in res:
    for j in i[1].items():
        if j[0] in analysis and j[1] not in analysis[j[0]]:
            analysis[j[0]].append(j[1])
        else:
            analysis[j[0]] = [j[1]]
print(analysis)