import json


def getting(name):
    res = [{}, {'average_profit': 0}]
    with open(name, 'r') as f:
        s = f.readlines()
        counter = 0
        for i in s:
            val = i.split()
            profit = int(val[-2]) - int(val[-1])
            res[0][val[0]] = profit
            if profit >= 0:
                res[1]['average_profit'] += profit
                counter += 1
        res[1]['average_profit'] /= counter
    f = open('res.json', 'w')
    json.dump(res, f)
    print(res)
    f.close()


getting('example.txt')
                