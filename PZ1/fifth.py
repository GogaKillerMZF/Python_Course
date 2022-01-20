proc = int(input('Выручка: '))
costs = int(input('Издержки: '))
if proc == costs:
    print('Нейтральная ситуация')
else:
    print('Прибыль' if proc > costs else 'Убыток')