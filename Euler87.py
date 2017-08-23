__author__ = 'mshepher'
class Euler87(object):
    def __init__(self):
        self.primes = list()
        plines = open('primes87.txt').readlines()
        for l in plines:
            self.primes.extend([int(i) for i in l.strip().split()])
        self.p2 = [p**2 for p in self.primes]
        self.p3 = [p**3 for p in self.primes[:80]]
        self.p4 = [p**4 for p in self.primes[:30]]


        print(self.p2[:10])
        print(self.p3[:10])
        print(self.p4[:10])


        print(self.p2[-10:])
        print(self.p3[-10:])
        print(self.p4[-10:])

        print(len(self.p2))
        print(len(self.p3))
        print(len(self.p4))

    def gen(self, top):
        for i in self.p2:
            for j in self.p3:
                for k in self.p4:
                    s = i + j + k
                    if s < top:
                        yield s, (i,j,k)

if __name__ == '__main__':
    e = Euler87()
    total = 0
    l = list()
    for i in e.gen(50000000):
        total += 1
        #print(i)
        l.append(i[0])
    print(sorted(l)[-40:])
    print(total)

