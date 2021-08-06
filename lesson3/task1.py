def divide(a: float, b: float) -> float:
    return float('nan') if b == 0 else a / b


a = float(input('Введите делимое:'))
b = float(input('Введите делитель:'))

fraction = divide(a, b)

print(f'Результат деления {a} / {b} = {fraction}')
