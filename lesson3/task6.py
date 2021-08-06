def int_func(word: str) -> str:
    if len(word) > 0:
        first_letter = ord(word[0])
        if ord('a') <= first_letter <= ord('z'):
            first_letter += ord('A') - ord('a')
            word = chr(first_letter) + word[1:]
    return word


s = input('Введите слова латинскими буквами через пробел:')
words = s.split(' ')
words_upper = [int_func(word) for word in words]
s_upper = ' '.join(words_upper)
print(f'Исходная строка и строка с заглавными первыми буквами:\n{s}\n{s_upper}')
