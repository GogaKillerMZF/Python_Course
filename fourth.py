class Car:
    
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name} поехала')

    def stop(self):
        print(f'Машина {self.name} остановилась')

    def turn(self, direction):
        print(f'Машина {self.name} повернула на {direction}')

    def show_speed(self):
        print(f'Скорость машины {self.name}: {self.speed} км/ч')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f'Машина {self.name} превысила скорость(60 км/ч): {self.speed} км/ч')
        else:
            print(f'Скорость машины {self.name}: {self.speed} км/ч')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f'Машина {self.name} превысила скорость(40 км/ч): {self.speed} км/ч')
        else:
            print(f'Скорость машины {self.name}: {self.speed} км/ч')


first = TownCar(70, 'red', 'Opel', False)
second = SportCar(140, 'green', 'speedy', False)
third = PoliceCar(100, 'black', 'kindy', True)
fourth = WorkCar(220, 'yellow', 'crazy', False)
first.show_speed()
second.show_speed()
third.show_speed()
fourth.show_speed()
print(third.speed)
print(first.speed)
print(second.name)