a = int(input('Введите результат первого дня:'))
b = int(input('Введите требуемый результат:'))

total = None
day_number = 0
while total is None or total < b:
    total = total * 1.1 if total is not None else a
    day_number += 1
    # print(f'{day_number}-й день: {total}')

print(f'Ответ: на {day_number}-й день спортсмен достиг результата — не менее {b} км.')
