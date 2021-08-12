people = []
with open('data/task3-input.txt') as file:
    for line in file:
        parts = line.strip().split(' ')
        if len(parts) > 1:
            people.append((parts[0], float(parts[1])))

surnames_lt_20k = [person[0] for person in people if person[1] < 20000]
print('У сотрудников оклад менее 20к: ', surnames_lt_20k)

average_salary = (sum([person[1] for person in people]) / len(people)) if len(people) > 0 else float('nan')
print('Средний оклад: ', average_salary)