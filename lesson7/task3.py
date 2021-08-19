from __future__ import annotations


class Cell:
    def __init__(self, count):
        self.__count = count

    def make_order(self, places: int):
        return '\n'.join(['*' * min(places, self.__count - p) for p in range(0, self.__count, places)])

    def __str__(self) -> str:
        return f'Cell [{self.__count}]'

    @property
    def unit_count(self):
        return self.__count

    def __add__(self, other: Cell):
        return Cell(self.__count + other.__count)

    def __sub__(self, other: Cell):
        return Cell(self.__count - other.__count)

    def __mul__(self, other: Cell):
        return Cell(self.__count * other.__count)

    def __truediv__(self, other: Cell):
        return Cell(self.__count / other.__count)


c1 = Cell(1)
c2 = Cell(2)

print(c1 + c2)
print(c2 - c1)
print(c1 * c2)
print(c1 / c2)

print()
print(Cell(12).make_order(5))
print()
print(Cell(15).make_order(5))
