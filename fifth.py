from functools import reduce


print(reduce(lambda a, b: a * b, range(100,1001,2)))