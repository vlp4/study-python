def print_user(first_name, last_name, year, city, email, phone):
    print(f'Данные пользователя: {first_name} {last_name}, год рождения: {year}, город проживания: {city},'
          f' почта: {email}, телефон: {phone}')


print_user(
    last_name='Иванов',
    first_name='Иван',
    year='1990',
    city='Москва',
    email='my@email.com',
    phone='+71234567890'
)