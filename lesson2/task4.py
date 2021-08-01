def truncate(string: str, max_len: int) -> str:
    return string if len(string) <= max_len else string[:max_len] + '...'


value = input('Введите строку из нескольких слов:')
words = [word for word in value.split(' ') if len(word) > 0]

print()
for i in range(len(words)):
    word = words[i]
    print(f'Слово {i + 1}: {truncate(word, 10)}')
