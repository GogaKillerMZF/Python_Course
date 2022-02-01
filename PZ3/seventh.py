def int_func(s):
    return chr(ord(s[0]) - 32) + s[1:]


def int_funcs(s):
    res = ''
    my_list = s.split()
    for i in range(len(my_list)):
        my_list[i] = int_func(my_list[i])
    return ' '.join(my_list)
        
        
print(int_funcs('asd wer sdf'))
        