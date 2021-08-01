values = []
while True:
    value = input(f'Введите элемент {len(values) + 1} - ')
    if len(value) < 1:
        break
    values.append(value)

print()
print(f'Исходный список:  {values}')

for i in range(len(values) // 2):
    t = values[i * 2]
    values[i * 2] = values[i * 2 + 1]
    values[i * 2 + 1] = t

print(f'Список-результат: {values}')
