def cutting_spot(*sp):
    sp = [*sp]
    sl = {}
    sl[2] = []
    sl[3] = []
    sl[5] = []
    for i in range(len(sp)):
        if len(sp[i]) % 5 == 0:
            sl[5].append(sp[i].capitalize())
        if len(sp[i]) % 3 == 0:
            sl[3].append(sp[i].lower())
        if len(sp[i]) % 2 == 0:
            word = ''
            for j in range(len(sp[i])):
                if sp[i][j].isupper():
                    word += sp[i][j].lower()
                else:
                    word += sp[i][j].upper()
            sl[2].append(word)
    sl[2].sort()
    sl[3].sort()
    sl[5].sort()
    return sl


data = ['scarf', 'Hat', 'sweAter', 'Mittens']
print(cutting_spot(*data))




