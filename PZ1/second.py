t = int(input('Введите время в секундах: '))
minutes = t // 60
seconds = t % 60
hours = minutes // 60
minutes %= 60
print(f'Ответ: {hours}:{minutes}:{seconds}')