from itertools import count, cycle


def since(num):
    for i in count(num):
        print(i)
        if i == 10:
            break


def repeat(seq):
    counter = 0
    for i in cycle(seq):
        print(i)
        counter += 1
        if counter == len(seq) * 3:
            break


since(3)
repeat('Hellow')