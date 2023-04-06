class Profile:
    def __init__(self, nameprof):
        self.name = nameprof

    def info(self):
        return ''

    def describe(self):
        print(self.info())


class Vacancy(Profile):
    def __init__(self, nameprof, salary):
        super().__init__(nameprof)
        self.salary = salary

    def info(self):
        return f'Предлагаемая зарплата: {self.salary}'


class Resume(Profile):
    def __init__(self, nameprof, staj):
        super().__init__(nameprof)
        self.staj = staj

    def info(self):
        return f'Стаж работы: {self.staj}'
