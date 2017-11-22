class Euler75():
    def __init__(self, top):
        self.sq = list()
        for i in range(1, top):
            self.sq.append(i*i)
        print('squares complete')
        self.pyth = dict()
        for i, a2 in enumerate(self.sq):
            print(i)
            for j, b2 in enumerate(self.sq[:i]):
                c2 = a2 + b2
                if c2 in self.sq:
                    k = self.sq.index(c2)
                    circum = i+j+k+3
                    if circum in self.pyth:
                        self.pyth[circum] += 1
                    else:
                        self.pyth[circum] = 1



    def compute(self):
        print(self.pyth)
        for i in self.pyth:
            if self.pyth[i] == 1:
                print(i, self.pyth[i])

if __name__ == '__main__':
    e = Euler75(10000)
    e.compute()