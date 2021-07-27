income = int(input('Введите значение выручки:'))
cost = int(input('Введите значение издержек:'))

profit = income - cost
print('Фирма отработала ' + ('с прибылью' if profit > 0 else 'с убытком'))

if profit > 0:
    profitability = profit / income
    print(f'Рентабельность составила {profitability}')

    employee_count = int(input('Введите количество сотрудников:'))
    profit_per_employee = profit / employee_count
    print(f'Прибыль на одного сотрудника составила {profit_per_employee}')
