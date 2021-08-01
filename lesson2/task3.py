# Prepare season list and dict
season_names = ('Зима', 'Весна', 'Лето', 'Осень')
season_list = [season_names[(i + 1) % 12 // 3] for i in range(12)]
season_dict = {(i + 1): season_list[i] for i in range(12)}
print('Список сезонов: ', season_list)
print('Хеш-таблица сезонов: ', season_dict)

# Get user input
month = 0
while month < 1 or month > 12:
    val = input('Введите номер месяца - ')
    if val.isdigit():
        month = int(val)

# Perform season calculation
season1 = season_list[month - 1]
season2 = season_dict[month]

print()
print(f'Месяц {month}. Время года вычислено с list: {season1}; вычислено с dict: {season2}')