from itertools import count

from_value = int(input('Введите начальное число:'))
integers = count(from_value)
it = iter(integers)
for i in range(0, 50):
    print('Следующее число -', next(it))