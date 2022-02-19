class Stationery:

    def __init__(self, title):
        self.title = title

    def draw():
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки ручкой "{self.title}"')


class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки карандашом "{self.title}"')


class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки маркером "{self.title}"')


first = Pencil('Special')
second = Pen('Usual')
third = Handle('Super Special')
first.draw()
second.draw()
third.draw()