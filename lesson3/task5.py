
def input_numbers():
    stop_marker = "Q"
    stop_marker_lower = stop_marker.lower()
    s = input(f'Введите числа через пробел. Конец ввода - символ "{stop_marker}":').lower()
    words = s.split(' ')
    found_stop_marker = False
    try:
        stop_position = words.index(stop_marker_lower)
        found_stop_marker = True
    except ValueError:
        stop_position = len(words)
    numbers = [int(word) for word in words[:stop_position] if word.isdigit()]
    return numbers, found_stop_marker


total = 0
found_stop = False
while not found_stop:
    numbers, found_stop = input_numbers()
    numbers_sum = sum(numbers)
    total_new = total + numbers_sum
    print(f'Добавляем введенные числа: {total} + {numbers} = {total_new}')
    total = total_new



