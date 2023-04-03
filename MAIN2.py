class SparseArray:
    def __init__(self):
        self.sp = []

    def __setitem__(self, key, value):
        if len(self.sp) < key + 1:
            self.sp.extend([0 for i in range(key - len(self.sp) + 1)])
            self.sp[key] = value
        else:
            self.sp[key] = value

    def __getitem__(self, item):
        if len(self.sp) < item + 1:
            self.sp.extend([0 for i in range(item - len(self.sp) + 1)])
            return self.sp[item]
        return self.sp[item]