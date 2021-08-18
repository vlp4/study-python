from abc import ABC, abstractmethod


class Clothing(ABC):
    @abstractmethod
    def calculate_cloth_size(self):
        pass


class Coat(Clothing):
    def __init__(self):
        self.__size_v = None

    def calculate_cloth_size(self):
        return self.__size_v / 6.5 + 0.5

    @property
    def size_v(self):
        return self.__size_v

    @size_v.setter
    def size_v(self, value):
        self.__size_v = value


class Suite(Clothing):
    def __init__(self):
        self.__size_h = None

    def calculate_cloth_size(self):
        return 2 * self.__size_h + 0.3

    @property
    def size_h(self):
        return self.__size_h

    @size_h.setter
    def size_h(self, value):
        self.__size_h = value


coat = Coat()
coat.size_v = 65

suite = Suite()
suite.size_h = 10

cloths = [coat, suite]

total_size = sum([cloth.calculate_cloth_size() for cloth in cloths])

print(f'Расход ткани на пальто: {coat.calculate_cloth_size()}'
      f', расход ткани на костюм: {suite.calculate_cloth_size()}'
      f', общий расход: {total_size}')
