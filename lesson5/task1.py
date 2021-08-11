with open('task1-out.txt', 'a') as outfile:
    while line := input('Введите строку:'):
        outfile.write(f'{line}\n')

