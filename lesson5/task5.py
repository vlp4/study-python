import random

file_name = 'data/task5-out.txt'

# Prepare random numbers in the file:
with open(file_name, 'w') as out:
    out.write(' '.join([str(random.randint(0, 10)) for i in range(4)]))

# Read numbers and calculate their sum:
with open(file_name, 'r') as infile:
    total = 0
    for line in infile:
        numbers = [int(s) for s in line.split(' ') if s.isdigit()]
        total += sum(numbers)

print(f'Сумма чисел в файле: {total}')
