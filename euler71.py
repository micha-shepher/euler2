import itertools
from operator import itemgetter

from sympy import igcd
from decimal import Decimal

class Euler71(object):
    def __init__(self, top):
        self.denomi = range(2, top+1)
        self.frac = list()
        for i in self.denomi:
            if i % 10000 == 0:
                print('.')
            jfrom = int(0.4285707*i)
            jto   = int(0.4285724*i) + 1
            for j in range(jfrom, jto):
                if igcd(i, j) == 1:
                    self.frac.append((j, i,))
    def left(self):
        l = list()
        for d, n  in self.frac:
            l.append((d, n, Decimal(d)/Decimal(n)))
        print('sorting.')
        l.sort(key=itemgetter(2))
        where = l.index((3, 7, Decimal(3)/Decimal(7)))

        print(where)
        print(l[where-2:where+3])

if __name__ == '__main__':
    e = Euler71(1000000)
    print(len(e.frac))

    e.left()


