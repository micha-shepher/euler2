class Euler64():
    def __init__(self, top):
        self.top = top
        self.d = dict()
    def sq(self, n):
        frac = n**0.5
        period = 0
        coef = list()
        fracs = list()
        coef.append(int(frac))
        while not frac in fracs[:-1]:
            frac = 1/(frac-coef[-1])
            fracs.append(frac)
            period += 1
            coef.append(int(frac))
        return period, coef
    def play(self):
        for i in range(2, self.top+1):
            if not (i**0.5).is_integer():
                print(self.sq(i))

if __name__ == '__main__':
    e = Euler64(13)
    e.play()