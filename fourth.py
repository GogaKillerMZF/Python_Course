def change(name):
    with open(name) as f:
        chg = {'One': "Один", 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре', 'Five': "Пять", 'Six': 'Шесть', 'Seven': "Семь", 'Eight': 'Восемь', 'Nine': 'Девять'}
        with open('res.txt', 'w') as res:
            s = f.readlines()
            for i in s:
                val = i.split(' - ')
                val[0] = chg[val[0]]
                i = ' - '.join(val)
                res.write(i)


change('example.txt')