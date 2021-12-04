from itertools import cycle

source = ['Test', 1, 2, 3, True]
it = iter(cycle(source))

for i in range(0, 50):
    print('Следующее значение -', next(it))
