seconds_total = int(input('Введите количество секунд:'))

hours = seconds_total // 3600
minutes = seconds_total % 3600 // 60
seconds = seconds_total % 60

print(f'Длительность: {hours:02d}:{minutes:02d}:{seconds:02d}')
