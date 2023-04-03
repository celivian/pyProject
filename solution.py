class MinMaxWordFinder:
    def __init__(self):
        self.short = []
        self.long = []
        self.c = True
        self.textsort = []
        self.filtmax = []
        self.filtmin = []
        self.min = 0
        self.max = 0
        self.shr = []

    def add_sentence(self, text):
        self.textsort = sorted(text.split(), key=lambda x: len(x))
        if self.c:
            if text:
                self.min = len(self.textsort[0])
                self.max = len(self.textsort[-1])
                self.filtmin = list(filter(lambda x: len(x) == self.min, self.textsort))
                self.filtmax = list(filter(lambda x: len(x) == self.max, self.textsort))
        else:
            if self.filtmin and self.filtmax:
                self.min = len(self.textsort[0])
                if self.min < len(self.filtmin[0]):
                    self.filtmin = list(filter(lambda x: len(x) == self.min, self.textsort))
                elif self.min >= len(self.filtmin[0]):
                    self.min = len(self.filtmin[0])
                    self.filtmin.extend(list(filter(lambda x: len(x) == self.min, self.textsort)))
                self.max = len(self.textsort[-1])
                if self.max > len(self.filtmax[0]):
                    self.filtmax = list(filter(lambda x: len(x) == self.max, self.textsort))
                elif self.max <= len(self.filtmax[0]):
                    self.max = len(self.filtmax[0])
                self.filtmax.extend(list(filter(lambda x: len(x) == self.max, self.textsort)))
        if self.filtmin and self.filtmax:
            self.c = False
        else:
            self.c = True

    def shortest_words(self):
        self.short = sorted(self.filtmin)
        return self.short

    def longest_words(self):
        self.shr = []
        for i in self.filtmax:
            if i not in self.shr:
                self.shr.append(i)
        self.max = sorted(self.shr)
        return self.max


finder = MinMaxWordFinder()
finder.add_sentence('')
print(' '.join(finder.shortest_words()))
print(' '.join(finder.longest_words()))

finder.add_sentence('bb cc    dd')
finder2 = MinMaxWordFinder()
print(' '.join(finder2.shortest_words()))
print(' '.join(finder2.longest_words()))

print(' '.join(finder.shortest_words()))
print(' '.join(finder.longest_words()))

finder2.add_sentence('bbb ccc    ddc')
finder.add_sentence('zzzz')
finder.add_sentence('p q r')

print(' '.join(finder2.shortest_words()))
print(' '.join(finder2.longest_words()))

print(' '.join(finder.shortest_words()))
print(' '.join(finder.longest_words()))

print(' '.join(finder2.shortest_words()))
print(' '.join(finder2.longest_words()))
