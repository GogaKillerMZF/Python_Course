s = input('Введите строку: ')
mas = s.split()
for i in range(len(mas)):
    print(f'{i + 1}) {mas[i][:10]}') if (len(mas[i]) > 10) else print(f'{i + 1}) {mas[i]}')