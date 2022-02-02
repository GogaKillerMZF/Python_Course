def int_func(s):
    return chr(ord(s[0]) - 32) + s[1:]


print(int_func('asd'))