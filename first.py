from time import sleep


class TrafficLight:
    __color_num = {'Зеленый': 0, 'Желтый': 1, 'Красный': 2}
    __num_color = ['Зеленый', 'Желтый', 'Красный', 'Желтый']
    __sleep_time = {0: 3, 1: 2, 2: 7, 3: 2}
    
    def __init__(self, color):
        self.__color = color
    
    def running(self):
        cycles = int(input('Введите количество циклов: '))
        n = TrafficLight.__color_num[self.__color]
        l = [i % 4 for i in range(n,n + 5)]
        print(l)
        for step in range(cycles):
            for i in l:
                print (TrafficLight.__num_color[i])
                sleep(TrafficLight.__sleep_time[i])


ex = TrafficLight('Красный')
ex.running()

        