import time


class TrafficLight:
    def __init__(self):
        self.__color = 'red'

    def running(self, cycles: int):
        for _ in range(cycles):
            self.__switch()

    def __switch(self):
        states = {
            'red': (7, 'yellow'),
            'yellow': (2, 'green'),
            'green': (3, 'red'),
        }
        print(f'The color is {self.__color} ', end='')
        next_state = states[self.__color]
        for _ in range(next_state[0]):
            time.sleep(1)
            print('.', end='')
        print()
        self.__color = next_state[1]


light = TrafficLight()
light.running(5)
