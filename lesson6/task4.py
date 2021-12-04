class Car:
    def __init__(self, color, name, is_police):
        self.__speed = 0
        self.__direction = None
        self.__color = color
        self.__name = name
        self.__is_police = is_police

    def go(self, speed, direction):
        self.__speed = speed
        self.__direction = direction
        pass

    def stop(self):
        self.__speed = 0
        pass

    def turn(direction):
        pass

    def _get_speed(self):
        return self.__speed

    def show_speed(self):
        state = f'едет со скоростью {self.__speed} км/ч на {self.__direction}' if self.__speed > 0 else 'стоит на месте'
        print(f'Машина {self.__name} {self.__color}: {state}')


class SpeedLimitCar(Car):
    def __init__(self, max_speed, **kwargs):
        super().__init__(is_police=False, **kwargs)
        self.__max_speed = max_speed

    def show_speed(self):
        super().show_speed()
        if self._get_speed() > self.__max_speed:
            print(f'  >> Превышение скорости! Ограничение =', self.__max_speed)


class TownCar(SpeedLimitCar):
    def __init__(self, **kwargs):
        super().__init__(max_speed=60, **kwargs)


class WorkCar(SpeedLimitCar):
    def __init__(self, **kwargs):
        super().__init__(max_speed=40, **kwargs)


class SportCar(Car):
    def __init__(self, **kwargs):
        super().__init__(is_police=False, **kwargs)


class PoliceCar(Car):
    def __init__(self, **kwargs):
        super().__init__(is_police=True, **kwargs)


town = TownCar(color='red', name='Town car')
police = PoliceCar(color='blue', name='Police car')
work = WorkCar(color='yellow', name='Work car')
sport = SportCar(color='white', name='Sort car')

town.go(80, 'север')
sport.go(160, 'юг')
police.go(150, 'вызов')
work.stop()

for car in (town, sport, police, work):
    car.show_speed()
