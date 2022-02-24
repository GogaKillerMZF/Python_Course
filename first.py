import sys


def salary(total_time, rate, bonus):
    res = (total_time * rate) + bonus
    return res


args = list(map(int, sys.argv[1:]))
print(salary(args[0], args[1], args[2]))