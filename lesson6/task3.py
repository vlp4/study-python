class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)

    def get_full_name(self):
        return f'{self.surname} {self.name}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


ivanov = Position('Ivan', 'Ivanov', 'programmer', {'wage': 1000, 'bonus': 100})
petrov = Position('Petr', 'Petrov', 'tester', {'wage': 800, 'bonus': 80})

for person in [ivanov, petrov]:
    print(f'Зарплата сотрудника {person.get_full_name()} ({person.position}):', person.get_total_income())
