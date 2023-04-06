class Summator:
    def __init__(self):

    def transform(self, n):
        return n

    def sum(self, n):
        count = 0
        for i in range(1, n + 1):
            count += self.transform(i)
        return count


class SquareSummator(Summator):
    def transform(self, n):
        return n ** 2


class CubeSummator(Summator):
    def transform(self, n):
        return n ** 3
