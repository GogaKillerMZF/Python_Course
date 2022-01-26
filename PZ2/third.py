cal = {'Зима' : [1, 2, 12], 'Весна': [3, 4, 5], "Лето": [6, 7, 8], 'Осень': [9, 10, 11]}
month = int(input('Введите номер месяца: '))
for i in cal.items():
    if month in i[1]:
        print(i[0])
        break
