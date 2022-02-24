def lessns(name):
    with open(name) as f:
        res = {}
        s = f.readlines()
        for i in s:
            val = i.split(':')
            vals = [int(j.split('(')[0]) for j in val[1].split()]
            if val[0] in res:
                res[val[0]] += sum(vals)
            else:
                res[val[0]] = sum(vals)
    return res


print(lessns('example.txt'))