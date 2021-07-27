n = 0
while n < 1 or n > 9:
    n = int(input('Введите число от 1 до 9:'))

result = n * (1 + 11 + 111)

print(f'Результат расчета = {result}')
