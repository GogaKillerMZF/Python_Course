def enter_nums(s, val):
    my_list = s.split()
    for i in my_list:
        if i == '+':
            return val
        else:
            val += int(i)
    print(val)
    return enter_nums(input('Введите строку: '), val)


print(enter_nums(input('Введите строку: '), 0))