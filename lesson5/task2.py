line_word_count = []
with open('task2-input.txt') as file:
    for line in file:
        words = [word for word in line.strip().split(' ') if len(word) > 0]
        line_word_count.append(len(words))

print(f'Количество строк: {len(line_word_count)}. Количество слов в строках: {line_word_count}')
