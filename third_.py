class MyEx(Exception):
    def __init__(self):
        super().__init__('Введена строка, необходимо ввести число. Повторите попытку.')


def check(val):
    try:
        int(val)
        return True
    except:
        return False


res = []
while True:
    val = input("Введите элемент спика, для остановки введите 'stop': ")
    if val == 'stop':
        print(res)
        break
    else:
        try:
            if check(val):
                res.append(int(val))
            else:
                raise MyEx
        except MyEx as err:
            print(err)
