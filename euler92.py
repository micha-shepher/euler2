class Euler92(object):
    def __init__(self):
        self.sq = [i*i for i in range(10)]
        self.s89 = set()
        self.s1 = set()
    def count(self, top):
        for i in range(1, top):
            j = i
            while True:
                j = sum([self.sq[int(k)] for k in list(str(j))])
                if j in self.s89 or j == 89:
                    self.s89.add(i)
                    break
                elif j in self.s1 or j == 1:
                    self.s1.add(i)
                    break

        #print(self.s89)
        #print(self.s1)
        print(len(self.s89))
        print(len(self.s1))

if __name__ == '__main__':
    e = Euler92()
    e.count(10000000)
