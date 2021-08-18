class Matrix:
    def __init__(self, rows):
        self.__rows = rows

    def __str__(self):
        return '\n'.join([', '.join([str(x) for x in row]) for row in self.__rows])

    def __add__(self, other):
        if len(self.__rows) != len(other.__rows):
            raise Exception('Row count must be equal')
        new_rows = []
        for i in range(len(self.__rows)):
            row = self.__rows[i]
            other_row = other.__rows[i]
            if len(row) != len(other_row):
                raise Exception('Column count must be equal', i)
            new_row = [row[j] + other_row[j] for j in range(len(row))]
            new_rows.append(new_row)

        return Matrix(new_rows)


m1 = Matrix([[1, 2, 3], [4, 5, 6]])
m2 = Matrix([[10, 20, 30], [40, 50, 60]])

print(f'{m1}\n + \n{m2}\n = \n{m1 + m2}')


