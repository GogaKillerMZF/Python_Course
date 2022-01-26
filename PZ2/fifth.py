my_list = [55,23,12,2,1,0]
n = int(input('Количество значений: '))
for i in range(n):
    val = int(input('Введите число: '))
    for i in range(len(my_list)):
        if val >= my_list[i]:
            my_list.insert(i, val)
            break
    print(f'Результат: {my_list}\n')