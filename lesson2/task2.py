values = []
while True:
    value = input(f'Введите элемент {len(values) + 1} - ')
    if len(value) < 1:
        break
    values.append(value)

print(f'\nИсходный список:  {values}')

for i in range(0, len(values) // 2 * 2, 2):
    values[i], values[i + 1] = values[i + 1], values[i]

print(f'Список-результат: {values}')
