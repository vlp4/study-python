def fact(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
        yield result


n = int(input('Введите число N:'))
for el in fact(n):
    print('Следующее число -', el)
