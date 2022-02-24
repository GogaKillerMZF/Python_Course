my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
my_dict = {}
for i in my_list:
    if i in my_dict:
        my_dict[i] += 1
    else:
        my_dict[i] = 1
res = [i[0] for i in my_dict.items() if i[1] == 1]
print(res)