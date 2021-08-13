def my_func_1(x, y):
    return x ** y


def my_func_2(x, y):
    value = 1.0
    while y < 0:
        value /= x
        y += 1
    return value


print(my_func_1(10, -2), my_func_2(10, -2))