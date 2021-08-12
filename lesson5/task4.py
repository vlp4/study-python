def replace_quantitative(s: str) -> str:
    replace = {
        'One': 'один',
        'Two': 'два',
        'Three': 'три',
        'Four': 'четыре',
        'Five': 'пять',
    }
    new_string = s
    for replace_from,  replace_to in replace.items():
        new_string = new_string.replace(replace_from, replace_to)
    return new_string


with open('task4-input.txt') as file_in, open('task4-out.txt', 'w') as file_out:
    for line in file_in:
        new_line = replace_quantitative(line)
        file_out.write(new_line)
