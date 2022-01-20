proc = int(input('Выручка: '))
costs = int(input('Издержки: '))
if proc > costs:
    staff = int(input('Кол-во работников: '))
    plus = proc - costs
    rent = round(plus / proc, 3)
    for_one = round(plus / staff, 2)
    print(f'Рентабельность: {rent}\nПрибыль на одного работника: {for_one}')
elif proc < costs:
    print('Убыток')
else:
    print('Нейтральная ситуцаия')
