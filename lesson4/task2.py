source = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [source[i] for i in range(1, len(source)) if source[i] > source[i-1]]
print(result)
