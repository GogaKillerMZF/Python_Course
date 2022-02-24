def salary(name):
    res = {'lower_20' : [], 'average' : 0}
    with open(name) as f:
        s = f.readline()
        counter = 0
        while s != '':
            val = s.split()
            val[1] = float(val[1])
            if val[1] < 20000:
                res['lower_20'].append(val[0])
            res['average'] += val[1]
            counter += 1
            s = f.readline()
        res['average'] = round(res['average']/counter, 2)
    return res


print(salary('example.txt'))