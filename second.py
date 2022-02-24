def getting(name):
    strings = {}
    with open(name, 'r') as f:
        s = f.readlines()
        counter = 1
        for i in s:
            strings[counter] = len(i)
            counter += 1
    return strings


res = getting('example.txt')
print(f'Количество строк = {len(res)}')
for i in res:
    print(f'Количество символов в строке {i}: {res[i]}')