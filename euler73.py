from fractions import Fraction


class Euler73():
    def __init__(self, top):
        self.top = top
        self.frac = list()
    def compute(self):
        for i in range (2, self.top+1):
            for j in range(1, i):
                f = Fraction(j,i)
                if f not in self.frac:
                    self.frac.append(f)
        self.frac = sorted(self.frac)
        print(self.frac.index(Fraction(1,3)))
        print(self.frac.index(Fraction(1,2)))

if __name__ == '__main__':
    e = Euler73(100)
    e.compute()
    for i in range(1015, 1522):
        print(e.frac[i])