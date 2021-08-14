class Stationery:
    def __init__(self, title):
        self._title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Рисуем ручкой.')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Рисуем карандашом:', self._title)


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Рисуем маркером.')


pen = Pen('The pen')
pencil = Pencil('The pencil')
handle = Handle('The handle')

for item in (pen, pencil, handle):
    item.draw()
