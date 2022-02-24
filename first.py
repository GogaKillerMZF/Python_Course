def inputing(name):
    with open(name, 'w') as f:
        s = input("Введите данные (для завершения нажмите Enter): ")
        while s != '':
            f.write(s + '\n')
            s = input("Введите данные (для завершения нажмите Enter): ")


inputing('example.txt')