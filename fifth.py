def inputing(name):
    with open(name, 'w') as f:
        for i in range(1,23):
            f.write(str(i) + ' ')
            
            
def counting(name):
    res = 0
    with open(name) as f:
        s = f.readline()
        for i in s.split():
            res += int(i)
    return res


inputing('example2.txt')
print(counting('example2.txt'))