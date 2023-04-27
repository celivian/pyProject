class Hanger:
    def __init__(self, namezak, time, oddness=0):
        self.name = namezak
        self.time = time
        self.odd = oddness

    def time_inc(self, n):
        self.time += n
        self.odd += n // 2

    def __add__(self, other):
        return Hanger(self.name.split()[0] + other.name.split()[1], 0, (self.odd + other.odd) // 2)

    def __imod__(self, other):
        self.odd = self.odd % other
        return self

    #def __lt__(self, other):
    #    return self < other
#
    #def __le__(self, other):
    #    return self <= other
#
    #def __eq__(self, other):
    #    return self == other
#
    #def __ne__(self, other):
    #    return self != other
#
    #def __gt__(self, other):
    #    return self > other
#
    #def __ge__(self, other):
    #    return self >= other

    def __str__(self):
        return f'Hanger by name {self.name} ({self.time}, {self.odd})'

    def __call__(self, *args, **kwargs):
        return self.odd * self.time


hg = Hanger('Rual', 3)
print(hg)
hg.time_inc(8)
hg %= 8
print(hg)
print(hg())