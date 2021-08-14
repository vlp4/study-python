class Road:
    __density = 25

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate_weight(self, thickness):
        return self._width * self._length * thickness * Road.__density


road = Road(5000, 20)
print('Масса асфальта =', road.calculate_weight(5))
