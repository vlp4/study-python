from sys import argv

hours, rate, bonus = map(float, argv[1:])

salary = hours * rate + bonus
print('Зарплата сотрудника =', salary)