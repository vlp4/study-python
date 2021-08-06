from functools import reduce

the_list = [n for n in range(100, 1001, 2)]
multiplied = reduce(lambda a, b: a * b, the_list, 1)
print(multiplied)
