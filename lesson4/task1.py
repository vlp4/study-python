from sys import argv

hours, rate, bonus = argv

salary = hours * rate + bonus
print('Зарплата сотрудника =', salary)