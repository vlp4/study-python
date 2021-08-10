values = ['Something', 123, False, None, 1.23, [], {}, (), complex(2, -3)]

for value in values:
    print(f'Обнаружен элемент списка типа {type(value)}: {value}')
