def fuct(n):
    res = 1
    for i in range(2, n + 2):
        yield res
        res *= i


for i in fuct(4):
    print(i)