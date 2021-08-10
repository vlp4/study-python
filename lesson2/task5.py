from typing import List


def add_value_to_rating(new_value: int, rating: List[int]):
    insert_at = len(rating)
    for i in range(len(rating)):
        if rating[i] < new_value:
            insert_at = i
            break
    rating.insert(insert_at, new_value)


rating = [7, 5, 3, 3, 2]
print('Текущий рейтинг:', rating)

new_value = None
while new_value is None or new_value <= 0:
    s = input('Введите новое значение:')
    if s.isdigit():
        new_value = int(s)

add_value_to_rating(new_value, rating)
print()
print('Новый рейтинг:', rating)
