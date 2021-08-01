n = 0
while n <= 0:
    n = int(input('Введите целое положительное число:'))

max_digit = -1
remainder = n
while remainder > 0:
    digit = remainder % 10
    remainder //= 10
    if digit > max_digit:
        max_digit = digit

print(f'Самая большая цифра в числе {n}:  {max_digit}')
