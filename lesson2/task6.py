def input_number(prompt: str):
    result = None
    while result is None:
        s = input(prompt)
        if s.isdigit():
            result = int(s)
    return result


def input_good(prompt: str):
    print(prompt)
    good = None
    name = input('Название (введите пустую строку, если больше нет товаров):')
    if len(name) > 0:
        good = {
            'название': name,
            'цена': input_number('Цена:'),
            'количество': input_number('Количество:'),
            'eд': input('Единица измерения:'),
        }
    return good


def analyze_goods(items):
    attribute_values = {}
    for good_item in items:
        for attribute, value in good_item[1].items():
            values = attribute_values.get(attribute)
            if values is None:
                values = {}
                attribute_values[attribute] = values
            values[value] = True
    return {attr: list(values.keys()) for attr, values in attribute_values.items()}


# Initial goods list:
good_items = [
    (1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
    (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'}),
    (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт.'})
]
print('Текущий список товаров:\n', good_items)

# Read more goods from user:
while True:
    good_index = len(good_items) + 1
    good = input_good(f'Введите данные товара №{good_index}')
    if good:
        good_items.append((good_index, good))
    else:
        break
print('\nТовары:\n', good_items)

# Analyze and show result
analysis_result = analyze_goods(good_items)
print('\nАнализ атрибутов товаров: ', analysis_result)
